import sys
from os import environ
import xml.etree.ElementTree as ET

from PyQt5 import QtGui

from .nodewidgets import *


class NodeTree(QtWidgets.QTreeWidget):
    def __init__(self, sourceName, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.sourceName = sourceName
        self.pageIndex = 0

        self.setHeaderLabel("Nodes")

        # Create page when item is clicked
        self.itemClicked.connect(self.item_clicked)

    def setPage(self, stack):
        self.nodePage = stack

    def item_clicked(self, item, col_no):
        self.nodePage.create_page(item, self.sourceName)

    def add_item(self, node, parent=None):
        name = node.find('name').text
        treeItem = QtWidgets.QTreeWidgetItem()
        treeItem.setText(0, name)
        treeItem.setExpanded(True)
        treeItem.node = node

        treeItem.pageIndex = self.pageIndex
        self.pageIndex += 1

        textDescription = None

        if parent:
            textDescription = parent.textDescription
            treeItem.level = parent.level + 1
            treeItem.hierarchy = parent.hierarchy + " → " + name

            modifier = "'s" if textDescription[-1] != 's' else "'"
            textDescription = "{}{} {}".format(textDescription, modifier, name)

            parent.addChild(treeItem)
        else:
            textDescription = name
            treeItem.level = 1
            treeItem.hierarchy = name

            self.addTopLevelItem(treeItem)

        treeItem.textDescription = textDescription

        treeItem.textContent = "I want to scrape a {} {}".format(self.sourceName, textDescription)

        return treeItem


class NodePageBox(QtWidgets.QGroupBox):
    def __init__(self, title, content=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.layout = QtWidgets.QFormLayout()
        self.setLayout(self.layout)

        self.setTitle(title)
        if content:
            self.layout.addWidget(content)

    def add_widget(self, widget):
        self.layout.addWidget(widget)


class NodePage(QtWidgets.QWidget):
    def __init__(self, queue, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.queue = queue

        # Add layout
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        # Create a scroll area
        self.pageScroll = QtWidgets.QScrollArea()
        self.pageScroll.setWidgetResizable(True)
        self.pageScroll.setBackgroundRole(QtGui.QPalette.Light)

        # Create a widget that scrolls
        self.pageDescription = QtWidgets.QWidget(self)
        self.pageDescription.layout = QtWidgets.QFormLayout()
        self.pageDescription.setLayout(self.pageDescription.layout)
        self.layout.addWidget(self.pageDescription)
        self.layout.addWidget(self.pageScroll)

        self.pageScroll.setWidget(self.pageDescription)

    def create_page(self, treeItem, sourceName):
        self.clearLayout(self.pageDescription.layout)
        node = treeItem.node

        # Define node information
        nodeName, functionName, inputs = self.get_node_info(node)

        # Create description stack page
        textContent = treeItem.textContent

        # Add title
        title = QtWidgets.QLabel(treeItem.hierarchy)
        title.setStyleSheet("font-weight: bold;")
        self.add_widget(title)

        # Create text description box
        textContentLabel = QtWidgets.QLabel(textContent)
        textContentLabel.setWordWrap(True)
        textContentLabel.setStyleSheet("font-style: italic;")
        textBox = NodePageBox("Text description", textContentLabel)
        self.add_widget(textBox)

        # Create socialreaper box
        srFunctionText = QtWidgets.QLabel("{}().{}()".format(sourceName, functionName))
        srFunction = NodePageBox("Social Reaper function", srFunctionText)
        self.add_widget(srFunction)

        # Create inputs
        inputBox = NodePageInputBox(sourceName, {}, self.queue, functionName)

        # Add advanced box
        advancedBox = AdvancedBox()
        inputBox.layout.addRow("Show all", advancedBox)

        # Add input widget
        self.add_inputs(inputs, inputBox, advancedBox)
        self.add_widget(inputBox)

        # Add download widget
        self.add_download(inputBox)

    def clearLayout(self, layout):
        while layout.count():
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())

    def add_download(self, inputBox):
        # Add download box
        downloadBox = NodePageBox("Download")
        downloadButton = QtWidgets.QPushButton("Add job", downloadBox)
        downloadButton.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        downloadButton.setToolTip("Add a scraping job to the job queue")
        downloadBox.layout.addRow(downloadButton)

        downloadButton.clicked.connect(inputBox.construct_iterator)
        self.add_widget(downloadBox)

    def add_widget(self, widget):
        if isinstance(widget, NodePageInputBox):
            self.read_values = widget.construct_iterator

        self.pageDescription.layout.addWidget(widget)

    def add_setters(self, setters, inputBox, table):
        if setters:
            for setter in setters:
                setterName = setter.find('name').text
                setterType = setter.find('type').text
                setterValue = setter.find('value').text

                setterWidget = None
                if setterType == "counter":
                    setterWidget = CounterSetter(int(setterValue), table, "count")
                inputBox.layout.addRow(setterName, setterWidget)

    def add_inputs(self, inputs, inputBox, advancedBox):
        for input in inputs.findall('input'):
            inputName = input.find('name').text
            inputType = input.find('type').text
            inputRequired = bool(input.attrib.get('required'))

            inputWidget = None

            if inputType == "text":
                inputWidget = NodeInputLine(inputRequired, inputBox)

            elif inputType == "list":
                inputWidget = NodeInputList(inputRequired, inputBox)
                inputWidget.add_elements(input.find('elems'))

            elif inputType == "arguments":
                # Create table
                rows = input.find('rows')
                argumentTable = NodeInputArgs(rows, inputRequired, inputBox)

                # Add table setters
                setters = input.find('setters')
                self.add_setters(setters, inputBox, argumentTable)

                inputWidget = argumentTable

            else:
                sys.exit("UNKNOWN WIDGET")

            rowLabel = QtWidgets.QLabel(inputName)
            rowLabel.setVisible(inputWidget.required)
            inputBox.add_input(rowLabel, inputWidget)

            if not inputWidget.required:
                advancedBox.addRow(rowLabel, inputWidget)

    @staticmethod
    def get_node_info(node):
        name = node.find('name').text
        functionName = node.find('function').text
        inputs = node.find('inputs')

        return name, functionName, inputs


class NodePageInputBox(NodePageBox):
    def __init__(self, sourceName, sourceArgs, queue, functionName):
        super().__init__("Input")

        self.queue = queue

        self.sourceName = sourceName
        self.sourceArgs = {'api_key': environ.get('api_key')}
        self.functionName = functionName

        self.inputs = []

    def add_input(self, name, input):
        self.layout.addRow(name, input)
        self.inputs.append(input)

    def read_values(self):
        arguments = ", ".join([inputWidget.get_value() for inputWidget in self.inputs])
        return arguments

    def construct_iterator(self):
        functionArgs = self.read_values()
        self.queue.add_iterator(self.sourceName, self.sourceArgs, self.functionName, functionArgs, "C:")


class SourceTabs():
    def __init__(self, window, sourceFile):
        self.window = window
        self.sourceFile = sourceFile

        self.sources = self.read_sources()
        self.add_sources()

    @staticmethod
    def tree_click(item, column_no):
        item.sourceDescription.setCurrentIndex(item.pageIndex)

    def read_sources(self):
        tree = ET.parse(self.sourceFile)
        sourceRoot = tree.getroot()
        sources = sourceRoot.findall('source')

        return sources

    def add_sources(self):
        for source in self.sources:
            sourcePage, sourceName = self.create_source_page(source)
            nodeTree = self.create_node_tree(sourcePage, sourceName)
            nodePage = self.create_node_page(sourcePage, self.window.queue)
            nodeTree.setPage(nodePage)

            # Add source nodes to sourceTree and sourceDescription
            self.create_nodes(sourceName, source, nodeTree, nodePage)

            # Select the first node
            topItem = nodeTree.topLevelItem(0)
            if topItem:
                topItem.setSelected(True)
                nodeTree.item_clicked(topItem, 0)

    def create_source_page(self, source):
        sourcePage = QtWidgets.QWidget()
        sourceName = source.find('name').text
        self.window.sourcesTabs.addTab(sourcePage, sourceName)
        sourcePage.layout = QtWidgets.QHBoxLayout()
        sourcePage.setLayout(sourcePage.layout)

        return sourcePage, sourceName

    def create_node_tree(self, sourcePage, sourceName):
        nodeTree = NodeTree(sourceName)
        sourcePage.layout.addWidget(nodeTree)
        return nodeTree

    def create_node_page(self, sourcePage, queue):
        sourceDescription = NodePage(queue)
        sourcePage.layout.addWidget(sourceDescription)

        return sourceDescription

    def create_nodes(self, sourceName, parentNode, treeWidget, nodeStack, treeParentItem=None,
                     textDescription=""):

        nodes = parentNode.find('children')
        for node in nodes.findall('node'):
            # Create tree node
            treeItem = treeWidget.add_item(node, treeParentItem)
            self.create_nodes(sourceName, node, treeWidget, nodeStack, treeItem, textDescription)

    def add_setters(self, setters, inputBox, table):
        if setters:
            for setter in setters:
                setterName = setter.find('name').text
                setterType = setter.find('type').text
                setterValue = setter.find('value').text

                setterWidget = None
                if setterType == "counter":
                    setterWidget = CounterSetter(int(setterValue), table, "count")
                inputBox.layout.addRow(setterName, setterWidget)

    def add_inputs(self, inputs, inputBox, advancedBox):
        for input in inputs.findall('input'):
            inputName = input.find('name').text
            inputType = input.find('type').text
            inputRequired = bool(input.attrib.get('required'))

            inputWidget = None

            if inputType == "text":
                inputWidget = NodeInputLine(inputRequired, inputBox)

            elif inputType == "list":
                inputWidget = NodeInputList(inputRequired, inputBox)
                inputWidget.add_elements(input.find('elems'))

            elif inputType == "arguments":
                # Create table
                rows = input.find('rows')
                argumentTable = NodeInputArgs(rows, inputRequired, inputBox)

                # Add table setters
                setters = input.find('setters')
                self.add_setters(setters, inputBox, argumentTable)

                inputWidget = argumentTable

            else:
                sys.exit("UNKNOWN WIDGET")

            rowLabel = QtWidgets.QLabel(inputName)
            rowLabel.setVisible(inputWidget.required)
            inputBox.add_input(rowLabel, inputWidget)

            if not inputWidget.required:
                advancedBox.addRow(rowLabel, inputWidget)

    @staticmethod
    def get_node_info(node):
        name = node.find('name').text
        functionName = node.find('function').text
        inputs = node.find('inputs')

        return name, functionName, inputs

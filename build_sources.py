import xml.etree.ElementTree as ET
import sys
import json
from collections import OrderedDict

from PyQt5 import QtCore, QtGui, QtWidgets

from socialreaper import Facebook


class AdvancedBox(QtWidgets.QCheckBox):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.child_items = []

        self.stateChanged.connect(self.changeVisibility)

    def addRow(self, label, widget):
        self.child_items.append(label)
        self.child_items.append(widget)

    def changeVisibility(self, state):
        for item in self.child_items:
            item.setVisible(not item.isVisible())


class ArgTableItem(QtWidgets.QTableWidgetItem):
    def __init__(self, value, table, parent=None):
        super().__init__()
        QtWidgets.QWidget.__init__(self, parent)

        self.setText(value)
        self.table = table
        self.old_value = value


class ArgTableArg(ArgTableItem):
    def __init__(self, value, table, pair, parent=None):
        super().__init__(value, table, parent)
        self.pair = pair


class ArgTableVal(ArgTableItem):
    def __init__(self, value, table, pair, parent=None):
        super().__init__(value, table, parent)
        self.pair = pair


class ArgTablePair():
    def __init__(self, key, value, table):
        self.arg = ArgTableArg(key, table, self)
        self.val = ArgTableVal(value, table, self)

    def argument(self):
        return self.arg

    def value(self):
        return self.val

    def pair(self):
        return self.arg, self.val


class NodeTree(QtWidgets.QTreeWidget):
    def __init__(self, sourceName, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.sourceName = sourceName
        self.pageIndex = 0

        self.setHeaderLabel("Nodes")
        self.itemClicked.connect(self.item_clicked)

    def set_stack(self, stack):
        self.nodeStack = stack

    def item_clicked(self, item, col_no):
        self.nodeStack.setCurrentIndex(item.pageIndex)

    def add_item(self, name, parent=None):
        treeItem = QtWidgets.QTreeWidgetItem()
        treeItem.setText(0, name)
        treeItem.setExpanded(True)

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


class NodeStackPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.read_values = lambda : print("No input added")

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

    def add_widget(self, widget):
        if isinstance(widget, NodeInputBox):
            self.read_values = widget.read_values

        self.pageDescription.layout.addWidget(widget)


    def display_values(self, clicked):
        print(self.read_values())

    def add_download(self):
        # Add download box
        downloadBox = NodePageBox("Download")
        downloadButton = QtWidgets.QPushButton("Add job", downloadBox)
        downloadButton.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        downloadButton.setToolTip("Add a scraping job to the job queue")
        downloadBox.layout.addRow(downloadButton)

        downloadButton.clicked.connect(self.display_values)
        self.add_widget(downloadBox)


class NodeInputBox(NodePageBox):
    def __init__(self):
        super().__init__("Input")

        self.inputs = []

    def add_input(self, name, input):
        self.layout.addRow(name, input)
        self.inputs.append(input)

    def read_values(self):
        arguments = ", ".join([inputWidget.get_value() for inputWidget in self.inputs])
        return arguments


class NodeInputWidget():
    def __init__(self, required=True):
        self.required = required
        self.setVisible(self.required)

    def get_value(self):
        pass


class NodeInputArgs(QtWidgets.QTableWidget, NodeInputWidget):
    def __init__(self, rows=None, required=True, parent=None):
        super().__init__(0, 2, parent)
        NodeInputWidget.__init__(self, required=required)


        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
        self.setHorizontalHeaderLabels(['Argument', 'Value'])

        self.arguments = OrderedDict()

        self.itemChanged.connect(self.item_changed)

        if rows:
            self.read_rows(rows)

        self.fill_table()

    def read_rows(self, rows):
        for row in rows:
            argument = row[0].text
            value = row[1].text
            self.set_argument(argument, value)

    def item_changed(self, item):
        if isinstance(item, ArgTableArg):
            old_arg = item.old_value
            if old_arg != "":
                value = self.arguments.pop(old_arg)
            else:
                value = item.pair.value().text()
            new_key = item.text()
            if new_key:
                self.arguments[new_key] = value

        elif isinstance(item, ArgTableVal):
            argument = item.pair.argument().text()
            value = item.text()

            if value == "" and argument == "":
                self.arguments.pop("")
            else:
                self.arguments[argument] = value

        self.fill_table()

    def set_argument(self, arg, value):
        self.arguments[arg] = value

    def remove_argument(self, arg):
        del self.arguments[arg]

    def inc_rows(self):
        self.setRowCount(self.rowCount() + 1)
        return self.rowCount()

    def add_row(self, argument, value):
        self.itemChanged.disconnect(self.item_changed)
        rowCount = self.inc_rows()

        argItem, valItem = ArgTablePair(str(argument), str(value), self).pair()

        self.setItem(rowCount - 1, 0, argItem)
        self.setItem(rowCount - 1, 1, valItem)
        self.itemChanged.connect(self.item_changed)

    def fill_table(self):
        self.setRowCount(0)
        for key, value in self.arguments.items():
            self.add_row(key, value)

        self.add_row("", "")

    def get_value(self):
        return json.dumps(self.arguments)


class NodeInputLine(QtWidgets.QLineEdit, NodeInputWidget):
    def __init__(self, required=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        NodeInputWidget.__init__(self, required=required)

    def get_value(self):
        return json.dumps(self.text())


class NodeInputList(QtWidgets.QListWidget, NodeInputWidget):
    def __init__(self, required=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        NodeInputWidget.__init__(self, required=required)

        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setToolTip("Ctrl + Click to deselect list items")

    def add_elements(self, elements):
        for element in elements:
            listItem = QtWidgets.QListWidgetItem(element.text, self)
            self.addItem(listItem)

    def get_value(self):
        return json.dumps([item.text() for item in self.selectedItems()])


class CounterSetter(QtWidgets.QSpinBox):
    def __init__(self, value, table, argument, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setMinimum(0)
        self.setMaximum(999999999)

        self.table = table
        self.argument = argument
        self.valueChanged.connect(self.set_arg)
        self.setValue(value)

    def set_arg(self, value):
        self.table.set_argument(self.argument, value)
        self.table.fill_table()


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
            nodeStack = self.create_node_stack(sourcePage)
            nodeTree.set_stack(nodeStack)

            # Add source nodes to sourceTree and sourceDescription
            self.create_nodes(sourceName, source, nodeTree, nodeStack)

            # Select the first node
            topItem = nodeTree.topLevelItem(0)
            if topItem:
                topItem.setSelected(True)

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

    def create_node_stack(self, sourcePage):
        sourceDescription = QtWidgets.QStackedWidget()
        sourcePage.layout.addWidget(sourceDescription)

        return sourceDescription

    def create_nodes(self, sourceName, parentNode, treeWidget, nodeStack, treeParentItem=None,
                     textDescription=""):

        nodes = parentNode.find('children')
        for node in nodes.findall('node'):
            # Define node information
            nodeName, functionName, inputs = self.get_node_info(node)

            # Create tree node
            treeItem = treeWidget.add_item(nodeName, treeParentItem)

            # Create description stack page
            pageStack = NodeStackPage()
            textContent = treeItem.textContent

            # Add title
            title = QtWidgets.QLabel(treeItem.hierarchy)
            title.setStyleSheet("font-weight: bold;")
            pageStack.add_widget(title)

            # Create text description box
            textContentLabel = QtWidgets.QLabel(textContent)
            textContentLabel.setWordWrap(True)
            textContentLabel.setStyleSheet("font-style: italic;")
            textBox = NodePageBox("Text description", textContentLabel)
            pageStack.add_widget(textBox)

            # Create socialreaper box
            srFunctionText = QtWidgets.QLabel("{}().{}()".format(sourceName, functionName))
            srFunction = NodePageBox("Social Reaper function", srFunctionText)
            pageStack.add_widget(srFunction)

            # Create inputs
            inputBox = NodeInputBox()

            # Add advanced box
            advancedBox = AdvancedBox()
            inputBox.layout.addRow("Show all", advancedBox)

            # Add input widget
            self.add_inputs(inputs, inputBox, advancedBox)
            pageStack.add_widget(inputBox)

            # Add download widget
            pageStack.add_download()

            # Add page to stack
            nodeStack.addWidget(pageStack)
            nodeStack.setCurrentIndex(0)

            # Recurse through children
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
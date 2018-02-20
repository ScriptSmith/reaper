import sys
import xml.etree.ElementTree as ET
from os import environ, getcwd, sep, path

from components.widgets.nodes import *


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
    def __init__(self, title, content=None, layout=QtWidgets.QVBoxLayout, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.layout = layout()
        self.setLayout(self.layout)

        self.setTitle(title)
        if content:
            self.layout.addWidget(content)

    def add_widget(self, widget):
        self.layout.addWidget(widget)


class NodePage(QtWidgets.QWidget):
    def __init__(self, mainWindow, primaryInputWindow, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.mainWindow = mainWindow
        self.queue = mainWindow.queue
        self.queue_table = mainWindow.queue_table
        self.primaryInputWindow = primaryInputWindow

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
        self.pageDescription.layout = QtWidgets.QVBoxLayout()
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
        inputBox = NodePageInputBox(sourceName, self.queue, self.queue_table, functionName)
        inputBox.add_iterator.connect(self.queue.add_jobs)

        # Add advanced box
        advancedBox = AdvancedBox()
        inputBox.layout.addRow("Show all", advancedBox)

        # Add input widget
        self.add_inputs(inputs, inputBox, advancedBox)
        self.add_widget(inputBox)

        if self.mainWindow.advanced_mode:
            advancedBox.toggle()

        # Add download widget
        downloadBox = NodePageDownloadBox(inputBox)
        self.add_widget(downloadBox)

        inputBox.path_function = downloadBox.get_path

        # Add primary key listener
        inputBox.primary.fileText.connect(downloadBox.set_path)

        self.add_widget(QtWidgets.QSplitter(QtCore.Qt.Vertical))

    def clearLayout(self, layout):
        while layout.count():
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    self.clearLayout(child.layout())

    def add_widget(self, widget):
        if isinstance(widget, NodePageInputBox):
            self.read_values = widget.construct_iterator

        self.pageDescription.layout.addWidget(widget)

    def add_setters(self, setters, inputBox, table):
        if setters:
            for setter in setters:
                setterName = setter.find('name').text
                setterArg = setter.find('argument').text
                setterType = setter.find('type').text
                setterValue = setter.find('value').text

                setterWidget = None
                if setterType == "counter":
                    setterWidget = CounterSetter(int(setterValue), table, setterArg)

                elif setterType == "checkbox":
                    setterWidget = CheckboxSetter(bool(setterValue), table, setterArg)

                elif setterType == "list":
                    setterWidget = ListSetter(setterValue.split(","), table, setterArg)
                inputBox.layout.addRow(setterName, setterWidget)

    def add_inputs(self, inputs, inputBox, advancedBox):
        for input in inputs.findall('input'):
            inputName = input.find('name').text
            inputType = input.find('type').text
            inputRequired = bool(input.attrib.get('required'))

            inputWidget = None

            if inputType == "primary":
                inputWidget = NodeInputPrimary(self.primaryInputWindow, inputBox)

            elif inputType == "text":
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
            else:
                inputBox.add_required(inputWidget)

    @staticmethod
    def get_node_info(node):
        name = node.find('name').text
        functionName = node.find('function').text
        inputs = node.find('inputs')

        return name, functionName, inputs


class NodePageDownloadBox(NodePageBox):
    def __init__(self, inputBox):
        super().__init__("Download", layout=QtWidgets.QFormLayout)

        self.setEnabled(False)
        self.add_path()
        self.add_name()
        self.add_button(inputBox)

        inputBox.downloadBox = self

    def add_path(self):
        pathWidget = QtWidgets.QWidget()
        pathWidget.layout = QtWidgets.QHBoxLayout()
        pathWidget.setLayout(pathWidget.layout)
        pathWidget.layout.setContentsMargins(0, 0, 0, 0)

        self.dirPath = QtWidgets.QLabel(getcwd())
        pathWidget.layout.addWidget(self.dirPath)

        pathWidget.layout.addStretch(1)

        self.pathButton = QtWidgets.QPushButton("Choose folder")
        pathWidget.layout.addWidget(self.pathButton)
        self.pathButton.clicked.connect(self.open_dir)

        self.layout.addRow("Folder", pathWidget)

    def add_name(self):
        self.fileName = QtWidgets.QLineEdit()
        self.fileName.setToolTip("Adding {key} to the file name will replace the {key} with the primary key")
        self.fileName.setText(".csv")
        self.layout.addRow("File name", self.fileName)

    def add_button(self, inputBox):
        downloadButton = QtWidgets.QPushButton("Add job", self)

        downloadButton.setSizePolicy(
            QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        downloadButton.setToolTip("Add a scraping job to the job queue")
        self.layout.addWidget(downloadButton)

        downloadButton.clicked.connect(inputBox.construct_iterator)

    def get_path(self):
        dir = self.dirPath.text()
        file = self.fileName.text()
        return dir + sep + file

    def set_path(self, text):
        self.fileName.setText(text + ".csv")

    def open_dir(self, _):
        print("opening dir")
        options = QtWidgets.QFileDialog.Options()

        title = "Open folder"
        directory = ""

        dirPath = QtWidgets.QFileDialog.getExistingDirectory(caption=title, directory=directory, options=options)
        if dirPath:
            self.dirPath.setText(path.abspath(dirPath))


class NodePageInputBox(NodePageBox):
    add_iterator = QtCore.pyqtSignal(list)

    def __init__(self, sourceName, queue, queueTable, functionName):
        super().__init__("Input", layout=QtWidgets.QFormLayout)

        self.queue = queue
        self.queueTable = queueTable

        self.queue.job_table.connect(self.queueTable.display_jobs)
        # self.queue.progress_table.connect(self.progressTable.display_value)

        self.downloadBox = None

        self.sourceName = sourceName
        self.sourceArgs = {'api_key': environ.get('api_key')}
        self.sourceArgs = {
            'api_key': "EFlxjNX2RobPexqWY2k0jCJZb",
            'api_secret': "MKCWguSxQjUOMVTocnq0z7onqUpW7B9LFX6EVaCgCEwgAjiwSj",
            'access_token': "706601329-TKRz5TOCpeiICuPqRrq7yvJZWEk5D1Dg0MMz5lzK",
            'access_token_secret': "sWZpLKa9obzuTWqUu4OE0CZ8Wj3Xa88o3acIC9crZgobL"
        }
        self.sourceArgs = {"application_id": "USnY_aKOHDd32w", "application_secret": "wxzi-vu1KXJBr-FEZIO352iUM4E"}
        self.sourceArgs = {"api_key": "AIzaSyAFzLtWI6FiIDkEpLtjXtFhdSEnRJ7qLso"}
        self.functionName = functionName

        self.inputs = []
        self.required = []

    def add_input(self, name, input):
        if isinstance(input, NodeInputPrimary):
            self.primary = input
        self.layout.addRow(name, input)
        self.inputs.append(input)

    def read_values(self):
        primary_keys = self.primary.get_value()
        jobs = []
        for primary_key in primary_keys:
            arguments = ", ".join([inputWidget.get_value() for inputWidget in self.inputs[1:]])
            arguments = primary_key + ", " + arguments
            jobs.append((primary_key.replace('"', ""), arguments))
        return jobs

    def construct_iterator(self):
        filePathKey = self.path_function()

        details = []

        for primary_key, args in self.read_values():
            filePath = filePathKey.replace("{key}", primary_key)
            # details.append((self.sourceName, self.sourceArgs, self.functionName, args, filePath))
            details.append((filePath, self.sourceName, self.functionName, args, self.sourceArgs))
            # outputPath, sourceName, functionName, functionArgs, sourceKeys

        self.add_iterator.emit(details)

    def add_required(self, input):
        self.required.append(False)
        required_i = len(self.required) - 1

        input.containsValue.connect(lambda bool: self.required_changed(required_i, bool))

    def required_changed(self, i, bool):
        if i < len(self.required):
            self.required[i] = bool

        for req in self.required:
            if not req:
                self.downloadBox.setEnabled(False)
                return

        self.downloadBox.setEnabled(True)


class SourceTabs():
    def __init__(self, mainWindow, sourceFile, primaryInputWindow):
        self.mainWindow = mainWindow
        self.primaryInputWindow = primaryInputWindow
        self.sourceFile = sourceFile

        self.sources = self.read_sources()
        self.add_sources()

    @staticmethod
    def tree_click(item, column_no):
        item.sourceDescription.setCurrentIndex(item.pageIndex)

    def read_sources(self):
        tree = ET.parse(self.sourceFile)
        sources_root = tree.getroot()
        source_files = sources_root.findall('source')

        sources = []

        for source_file in source_files:
            location = source_file.find('location').text

            source_tree = ET.parse(f"sources/{location}")
            source_root = source_tree.getroot()
            sources.append(source_root)

        return sources

    def add_sources(self):
        for source in self.sources:
            sourcePage, sourceName = self.create_source_page(source)

            nodeTree = NodeTree(sourceName)
            sourcePage.layout.addWidget(nodeTree)

            nodePage = NodePage(self.mainWindow, self.primaryInputWindow)
            sourcePage.layout.addWidget(nodePage)

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
        self.mainWindow.sourcesTabs.addTab(sourcePage, sourceName)
        sourcePage.layout = QtWidgets.QHBoxLayout()
        sourcePage.setLayout(sourcePage.layout)

        return sourcePage, sourceName

    def create_nodes(self, sourceName, parentNode, treeWidget, nodeStack, treeParentItem=None,
                     textDescription=""):

        nodes = parentNode.find('children')
        for node in nodes.findall('node'):
            # Create tree node
            treeItem = treeWidget.add_item(node, treeParentItem)
            self.create_nodes(sourceName, node, treeWidget, nodeStack, treeItem, textDescription)

    @staticmethod
    def get_node_info(node):
        name = node.find('name').text
        functionName = node.find('function').text
        inputs = node.find('inputs')

        return name, functionName, inputs

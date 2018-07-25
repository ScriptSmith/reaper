import sys
import xml.etree.ElementTree as ET
from os import sep, path

from PyQt5 import QtWidgets, QtCore, QtGui
from components.globals import BUNDLE_DIR
from components.widgets.nodes import PathWidget, CounterSetter, NodeInputPrimary, NodeInputLine, NodeInputList, \
    NodeInputArgs, CheckboxSetter, ListSetter


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
        name = node.find("name").text
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

            modifier = "'s" if textDescription[-1] != "s" else "'"
            textDescription = "{}{} {}".format(textDescription, modifier, name)

            parent.addChild(treeItem)
        else:
            textDescription = name
            treeItem.level = 1
            treeItem.hierarchy = name

            self.addTopLevelItem(treeItem)

        descriptionNode = node.find("description")
        if isinstance(descriptionNode, ET.Element):
            textDescription = descriptionNode.text

        treeItem.textDescription = textDescription

        treeItem.textContent = "Scrape a {} {}".format(
            self.sourceName, textDescription
        )

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

    def __init__(self, reaper, primaryInputWindow, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.mainWindow = reaper
        self.queue = reaper.queueThread
        self.keys = reaper.mainTabs.keyTab
        self.queue_table = reaper.mainTabs.queueTab.table
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
        inputBox = NodePageInputBox(
            sourceName, self.queue, self.queue_table, self.keys, functionName
        )
        inputBox.add_iterator.connect(self.queue.add_jobs)

        # Add advanced box
        from .widgets.nodes import AdvancedBox
        advancedBox = AdvancedBox()
        inputBox.layout.addRow("Show all", advancedBox)

        # Add input widget
        self.add_inputs(inputs, inputBox, advancedBox)
        self.add_widget(inputBox)

        if self.mainWindow.advanced_mode:
            advancedBox.toggle()

        # Add download widget
        downloadBox = NodePageDownloadBox(
            inputBox, self.mainWindow.settings_window.get_save_path()
        )
        self.add_widget(downloadBox)

        inputBox.path_function = downloadBox.get_path

        # Add primary key listener
        inputBox.primary[0].fileText.connect(downloadBox.set_path)

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
            self.read_values = widget.construct_job

        self.pageDescription.layout.addWidget(widget)

    def add_setters(self, setters, inputBox, table):
        if setters:
            for setter in setters:
                setterName = setter.find("name").text
                setterArg = setter.find("argument").text
                setterType = setter.find("type").text
                setterValue = setter.find("value").text

                setterWidget = None
                if setterType == "counter":
                    setterWidget = CounterSetter(int(setterValue), table, setterArg)

                elif setterType == "checkbox":
                    setterWidget = CheckboxSetter(bool(setterValue), table, setterArg)

                elif setterType == "list":
                    setterWidget = ListSetter(setterValue.split(","), table, setterArg)
                inputBox.layout.addRow(setterName, setterWidget)

    def add_inputs(self, inputs, inputBox, advancedBox):
        for input in inputs.findall("input"):
            inputName = input.find("name").text
            inputType = input.find("type").text
            inputRequired = bool(input.attrib.get("required"))

            inputWidget = None

            if inputType == "primary":
                inputWidget = NodeInputPrimary(
                    self.primaryInputWindow, self.mainWindow, inputBox
                )

            elif inputType == "text":
                inputWidget = NodeInputLine(inputRequired, inputBox)

            elif inputType == "list":
                inputWidget = NodeInputList(inputRequired, inputBox)
                inputWidget.add_elements(input.find("elems"))

            elif inputType == "arguments":
                # Create table
                rows = input.find("rows")
                argumentTable = NodeInputArgs(rows, inputRequired, inputBox)

                # Add table setters
                setters = input.find("setters")
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
        name = node.find("name").text
        functionName = node.find("function").text
        inputs = node.find("inputs")

        return name, functionName, inputs


class NodePageDownloadBox(NodePageBox):

    def __init__(self, inputBox, save_path):
        super().__init__("Download", layout=QtWidgets.QFormLayout)

        self.setEnabled(False)
        self.pathWidget = PathWidget(save_path)
        self.layout.addRow("Folder", self.pathWidget)
        self.add_name()
        self.add_options(inputBox)
        self.add_button(inputBox)

        inputBox.downloadBox = self

    def add_name(self):
        self.fileName = QtWidgets.QLineEdit()
        self.fileName.setToolTip(
            "Adding {key} to the file name will replace the {key} with the primary key"
        )
        self.fileName.setText(".csv")
        self.layout.addRow("File name", self.fileName)

    def add_button(self, inputBox):
        downloadButton = QtWidgets.QPushButton("Add job", self)

        downloadButton.setSizePolicy(
            QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
            )
        )
        downloadButton.setToolTip("Add a scraping job to the job queue")
        self.layout.addWidget(downloadButton)

        downloadButton.clicked.connect(inputBox.construct_job)

    def add_options(self, inputBox):
        appendBox = QtWidgets.QCheckBox("Append to existing file")
        appendBox.clicked.connect(inputBox.set_append)
        self.layout.addWidget(appendBox)

        keyBox = QtWidgets.QCheckBox("Add primary key column")
        keyBox.clicked.connect(inputBox.set_key_column)
        self.layout.addWidget(keyBox)

    def get_path(self):
        dir = self.pathWidget.get_path()
        file = self.fileName.text()
        return dir + sep + file

    def set_path(self, text):
        self.fileName.setText(text + ".csv")


class NodePageInputBox(NodePageBox):
    add_iterator = QtCore.pyqtSignal(list)

    def __init__(self, sourceName, queue, queueTable, keys, functionName):
        super().__init__("Input", layout=QtWidgets.QFormLayout)

        self.queue = queue
        self.queueTable = queueTable

        self.queue.queue_update.connect(self.queueTable.display_jobs)
        self.queue.queue_selected.connect(self.queueTable.select_jobs)
        # self.queue.progress_table.connect(self.progressTable.display_value)

        self.keys = keys
        self.primary = []

        self.downloadBox = None

        self.sourceName = sourceName
        self.functionName = functionName

        self.inputs = []
        self.required = []

        self.append = False
        self.keyColumn = None

    def add_input(self, name, input):
        if isinstance(input, NodeInputPrimary):
            self.primary.append(input)
        self.layout.addRow(name, input)
        self.inputs.append(input)

    def read_values(self):

        primary_keys = (
            list(tup) for tup in zip(*[primary.get_value() for primary in self.primary])
        )

        jobs = []
        for primary_tuple in primary_keys:
            arguments = ", ".join(
                [
                    inputWidget.get_value()
                    for inputWidget in self.inputs[len(self.primary) :]
                ]
            )
            arguments = ", ".join(primary_tuple) + ", " + arguments
            jobs.append(("_".join(primary_tuple).replace('"', ""), arguments))
        return jobs

    def set_append(self, boolean):
        self.append = boolean

    def set_key_column(self, boolean):
        self.keyColumn = boolean

    def construct_job(self):
        filePathKey = self.path_function()

        details = []

        for primary_key, args in self.read_values():
            filePath = filePathKey.replace("{key}", primary_key)

            keys = self.keys.get_keys(self.sourceName)
            keyColumnValue = primary_key if self.keyColumn else None
            details.append(
                (
                    filePath,
                    self.sourceName,
                    self.functionName,
                    args,
                    keys,
                    self.append,
                    keyColumnValue,
                )
            )

        self.add_iterator.emit(details)

    def add_required(self, input):
        self.required.append(False)
        required_i = len(self.required) - 1

        input.containsValue.connect(
            lambda bool: self.required_changed(required_i, bool)
        )

    def required_changed(self, i, bool):
        if i < len(self.required):
            self.required[i] = bool

        for req in self.required:
            if not req:
                self.downloadBox.setEnabled(False)
                return

        self.downloadBox.setEnabled(True)


class SourceTab(QtWidgets.QTabWidget):

    def __init__(self, mainTabs):
        super().__init__(mainTabs)
        self.mainWindow = mainTabs.mainWindow
        self.keyTab = mainTabs.keyTab
        self.primaryInputWindow = mainTabs.primaryInputWindow
        self.sourceFile = "sources.xml"

        self.sources = self.read_sources()
        self.add_sources()

    @staticmethod
    def tree_click(item, column_no):
        item.sourceDescription.setCurrentIndex(item.pageIndex)

    def read_sources(self):
        tree = ET.parse(f"{BUNDLE_DIR}{sep}{self.sourceFile}")
        sources_root = tree.getroot()
        source_files = sources_root.findall("source")

        sources = []

        for source_file in source_files:
            location = source_file.find("location").text

            source_tree = ET.parse(
                f"{BUNDLE_DIR}{sep}sources/{location}"
            )
            source_root = source_tree.getroot()
            sources.append(source_root)

        return sources

    def add_sources(self):
        for source in self.sources:
            sourcePage, sourceName = self.create_source_page(source)

            self.create_source_keys(sourceName, source)

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
        sourceName = source.find("name").text
        self.addTab(sourcePage, sourceName)
        sourcePage.layout = QtWidgets.QHBoxLayout()
        sourcePage.setLayout(sourcePage.layout)

        return sourcePage, sourceName

    def create_source_keys(self, sourceName, source):
        keys = source.find("keys")
        key_list = [
            (key.find("name").text, key.find("value").text)
            for key in keys.findall("key")
        ]

        self.keyTab.add_source(sourceName, key_list)

    def create_nodes(
        self,
        sourceName,
        parentNode,
        treeWidget,
        nodeStack,
        treeParentItem=None,
        textDescription="",
    ):

        nodes = parentNode.find("children")
        for node in nodes.findall("node"):
            # Create tree node
            treeItem = treeWidget.add_item(node, treeParentItem)
            self.create_nodes(
                sourceName, node, treeWidget, nodeStack, treeItem, textDescription
            )

    @staticmethod
    def get_node_info(node):
        name = node.find("name").text
        functionName = node.find("function").text
        inputs = node.find("inputs")

        return name, functionName, inputs

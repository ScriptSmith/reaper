import xml.etree.ElementTree as ET
import sys

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


class ArgTable(QtWidgets.QTableWidget):
    def __init__(self, rows=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        super().__init__(0, 2)

        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
        self.setHorizontalHeaderLabels(['Argument', 'Value'])

        self.arguments = {}

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


def tree_handler(item, column_no):
    item.sourceDescription.setCurrentIndex(item.pageIndex)


def table_add_item(text, parent, row, col):
    newItem = QtWidgets.QTableWidgetItem(text)
    newItem.parent = parent
    parent.setItem(row, col, newItem)


def table_cell_changed(item):
    parent = item.parent
    parent.itemChanged.disconnect(table_cell_changed)

    itemRow = item.row()
    parentRowCount = parent.rowCount()
    parentColCount = parent.columnCount()

    # Add new empty row
    if itemRow == parentRowCount - 1:
        parent.setRowCount(parentRowCount + 1)
        parentRowCount = parent.rowCount()
        for col_c in range(parentColCount):
            table_add_item("", parent, parentRowCount - 1, col_c)

    # Remove empty rows
    if item.text() == "":
        for col_c in range(parentColCount):
            if parent.item(itemRow, col_c).text() != "":
                break
        else:
            parent.removeRow(itemRow)

    parent.itemChanged.connect(table_cell_changed)


def build(window):
    # Get sources from XML
    tree = ET.parse('sources.xml')
    sources = tree.getroot()
    sources = sources.findall('source')

    for source in sources:
        # Add tab
        sourcePage = QtWidgets.QWidget()
        sourceName = source.find('name').text
        window.sourcesTabs.addTab(sourcePage, sourceName)
        sourcePage.layout = QtWidgets.QHBoxLayout()
        sourcePage.setLayout(sourcePage.layout)

        # Add tree to tab
        sourceTree = QtWidgets.QTreeWidget()
        sourceTree.setHeaderLabel("Nodes")
        sourcePage.layout.addWidget(sourceTree)

        # Add signals to tree
        sourceTree.itemClicked.connect(tree_handler)

        # Add description to tab
        sourceDescription = QtWidgets.QStackedWidget()
        sourcePage.layout.addWidget(sourceDescription)

        # Define global pageIndex counter that maps tree items to stack indexes
        global pageIndex
        pageIndex = 0

        # Add source nodes to sourceTree and sourceDescription
        add_nodes(sourceName, source, sourceTree, sourceDescription)
        top_item = sourceTree.topLevelItem(0)
        if top_item:
            top_item.setSelected(True)


def add_nodes(sourceName, parentNode, treeWidget, sourceDescription, textDescription="", level=0):
    global pageIndex
    level += 1

    # Find child nodes
    nodes = parentNode.find('children')

    for node in nodes.findall('node'):
        # Define node information
        name = node.find('name').text
        functionName = node.find('function').text
        inputs = node.find('inputs')

        # Add item to tree
        treeItem = QtWidgets.QTreeWidgetItem(treeWidget)
        treeItem.sourceDescription = sourceDescription
        treeItem.setText(0, name)
        treeItem.setExpanded(True)

        # Assign treeItem a pageIndex
        treeItem.pageIndex = pageIndex
        pageIndex += 1

        # Add treeItem to tree hierarchy
        if type(treeWidget) == QtWidgets.QTreeWidget:
            treeWidget.addTopLevelItem(treeItem)
        else:
            treeWidget.addChild(treeItem)

        # Create description stack page
        pageStack = QtWidgets.QWidget()
        pageStack.layout = QtWidgets.QVBoxLayout()
        pageStack.layout.setContentsMargins(0, 0, 0, 0)
        pageStack.setLayout(pageStack.layout)

        # Create a scroll area
        pageScroll = QtWidgets.QScrollArea()
        pageScroll.setWidgetResizable(True)
        pageScroll.setBackgroundRole(QtGui.QPalette.Light)

        # Create a widget that scrolls
        pageDescription = QtWidgets.QWidget(pageStack)
        pageDescription.layout = QtWidgets.QFormLayout()
        pageDescription.setLayout(pageDescription.layout)
        pageStack.layout.addWidget(pageDescription)
        pageStack.layout.addWidget(pageScroll)

        # Create text description box
        textBox = QtWidgets.QGroupBox("Text description")
        textBox.layout = QtWidgets.QFormLayout()
        textBox.setLayout(textBox.layout)

        # Create the description text and title
        if level == 1:
            treeItem.hierarchy = name
            textDescription = name
        else:
            treeItem.hierarchy = treeWidget.hierarchy + " → " + name
            modifier = "'s" if textDescription[-1] != 's' else "'"
            textDescription = "{}{} {}".format(textDescription, modifier, name)
        textContent = "I want to scrape a {} {}".format(sourceName, textDescription)

        # Add title
        title = QtWidgets.QLabel(treeItem.hierarchy)
        title.setStyleSheet("font-weight: bold;")
        pageDescription.layout.addWidget(title)

        # Add text to layout
        textContentLabel = QtWidgets.QLabel(textContent)
        textContentLabel.setWordWrap(True)
        textContentLabel.setStyleSheet("font-style: italic;")
        textBox.layout.addWidget(textContentLabel)
        pageDescription.layout.addWidget(textBox)

        # Create socialreaper box
        srFunction = QtWidgets.QGroupBox("Social Reaper function")
        srFunction.layout = QtWidgets.QFormLayout()
        srFunction.setLayout(srFunction.layout)
        srFunctionText = "{}().{}()".format(sourceName, functionName)
        srFunction.layout.addWidget(QtWidgets.QLabel(srFunctionText))
        pageDescription.layout.addWidget(srFunction)

        # Add inputs
        inputBox = QtWidgets.QGroupBox("Input")
        inputBox.layout = QtWidgets.QFormLayout()
        inputBox.setLayout(inputBox.layout)

        advancedBox = AdvancedBox()
        inputBox.layout.addRow("Show all", advancedBox)

        for input in inputs.findall('input'):
            inputName = input.find('name').text
            inputType = input.find('type').text
            inputRequired = input.attrib.get('required')

            rowContent = None

            if inputType == "text":
                rowContent = QtWidgets.QLineEdit(inputBox)
            elif inputType == "list":
                listBox = QtWidgets.QListWidget(inputBox)
                listBox.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                listBox.setToolTip("Ctrl + Click to deselect list items")
                for elem in input.find('elems'):
                    listItem = QtWidgets.QListWidgetItem(elem.text, listBox)
                    listBox.addItem(listItem)
                rowContent = listBox
            elif inputType == "arguments":
                rows = input.find('rows')

                tableBox = ArgTable(rows)

                setters = input.find('setters')
                if setters:
                    for setter in setters:
                        setterName = setter.find('name').text
                        setterType = setter.find('type').text
                        setterValue = setter.find('value').text

                        if setterType == "counter":
                            setCounter = CounterSetter(int(setterValue), tableBox, "count")
                            inputBox.layout.addRow(setterName, setCounter)

                rowContent = tableBox

            rowContent.required = True if inputRequired else False
            rowContent.setVisible(rowContent.required)
            rowLabel = QtWidgets.QLabel(inputName)
            rowLabel.setVisible(rowContent.required)
            inputBox.layout.addRow(rowLabel, rowContent)

            if not rowContent.required:
                advancedBox.addRow(rowLabel, rowContent)

        pageDescription.layout.addWidget(inputBox)

        # Add download box
        downloadBox = QtWidgets.QGroupBox("Download")
        downloadBox.layout = QtWidgets.QFormLayout()
        downloadBox.setLayout(downloadBox.layout)
        downloadButton = QtWidgets.QPushButton("Add job", downloadBox)
        downloadButton.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        downloadButton.setToolTip("Add a scraping job to the job queue")
        downloadBox.layout.addRow(downloadButton)
        pageDescription.layout.addWidget(downloadBox)

        # Add description to pages
        pageScroll.setWidget(pageDescription)
        sourceDescription.addWidget(pageStack)
        sourceDescription.setCurrentIndex(0)

        # Recurse through children
        add_nodes(sourceName, node, treeItem, sourceDescription, textDescription, level)

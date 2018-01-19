import xml.etree.ElementTree as ET

from PyQt5 import QtCore, QtGui, QtWidgets

from socialreaper import Facebook


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

    # Remove empty second last row
    elif itemRow == parentRowCount - 2:
        searchRow = parentRowCount - 2
        for col_c in range(parentColCount):
            if parent.item(searchRow, col_c).text() != "":
                break
        else:
            parent.setRowCount(parentRowCount - 1)

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
        sourceDescription.layout = QtWidgets.QVBoxLayout()
        sourceDescription.setLayout(sourceDescription.layout)
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

        # Assign treeItem a pageIndex
        treeItem.pageIndex = pageIndex
        pageIndex += 1

        # Add treeItem to tree hierarchy
        if type(treeWidget) == QtWidgets.QTreeWidget:
            treeWidget.addTopLevelItem(treeItem)
        else:
            treeWidget.addChild(treeItem)

        # Create description stack page
        pageStack = QtWidgets.QWidget(sourceDescription)
        pageStack.layout = QtWidgets.QVBoxLayout()
        pageStack.layout.setContentsMargins(0, 0, 0, 0)
        pageStack.setLayout(pageStack.layout)

        # Create a scroll area
        pageScroll = QtWidgets.QScrollArea(sourceDescription)
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

        for input in inputs.findall('input'):
            inputName = input.find('name').text
            inputType = input.find('type').text

            if inputType == "text":
                textBox = QtWidgets.QLineEdit(inputBox)
                inputBox.layout.addRow(inputName, textBox)
            elif inputType == "list":
                listBox = QtWidgets.QListWidget(inputBox)
                listBox.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                listBox.setToolTip("Ctrl + Click to deselect list items")
                for elem in input.find('elems'):
                    listItem = QtWidgets.QListWidgetItem(elem.text, listBox)
                    listBox.addItem(listItem)
                inputBox.layout.addRow(inputName, listBox)
            elif inputType == "table":
                columns = input.find('columns')
                rows = input.find('rows')

                tableBox = QtWidgets.QTableWidget(len(rows) + 1, len(columns), inputBox)
                tableBox.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                tableBox.verticalHeader().setVisible(False)
                tableBox.setHorizontalHeaderLabels([column.text for column in columns])

                row_c = 0
                for row_c, row in enumerate(rows):
                    for cell_c, cell in enumerate(row):
                        table_add_item(cell.text, tableBox, row_c, cell_c)

                for cell_c in range(len(columns)):
                    table_add_item("", tableBox, row_c + 1, cell_c)

                tableBox.itemChanged.connect(table_cell_changed)

                inputBox.layout.addRow(inputName, tableBox)


            print(input.find('name').text)
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

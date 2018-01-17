import xml.etree.ElementTree as ET

from PyQt5 import QtCore, QtGui, QtWidgets


def tree_handler(item, column_no):
    item.sourceDescription.setCurrentIndex(item.pageIndex)


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
        text = QtWidgets.QGroupBox()
        text.setTitle("Text description")
        text.layout = QtWidgets.QFormLayout()
        text.setLayout(text.layout)

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
        text.layout.addWidget(QtWidgets.QLabel(textContent))
        pageDescription.layout.addWidget(text)

        # Create socialreaper box
        srFunction = QtWidgets.QGroupBox()
        srFunction.setTitle("Social Reaper function")
        srFunction.layout = QtWidgets.QFormLayout()
        srFunction.setLayout(srFunction.layout)
        srFunctionText = "{}().{}()".format(sourceName, functionName)
        srFunction.layout.addWidget(QtWidgets.QLabel(srFunctionText))
        pageDescription.layout.addWidget(srFunction)

        # Add description to pages
        pageScroll.setWidget(pageDescription)
        sourceDescription.addWidget(pageStack)
        sourceDescription.setCurrentIndex(0)

        # Recurse through children
        add_nodes(sourceName, node, treeItem, sourceDescription, textDescription, level)

import xml.etree.ElementTree as ET

from PyQt5 import QtCore, QtGui, QtWidgets

def tree_handler(item, column_no):
    # items = item.tree.findItems(None, QtCore.Qt.MatchRecursive, QtCore.Qt.MatchWildcard)
    item.sourceDescription.setCurrentIndex(item.pageIndex)
    print(f"{item} {item.pageIndex}")


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

        # Create small scroll
        # scrollArea = QtWidgets.QScrollArea()
        # scrollArea.setWidgetResizable(True)
        # scrollWidget = QtWidgets.QWidget()
        # scrollWidget.layout = QtWidgets.QVBoxLayout()
        # scrollWidget.setLayout(scrollWidget.layout)
        # for _ in range(15):
        #     scrollWidget.layout.addWidget(QtWidgets.QPushButton("Hi"))

        # scrollArea.setWidget(scrollWidget)
        # sourceDescription.layout.addWidget(scrollWidget)

        global pageIndex
        pageIndex = 0
        add_nodes(sourceName, source, sourceTree, sourceDescription)
        sourceTree.topLevelItem(0).setSelected(True)
        print(pageIndex)


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

        treeItem.parent = treeWidget
        treeItem.pageIndex = pageIndex
        pageIndex += 1
        if type(treeWidget) == QtWidgets.QTreeWidget:
            treeWidget.addTopLevelItem(treeItem)
        else:
            treeWidget.addChild(treeItem)

        # Create page description
        pageStack = QtWidgets.QWidget(sourceDescription)
        pageStack.layout = QtWidgets.QVBoxLayout()
        pageStack.setLayout(pageStack.layout)

        # Add title
        # title = QtWidgets.QLabel(name)
        # title.setStyleSheet("font-weight: bold;")
        # pageStack.layout.addWidget(title)


        pageScroll = QtWidgets.QScrollArea(sourceDescription)
        pageScroll.setWidgetResizable(True)
        pageScroll.setBackgroundRole(QtGui.QPalette.Light)
        # pageStack.setMinimumWidth(100)


        pageDescription = QtWidgets.QWidget(pageStack)
        pageDescription.layout = QtWidgets.QVBoxLayout()
        pageDescription.setLayout(pageDescription.layout)
        pageDescription.sizePolicy().setHorizontalPolicy(QtWidgets.QSizePolicy.Minimum)
        # pageDescription.setGeometry(QtCore.QRect(0, 0, 484, 461))
        # pageDescription.sizePolicy().setHorizontalPolicy(QtWidgets.QSizePolicy.Maximum)
        # pageStack.setFixedWidth(400)
        # pageScroll.setMinimumSize(400,400)
        # pageDescription.setFixedWidth(400)
        # sourceDescription.setFixedWidth(400)
        pageStack.layout.addWidget(pageDescription)
        pageStack.layout.addWidget(pageScroll)

        # for _ in range(10):
        #     pageDescription.layout.addWidget(QtWidgets.QLabel("hello"))

        # pageScroll.setHorizontalScrollPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Create text description box
        text = QtWidgets.QGroupBox()
        text.setTitle("Text description")
        text.layout = QtWidgets.QFormLayout()
        text.setLayout(text.layout)

        # Create the text
        if level == 1:
            textDescription = name
        else:
            modifier = "'s" if textDescription[-1] != 's' else "'"
            textDescription = "{}{} {}".format(textDescription, modifier, name)
        textContent = "I want to scrape a {}".format(textDescription)

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
        print(sourceDescription.count())

        # Recurse through children
        add_nodes(sourceName, node, treeItem, sourceDescription, textDescription, level)


class SourceInput(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SourceInput, self).__init__(parent)

        self.pushButton = QtWidgets.QPushButton('Hello')
        self.pushButton2 = QtWidgets.QPushButton('Hello2')

        self.the_layout = QtWidgets.QGridLayout()
        self.the_layout.addWidget(self.pushButton)
        self.the_layout.addWidget(self.pushButton2)
        self.setLayout(self.the_layout)

import csv
import json
from collections import OrderedDict
from os import getcwd, path

from PyQt5 import QtWidgets, QtCore, QtGui


class PrimaryInputWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(PrimaryInputWindow, self).__init__(parent)

        self.csvInput = True
        self.filePath = ""

        self.setup_ui()
        # self.setFixedSize(300, 300)

    def setup_ui(self):
        self.setWindowTitle("Read from file")

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.layout = QtWidgets.QHBoxLayout()
        self.centralWidget.setLayout(self.centralWidget.layout)
        self.setCentralWidget(self.centralWidget)

        # Add radio boxes
        self.radioBox = QtWidgets.QWidget()
        self.radioLayout = QtWidgets.QVBoxLayout()
        self.radioBox.layout = self.radioLayout
        self.radioBox.setLayout(self.radioBox.layout)

        self.radioCSV = QtWidgets.QRadioButton("Read CSV")
        self.radioCSV.setChecked(self.csvInput)
        self.radioCSV.toggled.connect(self.set_mode)
        self.radioLines = QtWidgets.QRadioButton("Read Text")
        self.radioLayout.addWidget(self.radioCSV)
        self.radioLayout.addWidget(self.radioLines)

        openButton = QtWidgets.QPushButton("Open file")
        openButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        openButton.clicked.connect(self.open_file)
        self.radioBox.layout.addWidget(openButton)

        self.radioLayout.addStretch(1)

        self.centralWidget.layout.addWidget(self.radioBox)

        # Add OK button
        self.okButton = QtWidgets.QPushButton("OK")
        self.okButton.clicked.connect(self.return_data)
        self.radioBox.layout.addWidget(self.okButton)

        # Add input widget
        inputWidget = QtWidgets.QWidget()
        inputWidget.layout = QtWidgets.QFormLayout()
        inputWidget.setLayout(inputWidget.layout)

        self.filePathLabel = QtWidgets.QLabel()
        self.filePathLabel.setVisible(False)
        self.filePathLabel.setStyleSheet("font-style: italic;")
        inputWidget.layout.addRow(self.filePathLabel)

        self.columnName = QtWidgets.QLineEdit()
        self.columnName.setPlaceholderText("Column name")

        self.extractButton = QtWidgets.QPushButton("Read")
        self.extractButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.extractButton.clicked.connect(self.extract_file)
        inputWidget.layout.addRow(self.columnName, self.extractButton)

        self.listWidget = QtWidgets.QListWidget()
        inputWidget.layout.addRow(self.listWidget)
        self.listWidget.setSelectionMode(self.listWidget.NoSelection)

        self.centralWidget.layout.addWidget(inputWidget)

    def open_file(self, _):
        print("opening file")
        options = QtWidgets.QFileDialog.Options()

        title = "Open file"
        directory = ""
        filter = "CSV Files (*.csv);;" if self.csvInput else ""
        filter += "All Files (*)"

        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(caption=title, directory=directory, filter=filter,
                                                            options=options)
        if filePath:
            self.filePath = filePath
            self.filePathLabel.setVisible(True)
            self.filePathLabel.setText(self.filePath)

            if not self.csvInput:
                self.extract_file()

    def set_mode(self, bool):
        self.csvInput = bool

        self.listWidget.clear()
        self.filePathLabel.setText("")
        self.extractButton.setVisible(bool)
        self.columnName.setVisible(bool)

    def extract_file(self):
        if not self.filePath:
            return

        self.listWidget.clear()

        if self.csvInput:
            self.extract_csv()
        else:
            self.extract_lines()

    def extract_csv(self):
        with open(self.filePath, 'r', encoding='utf8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                datum = row.get(self.columnName.text())
                if datum:
                    self.listWidget.addItem(str(datum))

    def extract_lines(self):
        with open(self.filePath, 'r', encoding='utf8') as f:
            lines = f.readlines()

            for line in lines:
                self.listWidget.addItem(line.strip())

    def return_data(self):
        data = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
        self.read_file(data)
        self.hide()


class NodeInputWidget():
    containsValue = QtCore.pyqtSignal(bool)

    def __init__(self, required=True):
        self.required = required
        self.setVisible(self.required)

    def get_value(self):
        pass


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
        return f"**{json.dumps(self.arguments)}"


class NodeInputLine(QtWidgets.QLineEdit, NodeInputWidget):
    def __init__(self, required=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        NodeInputWidget.__init__(self, required=required)

        self.textChanged.connect(self.value_changed)

    def get_value(self):
        return json.dumps(self.text())

    def value_changed(self, text):
        if text:
            self.containsValue.emit(True)
        else:
            self.containsValue.emit(False)


class NodeInputPrimary(NodeInputLine):
    fileText = QtCore.pyqtSignal(str)

    def __init__(self, window, parent=None):
        NodeInputLine.__init__(self, required=True, parent=parent)

        self.window = window

        self.readingText = "Reading from file"
        self.data = []

        self.readAction = self.addAction(QtGui.QIcon('ui/read.png'), self.TrailingPosition)
        self.readAction.triggered.connect(self.add_file)

        self.clearAction = self.addAction(QtGui.QIcon('ui/remove.png'), self.TrailingPosition)
        self.clearAction.triggered.connect(self.clear_file)
        self.clearAction.setVisible(False)

        self.textChanged.connect(self.updateText)

    def add_file(self, _):
        self.window.read_file = self.read_file
        self.window.show()

    def clear_file(self, _):
        self.readAction.setVisible(True)
        self.clearAction.setVisible(False)
        self.setReadOnly(False)
        self.setText("")
        self.setStyleSheet("")
        self.data.clear()

    def read_file(self, data):
        self.readAction.setVisible(False)
        self.clearAction.setVisible(True)
        self.setReadOnly(True)
        self.setText(self.readingText)
        self.setStyleSheet("background-color: #d0d4db")
        self.data = data

    def get_value(self):
        if len(self.data) > 0:
            return [json.dumps(datum) for datum in self.data]
        else:
            return [json.dumps(self.text())]

    def updateText(self, text):
        if text == self.readingText:
            self.fileText.emit("{key}")
        else:
            self.fileText.emit(text)


class NodeInputList(QtWidgets.QListWidget, NodeInputWidget):
    def __init__(self, required=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        NodeInputWidget.__init__(self, required=required)

        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setToolTip("Ctrl + Click to deselect list items")

    def add_elements(self, elements):
        if elements:
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


class CheckboxSetter(QtWidgets.QCheckBox):
    def __init__(self, value, table, argument, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.table = table
        self.argument = argument
        self.toggled.connect(self.set_arg)
        self.setEnabled(value)

    def set_arg(self, value):
        self.table.set_argument(self.argument, str(value))
        self.table.fill_table()


class ListSetter(QtWidgets.QListWidget):
    def __init__(self, values, table, argument, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.values = values
        self.table = table
        self.argument = argument
        self.currentRowChanged.connect(self.set_arg)

        self.fill_values()
        self.setMaximumHeight(self.sizeHintForRow(0) * len(self.values) + 5)

    def fill_values(self):
        for value in self.values:
            self.addItem(value)
        # self.setCurrentRow(0)

    def set_arg(self, row):
        self.table.set_argument(self.argument, self.item(row).text())
        self.table.fill_table()


class AdvancedBox(QtWidgets.QCheckBox):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.child_items = []

        self.toggled.connect(self.changeVisibility)

    def addRow(self, label, widget):
        self.child_items.append(label)
        self.child_items.append(widget)

    def changeVisibility(self, state):
        for item in self.child_items:
            item.setVisible(state)


class PathWidget(QtWidgets.QWidget):
    path_changed = QtCore.pyqtSignal(str)

    def __init__(self, save_path=None, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.dirPath = QtWidgets.QLabel(save_path if save_path else getcwd())
        self.layout.addWidget(self.dirPath)

        self.layout.addStretch(1)

        self.pathButton = QtWidgets.QPushButton("Choose folder")
        self.layout.addWidget(self.pathButton)
        self.pathButton.clicked.connect(self.open_dir)

    def open_dir(self, _):
        options = QtWidgets.QFileDialog.Options()

        title = "Open folder"
        directory = ""

        dirPath = QtWidgets.QFileDialog.getExistingDirectory(caption=title, directory=directory, options=options)
        if dirPath:
            dirPath = path.abspath(dirPath)
            self.dirPath.setText(dirPath)
            self.path_changed.emit(dirPath)

    def get_path(self):
        return self.dirPath.text()

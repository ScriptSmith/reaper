from PyQt5 import QtWidgets

from collections import OrderedDict
import json


class NodeInputWidget():
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

    def get_value(self):
        return json.dumps(self.text())


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
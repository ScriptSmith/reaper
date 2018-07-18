import json
from os import sep, makedirs, path

from components.globals import DATA_DIR

from PyQt5 import QtWidgets


class KeyLine(QtWidgets.QLineEdit):

    def __init__(self, name, key, sources, save):
        super().__init__()

        self.key = key
        self.name = name
        self.sources = sources
        self.save = save

        self.setText(sources[name][key])

        self.textChanged.connect(self.edit_key)

    def edit_key(self, text):
        self.sources[self.name][self.key] = text.rstrip()
        if text:
            self.save()


class KeyTab(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)

        self.scrollWidget = QtWidgets.QWidget(self.scrollArea)
        self.scrollWidget.layout = QtWidgets.QVBoxLayout()
        self.scrollWidget.setLayout(self.scrollWidget.layout)
        self.layout.addWidget(self.scrollWidget)
        self.layout.addWidget(self.scrollArea)

        self.location = f"{DATA_DIR}{sep}keys.json"

        if not path.exists(DATA_DIR):
            makedirs(DATA_DIR)

        self.sources = {}
        self.read_keys()

    def read_keys(self):
        try:
            with open(self.location, "r") as f:
                data = json.load(f)
                self.sources = data
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def write_keys(self):
        with open(self.location, "w") as f:
            json.dump(self.sources, f)

    def add_source(self, name, keys):
        if not self.sources.get(name):
            self.sources[name] = {}
            for key in keys:
                self.sources[name][key[1]] = ""

        sourceBox = QtWidgets.QGroupBox(name)
        sourceBox.layout = QtWidgets.QGridLayout()
        sourceBox.layout.setColumnMinimumWidth(0, 150)
        sourceBox.setLayout(sourceBox.layout)

        for count, key in enumerate(keys):
            keyLine = KeyLine(name, key[1], self.sources, self.write_keys)
            sourceBox.layout.addWidget(QtWidgets.QLabel(key[0]), count, 0)
            sourceBox.layout.addWidget(keyLine, count, 1)

        self.scrollWidget.layout.addWidget(sourceBox)

    def get_keys(self, name):
        keys = self.sources.get(name)
        if keys:
            for key in keys.keys():
                keys[key] = keys[key].strip()
            return keys
        else:
            return None

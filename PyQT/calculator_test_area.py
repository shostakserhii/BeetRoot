import sys

from functools import partial

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QListWidget,
                             QLabel)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Pyculator")
        self.setGeometry(100, 100, 280, 80)
        self.first_value = 0
        self.second_value = 0
        self.operation = ""
        self.widget = QWidget()
        self.mainLayout = QHBoxLayout()
        self.mainSubLayout = QVBoxLayout()
        self._createDisplay()
        self._createButtons()
        self.mainSubLayout.addLayout(self.buttonLayout)
        self.mainLayout.addLayout(self.mainSubLayout)
        self.history = QListWidget()
        self.mainLayout.addWidget(self.history)
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)
        self.buttons_processing()
        self.input_processing()


    def _createDisplay(self):
        self.display = QLineEdit('')
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.mainSubLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        self.buttonLayout = QGridLayout()
        buttons = [
            {
                'name':'C',
                'row':0,
                'col':4
            },
            {
                'name':'%',
                'row':2,
                'col':4,
            },
            {
                'name':'=',
                'row':3,
                'col':4,
            },
            {
                'name':'←',
                'row':1,
                'col':4
            },
            {
                'name':'1',
                'row':0,
                'col':0
            },
            {
                'name':'2',
                'row':0,
                'col':1
            },
            {
                'name':'3',
                'row':0,
                'col':2
            },
            {
                'name':'4',
                'row':1,
                'col':0
            },
            {
                'name':'5',
                'row':1,
                'col':1
            },
            {
                'name':'6',
                'row':1,
                'col':2
            },
            {
                'name':'7',
                'row':2,
                'col':0
            },
            {
                'name':'8',
                'row':2,
                'col':1
            },
            {
                'name':'9',
                'row':2,
                'col':2
            },
            {
                'name':'0',
                'row':3,
                'col':0,
                'colSpan': 2
            },
            {
                'name':'.',
                'row':3,
                'col':2
            },
            {
                'name':'+',
                'row':0,
                'col':3
            },
            {
                'name':'-',
                'row':1,
                'col':3
            },
            {
                'name':'*',
                'row':2,
                'col':3
            },
            {
                'name':'/',
                'row':3,
                'col':3
            },
        ]

        for buttonConfig in buttons:
            name = buttonConfig.get('name','')
            btn = QPushButton(name)
            self.buttons[name] = btn
            self.buttonLayout.addWidget(btn,
                                   buttonConfig['row'],
                                   buttonConfig['col'],
                                   buttonConfig.get('rowSpan',1),
                                   buttonConfig.get('colSpan',1))

        
    def change_text(self, text):
        self.display.setText(self.display.text() + text)

    def input_value_processing(self):
        pass

    def buttons_processing(self):
        for button_name in self.buttons:
            btn = self.buttons[button_name]
            if button_name in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                btn.clicked.connect(partial(self.change_text, button_name))
            elif button_name == 'C':
                btn.clicked.connect(self._clearDisplay)
            elif button_name == '←':
                btn.clicked.connect(self._remove)
            elif button_name == '+':
                btn.clicked.connect(self._additing)

    def input_processing(self):
        value = self.displayText()
        print(f"value is {value}")
        print(f"first_value is {self.first_value}")
        # if self.operation == '':
        #     pass
        if self.first_value == 0:
            self.first_value = value
            print(f"first_value is {self.first_value}")
        else:
            self.second_value = value
            print(f"second_value is {self.second_value}")
        print(f"operation {self.operation}")

        
        

    def setDisplayText(self, text):
        self.display.setText('')
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def _clearDisplay(self):
        self.setDisplayText('')
    
    def _remove(self):
        value = self.displayText()
        if len(value) == 0:
            self.setDisplayText("")
        else:
            value = value[:-1]
            self.display.setText(value)
    
    def _additing(self):
        self.operation = '+'
        self.input_processing()
       


def main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    

if __name__ == "__main__":
    main_window()    
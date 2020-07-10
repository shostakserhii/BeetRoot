import sys

from functools import partial
from operator import pow, truediv, mul, add, sub 
from PyQt5.QtGui import QFont, QColor
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
                             QLabel,
                             QSizePolicy)



class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Pyculator")
        self.setGeometry(100, 100, 280, 80)
        self.first_value = ''
        self.second_value = ''
        self.operation = ''
        self.result = ''
        self.dot = 0
        self.operations = {
                           '+':add,
                           '-':sub,
                           '*':mul
                           }
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
            font = QFont()
            font.setBold(True)
            btn.setFont(font)
            btn.setSizePolicy(QSizePolicy.Preferred, 
                              QSizePolicy.Expanding)
            self.buttons[name] = btn
            self.buttonLayout.addWidget(btn,
                                   buttonConfig['row'],
                                   buttonConfig['col'],
                                   buttonConfig.get('rowSpan',1),
                                   buttonConfig.get('colSpan',1))


    def change_text(self, text):
        self.display.setText(self.display.text() + text)

    def buttons_processing(self):
        for button_name in self.buttons:
            btn = self.buttons[button_name]
            if button_name in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                btn.clicked.connect(partial(self.change_text, button_name))
            elif button_name == 'C':
                btn.clicked.connect(self._clearAll)
            elif button_name == '←':
                btn.clicked.connect(self._remove)
            elif button_name == '+':
                btn.clicked.connect(self._additing)
            elif button_name == '=':
                btn.clicked.connect(self._ending)
            elif button_name == '-':
                btn.clicked.connect(self._substracting)
            elif button_name == '*':
                btn.clicked.connect(self._multiplication)
            elif button_name == '.':
                btn.clicked.connect(self._dotting)                

    def _dotting(self):
        value = self.displayText()
        if '.' in value:
            return
        else:
            self.display.setText(self.display.text() + ".")

    def int_or_float(self, num):
        try:
            num = float(num)
            if num.is_integer():
                return int(num)
            return num
        except ValueError:
            self._clearAll
            self.history.addItem("ERROR")
            return

    def input_processing(self):
        value = self.displayText()

        if value == '':
            return True

        print(f"value is {value}")
        print(f"first_value is {self.first_value}")
        print(f"operation is {self.operation}")
        print(f"second_value is {self.second_value}")
        if self.first_value != '' and value == '':
            return

        if self.first_value == '':
            self.first_value = value
            print(f"1st IF first_value is {self.first_value}")
            self.history.addItem(self.displayText())
            self.history.addItem(self.operation)
            self._clearDisplay()
            return

        elif self.first_value != '':
            if self.second_value == '':
                self.second_value = value
                self.history.addItem(self.displayText())
                self._clearDisplay()
                print(f"ELIF first_value is {self.first_value}")
                print(f"ELIF oeration is {self.operation}")
                print(f"ELIF second_value is {self.second_value}")
                return
            elif self.second_value != '' and self.second_value != '':     
                self.second_value = value
                self.history.addItem(self.displayText())
                self._clearDisplay()
                print(f"ELSE elif second_value is {self.second_value}")
                print(f"ELSE first_value is {self.first_value}")
                print(f"ELSE oeration is {self.operation}")
                print(f"ELSE second_value is {self.second_value}")
                return

    def setDisplayText(self, text=''):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def _clearDisplay(self):
        self.setDisplayText()

    def _clearAll(self):
        self.setDisplayText()
        self.first_value = ''
        self.second_value = ''
        self.result = ''
        self.history.clear()

    def validate(self, value):
        if value.lstrip("-").replace('.','',1).isdigit() and value.count("-") <= 1:
            return True

    def _remove(self):
        value = self.displayText()

        if len(value) == 0:
            self.setDisplayText("")
        else:
            value = value[:-1]
            self.display.setText(value)

    def _ending(self):
        self.input_processing()

        if self.second_value == '' and self.operation != '':
            print('U are in ending now')
            self.repeat = self.first_value
            self.result = self.operations[self.operation](self.int_or_float(self.first_value), self.int_or_float(self.repeat))
            self.result = ''
            self.setDisplayText(str(self.first_value))
            return

        for symbol in self.operations:
            if symbol == self.operation:
                print(f"first value = {self.first_value}, second value = {self.second_value}")
                self.result = self.operations[self.operation](self.int_or_float(self.first_value), self.int_or_float(self.second_value))

        self.history.addItem('=')
        self.history.addItem(str(self.int_or_float(self.result)))
        self.first_value = self.result
        self.result = ''
        self.second_value = ''
        # self.operation = ''
        self.history.clear()
        self.setDisplayText(str(self.first_value))
        print(f"""after ending first value is {self.first_value}
                                second value is {self.second_value}
                                result is {self.result}
        """)
        self.first_value = ''

    def _additing(self):
        self.operation = '+'
        
        if self.first_value == '':
            self.input_processing()
            return
        elif self.first_value != '':    
            if self.input_processing() is True:
                self.history.addItem(self.operation)
                return
            else:
                print(f"_additintg first value = {self.first_value} \nsecond_value is {self.second_value}")
                left = self.int_or_float(self.first_value)
                print(f"_additing left = {left}")
                right = self.int_or_float(self.second_value)
                print(f"_additing right = {right}")
                self.result = left + right
                self.history.addItem('=')
                self.history.addItem(str(self.result))
                self.history.addItem(self.operation)
                self.first_value = self.result
                return

    def _substracting(self):
        self.operation = '-'

        if self.first_value == '':
            self.input_processing()
            return
        elif self.first_value != '':    
            if self.input_processing() is True:
                self.history.addItem(self.operation)
                return
            else:
                print(f"_additintg first value = {self.first_value} \nsecond_value is {self.second_value}")
                left = self.int_or_float(self.first_value)
                print(f"_additing left = {left}")
                right = self.int_or_float(self.second_value)
                print(f"_additing right = {right}")
                self.result = left - right
                self.history.addItem('=')
                self.history.addItem(str(self.int_or_float(self.result)))
                self.history.addItem(self.operation)
                self.first_value = self.result
                return

    def _multiplication(self):
        self.operation = '*'

        if self.first_value == '':
            self.input_processing()
            return
        elif self.first_value != '':    
            if self.input_processing() is True:
                self.history.addItem(self.operation)
                return
            else:
                print(f"_additintg first value = {self.first_value} \nsecond_value is {self.second_value}")
                left = self.int_or_float(self.first_value)
                print(f"_additing left = {left}")
                right = self.int_or_float(self.second_value)
                print(f"_additing right = {right}")
                self.result = left * right
                self.history.addItem('=')
                self.history.addItem(str(self.int_or_float(self.result)))
                self.history.addItem(self.operation)
                self.first_value = self.result
                return


def main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main_window() 
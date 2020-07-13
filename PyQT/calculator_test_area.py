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
        self.temp1 = ''
        self.temp = ''
        self.temp_operation = ''
        self.number_of_minus = 0
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
        if self.first_value != '' and self.operation == '':
            print("IN CHANGING IF")
            self.first_value = ''
            self.history.clear()
            self.temp = ''
            self.temp1 = ''
            self._clearDisplay()
            self.display.setText(self.display.text()+text)
            return
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
            # elif button_name == '*':
            #     btn.clicked.connect(self._multiplication)
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
            self._clearAll()
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

        if self.first_value == '':
            self.first_value = value
            self.history.addItem(value)
            print(f"1st IF added to hitory self display {self.displayText()}")
            print(f"1st IF added to history operation {self.operation}")
            print(f"1st IF first_value is {self.first_value}")
            self.number_of_minus = 0
            self._clearDisplay()
            return

        # if self.first_value != '' and value == '':
        #     return

        if self.first_value != '':
            if self.second_value == '' and self.operation != '':
                self.second_value = value
                self.history.addItem(self.displayText())
                print(f"IF added to hitory self display {self.displayText()}")
                self._clearDisplay()
                print(f"IF first_value is {self.first_value}")
                print(f"IF oeration is {self.operation}")
                print(f"IF second_value is {self.second_value}")
                self.number_of_minus = 0
                return

    def setDisplayText(self, text=''):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def _clearDisplay(self):
        self.setDisplayText()

    def _clearAll(self):
        self.first_value = ''
        self.second_value = ''
        self.operation = ''
        self.result = ''
        self.temp1 = ''
        self.temp = ''
        self.history.clear()
        self._clearDisplay()
        self.temp_operation = ''
        self.number_of_minus = 0
        self.dot = 0

    def _remove(self):
        value = self.displayText()

        if len(value) == 0:
            self.setDisplayText("")
        else:
            value = value[:-1]
            self.display.setText(value)

    def _ending(self):
        self.input_processing()

        if self.second_value == '' and self.operation == '':
            for symbol in self.operations:
                if symbol == self.temp_operation:
                    print("in ending first IF")
                    self.temp1 = self.first_value
                    self.first_value = self.operations[self.temp_operation](self.int_or_float(self.first_value), self.int_or_float(self.temp))
                    self.setDisplayText(str(self.first_value))
                    self.history.addItem(f"{str(self.temp1)} {self.temp_operation} {str(self.temp)} = {str(self.int_or_float(self.first_value))}")
                    return

        for symbol in self.operations:
            if symbol == self.operation:
                print(f"first value = {self.first_value}, second value = {self.second_value}")
                self.temp1 = self.first_value
                self.first_value = self.operations[self.operation](self.int_or_float(self.first_value), self.int_or_float(self.second_value))
        self.history.clear()
        self.history.addItem(f"{str(self.temp1)} {self.operation} {str(self.second_value)} = {str(self.int_or_float(self.first_value))}")
        self.temp = self.second_value
        self.temp_operation = self.operation
        self.operation = ''
        self.second_value = ''
        self.setDisplayText(str(self.first_value))
        print(f"""after ending first value is {self.first_value}
                                second value is {self.second_value}
                                history is {self.history}
                                operation is {self.operation}
                                self.temp is {self.temp}

        """)


    def _additing(self):
        self.input_processing()
        
        if self.first_value == '':
            return
        
        if self.first_value != '' and self.second_value == '':
            self.operation = '+'
            self.history.addItem('+')
            self._clearDisplay()
            return
        if self.second_value != '':
            print(f"_additintg first value = {self.first_value} \nsecond_value is {self.second_value}")
            self.first_value = self.int_or_float(self.first_value)
            print(f"_additing left = {self.first_value}")
            self.second_value = self.int_or_float(self.second_value)
            print(f"_additing right = {self.second_value}")
            self.temp = self.second_value
            self.temp1 = self.first_value
            self.first_value = self.first_value + self.second_value
            self.second_value = '' 
            return

    def _substracting(self):

        self.input_processing()

        if self.first_value == '':
            self.number_of_minus += 1
            self.setDisplayText('-')

        if self.first_value != '' and self.operation == '':
            self.operation = '-'
            self._clearDisplay()
            self.history.addItem('-')
            self.number_of_minus = 0
            return

        if self.operation != '' and self.number_of_minus == 0:
            self.number_of_minus += 1
            self.setDisplayText('-')
            return

        if self.first_value != '':    
            self.history.addItem(self.operation)
            print(f"History added in subsctraction 1st IF {self.operation}")
            self.number_of_minus = 0
            return

        if self.first_value !='' and self.second_value !='':
            print(f"_additintg first value = {self.first_value} \nsecond_value is {self.second_value}")
            left = self.int_or_float(self.first_value)
            print(f"_additing left = {left}")
            right = self.int_or_float(self.second_value)
            print(f"_additing right = {right}")
            self.temp1 = self.first_value
            self.first_value = left - right
            self.history.addItem('=')
            self.history.addItem(str(self.int_or_float(self.first_value)))
            self.history.addItem(self.operation)
            print(f"History added in subsctraction 1st ELSE {self.operation}")
            return

def main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main_window() 
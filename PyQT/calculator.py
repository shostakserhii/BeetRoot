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
                             QLabel)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Pyculator")
        self.setGeometry(100, 100, 280, 80)
        self.editArea = QLineEdit('')
        self.first_input = ""
        self.second_input = ""
        self.operation = ""
        widget = QWidget()
        helloMsg = QLabel('Hello World!')
        helloMsg.setAlignment(Qt.AlignCenter)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(helloMsg)
        mainLayout.addWidget(self.editArea)

        buttonLayout = QGridLayout()
        buttons = [
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
                'name':'=',
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
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name','')
            btn = QPushButton(name)
            self.buttons[name] = btn
            buttonLayout.addWidget(btn,
                                   buttonConfig['row'],
                                   buttonConfig['col'],
                                   1,
                                   buttonConfig.get('colSpan',1))
        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)


    def data_processing(self):
        for button_name in self.buttons:
            btn = self.buttons[button_name]
            btn.clicked.connect(partial(self.change_text, button_name))

        
    def change_text(self, text):
        self.editArea.setText(self.editArea.text() + text)

def main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    

if __name__ == "__main__":
    main_window()    
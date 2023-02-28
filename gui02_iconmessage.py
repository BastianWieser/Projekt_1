"""
GUI-Calculator
Message Window hinzugefügt
by tobias
26.02.2023
"""

import sys
from PyQt6.QtWidgets import *

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        #window title 
        self.setWindowTitle('Calculator')

        #create display, no writing allowed
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)

        #create buttons
        self.button_0 = QPushButton('0')
        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')
        self.button_add = QPushButton('+')
        self.button_sub = QPushButton('-')
        self.button_mul = QPushButton('*')
        self.button_div = QPushButton('/')
        self.button_empty1 = QPushButton(' ')
        self.button_empty2 = QPushButton(' ')
        self.button_result = QPushButton('=')
        self.button_save = QPushButton('Save')
        self.button_load = QPushButton('Load')
        self.button_quit = QPushButton('Quit')
        self.button_clear = QPushButton('Clear')

        #create button layout, vertical and horizontal
        vbox = QVBoxLayout()
        hbox0 = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        
        hbox0.addWidget(self.button_save)
        hbox0.addWidget(self.button_load)
        hbox0.addWidget(self.button_quit)
        hbox0.addWidget(self.button_clear)

        hbox1.addWidget(self.button_7)
        hbox1.addWidget(self.button_8)
        hbox1.addWidget(self.button_9)
        hbox1.addWidget(self.button_add)

        hbox2.addWidget(self.button_4)
        hbox2.addWidget(self.button_5)
        hbox2.addWidget(self.button_6)
        hbox2.addWidget(self.button_sub)

        hbox3.addWidget(self.button_1)
        hbox3.addWidget(self.button_2)
        hbox3.addWidget(self.button_3)
        hbox3.addWidget(self.button_mul)

        hbox4.addWidget(self.button_empty1)
        hbox4.addWidget(self.button_0)
        hbox4.addWidget(self.button_empty2)
        hbox4.addWidget(self.button_div)

        hbox5.addWidget(self.button_result)

        vbox.addWidget(self.result_display)
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)
        
        #connect buttons
        self.button_0.clicked.connect(lambda: self.show_display('0'))
        self.button_1.clicked.connect(lambda: self.show_display('1'))
        self.button_2.clicked.connect(lambda: self.show_display('2'))
        self.button_3.clicked.connect(lambda: self.show_display('3'))
        self.button_4.clicked.connect(lambda: self.show_display('4'))
        self.button_5.clicked.connect(lambda: self.show_display('5'))
        self.button_6.clicked.connect(lambda: self.show_display('6'))
        self.button_7.clicked.connect(lambda: self.show_display('7'))
        self.button_8.clicked.connect(lambda: self.show_display('8'))
        self.button_9.clicked.connect(lambda: self.show_display('9'))
        self.button_add.clicked.connect(lambda: self.show_display('+'))
        self.button_sub.clicked.connect(lambda: self.show_display('-'))
        self.button_mul.clicked.connect(lambda: self.show_display('*'))
        self.button_div.clicked.connect(lambda: self.show_display('/'))
        self.button_clear.clicked.connect(self.clear_display)
        #self.button_clear.clicked.connect(self.save_function)
        #self.button_clear.clicked.connect(self.load_function)
        #self.button_quit.clicked.connect(self.quit_function)
        #save, load, quit function needed
        #button with the result function is needed here !!!

    
    #show numbers, operations of multiple numbers
    def show_display(self, text):
        current_text = self.result_display.text()
        new_text = current_text + text
        self.result_display.setText(new_text)

    #clear numbers, calculation
    def clear_display(self):
        self.result_display.setText('')
        message = QMessageBox()
        message.setIcon(QMessageBox.Icon.Information)
        message.setWindowTitle("note")
        message.setText("Calculation cleared!")
        message.exec()
        

#execute programm
if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

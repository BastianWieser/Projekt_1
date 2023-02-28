"""
GUI-Calculator
Die GUI ist fertig, vielleicht muss sie ein wenig angepasst werden,
abhängig von den zusätzlichen Rechenfunktionen. 
Es sind keine Rechenfunktionen momentan vorhanden. Nur eine optische GUI
by tobias
26.02.2023
<<<<<<< HEAD
"""
=======

Branch von der GUI
Erweiterung der GUI mit den benötigten Funktionen um einfache arithmetische Rechnungen und complexe zahlen zu rechnen
+Erweiterung der GUI mit Komma, imaginäres j 
+Funktion die hinzugefügt wurden:
- result_calc()
by Kadir
27.02.2023
"""
import cmath
>>>>>>> master
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
=======
        result = 0
>>>>>>> master

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
<<<<<<< HEAD
        self.button_empty1 = QPushButton(' ')
        self.button_empty2 = QPushButton(' ')
=======
        self.button_kom = QPushButton('.')
        self.button_img = QPushButton('j')
>>>>>>> master
        self.button_result = QPushButton('=')
        self.button_clear = QPushButton('Clear')

        #create button layout, vertical and horizontal
        vbox = QVBoxLayout()
        hbox0 = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        
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

<<<<<<< HEAD
        hbox4.addWidget(self.button_empty1)
        hbox4.addWidget(self.button_0)
        hbox4.addWidget(self.button_empty2)
=======
        hbox4.addWidget(self.button_kom)
        hbox4.addWidget(self.button_0)
        hbox4.addWidget(self.button_img)
>>>>>>> master
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
<<<<<<< HEAD
        self.button_clear.clicked.connect(self.clear_display)
        #button with the result function is needed here !!!
=======
        self.button_kom.clicked.connect(lambda: self.show_display('.'))
        self.button_img.clicked.connect(lambda: self.show_display('j'))

        self.button_result.clicked.connect(self.result_calc)
        self.button_clear.clicked.connect(self.clear_display)
>>>>>>> master

    #show number or function on button
    def show_display(self, text):
        current_text = self.result_display.text()
        new_text = current_text + text
        self.result_display.setText(new_text)

    #clear numbers, calculation
    def clear_display(self):
        self.result_display.setText('')

<<<<<<< HEAD
=======
    # calculate result and show on display
    def result_calc(self,result):
        try:

            expr = self.result_display.text()
            # replace 'j' with 'j' * 1j to create complex numbers
            expr = expr.replace('j', 'j*1j')
            # evaluate the expression using eval()
            result = eval(expr)

            # check if the result is a complex number and format it accordingly
            if isinstance(result, complex):
                result = '{:.2f}'.format(result.real)
            else:
                result = str(result)
            self.result_display.setText(result)
        except (SyntaxError, ZeroDivisionError, TypeError):
            self.result_display.setText('Error')

    


>>>>>>> master
#execute programm
if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

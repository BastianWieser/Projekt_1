"""
GUI-Calculator
Die GUI ist fertig, vielleicht muss sie ein wenig angepasst werden,
abhängig von den zusätzlichen Rechenfunktionen. 
Es sind keine Rechenfunktionen momentan vorhanden. Nur eine optische GUI
außer clear function und eingabe option
by tobias
26.02.2023
<<<<<<< HEAD
"""

"""
Branch von der GUI
Erweiterung der GUI mit den benötigten Funktionen um einfache arithmetische Rechnungen und complexe zahlen zu rechnen
+Erweiterung der GUI mit Komma, imaginäres j 
+Funktion die hinzugefügt wurden:
- result_calc()
by Kadir
27.02.2023
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

        self.button_kom = QPushButton('.')
        self.button_img = QPushButton('j')
        self.button_result = QPushButton('=')
        self.button_clear = QPushButton('Clear')

        self.button_save = QPushButton('Save')
        self.button_load = QPushButton('Load')
        self.button_quit = QPushButton('Quit')

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

        hbox4.addWidget(self.button_kom)
        hbox4.addWidget(self.button_0)
        hbox4.addWidget(self.button_img)
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
        self.button_kom.clicked.connect(lambda: self.show_display('.'))
        self.button_img.clicked.connect(lambda: self.show_display('j'))
        

        self.button_result.clicked.connect(self.result_calc)
        self.button_clear.clicked.connect(self.clear_display)
        self.button_save.clicked.connect(self.save_function)
        self.button_load.clicked.connect(self.load_function)
        self.button_quit.clicked.connect(self.quit_function)

    #show number or function on button
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
        
    
        
    #calculate result and show on display
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
        self.save_result = result
            
    def save_function(self):
        save_data = f"{self.save_result}" #makes the result a string
        f = QFileDialog.getSaveFileName(self) #makes a new file an lets you save it
        with open (f[0], "w+") as fobj:
            fobj.write(save_data)
            
    def load_function(self):
        loadresult= QFileDialog.getOpenFileName(self)
        with open (loadresult[0], "r") as fobj:
            read = fobj.readline()
            self.show_display(read)
            
    def quit_function(self):
        sys.exit()
            
            
        
        
#execute programms
if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())

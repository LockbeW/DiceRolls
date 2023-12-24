import sys
import random
import time

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIntValidator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(300, 500))
        MainWindow.setMaximumSize(QtCore.QSize(300, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        self.checkButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.checkButton.setGeometry(QtCore.QRect(109, 60, 83, 30))
        self.checkButton.setObjectName("checkButton")
        self.checkButton.clicked.connect(self.diceRolls)
        

        self.inputLine = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputLine.setGeometry(QtCore.QRect(110, 15, 81, 40))
        self.inputLine.setObjectName("inputLine")
        self.inputLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputLine.setMaxLength(1)
        int_validator = QIntValidator(1, 10)
        self.inputLine.setValidator(int_validator)
        

        self.outputLine = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.outputLine.setGeometry(QtCore.QRect(0, 100, 400, 400))
        self.inputLine.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.outputLine.setHtml('<p style="margin-left: 86px;">Enter number of dice.</p>')
        self.outputLine.setObjectName("outputLine")
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dice Rolls"))
        self.checkButton.setText(_translate("MainWindow", "Check"))

    def diceRolls(self):
        if self.inputLine.text() == '':
            return
        
        inputNumber = int(self.inputLine.text())        
        combinations = {}
        
        for i in range(inputNumber, (inputNumber * 6) + 1):
            combinations[i] = 0

        lastRandSeed = time.time()
        for i in range(1000000):
            if time.time() > lastRandSeed + 1:
                lastRandSeed = time.time()
            total = 0
            for j in range(inputNumber):
                total = total + random.randint(1, 6)
            combinations[total] = combinations[total] + 1
            
        htmlInsertion = ''
        for i in range(inputNumber, (inputNumber * 6) + 1):
            totalRolls = combinations[i]
            percentage = round(combinations[i] / 10000, 1)
            htmlInsertion += f'<tr><td style="border: 1px solid #000000; text-align: center; padding: 5px;">{i}</td> \
                               <td style="border: 1px solid #000000; text-align: center; padding: 5px;">{totalRolls}</td> \
                               <td style="border: 1px solid #000000; text-align: center; padding: 5px;">{percentage}%</td></tr>'

        html = f"""
                <table style="margin-left: 7px; margin-right: 7px;">
                <tbody>
                <tr>
                <th style="border: 1px solid #000000; padding: 5px;">COMBINATION</th>
                <th style="border: 1px solid #000000; padding: 5px;">TOTAL ROLLS</th>
                <th style="border: 1px solid #000000; padding: 5px;">PERCENTAGE</th>
                </tr>
                {htmlInsertion}
                </tbody>
                </table>
                """
        
        self.outputLine.setHtml(html)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

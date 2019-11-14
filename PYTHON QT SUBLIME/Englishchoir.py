from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Eng(QMainWindow):
    def __init__(self):
        super(Eng, self).__init__()
        self.setGeometry(100,200,400,350)
        self.setWindowTitle("English Choir")
        self.UI()

    def UI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Welcome to St. Cecilia English Choir, St James Umule Aba\nEnter your details for validation\n\nUsername:\nPassword:")
        self.label.move(20,10)
        self.label.adjustSize()

        self.pb = QtWidgets.QPushButton(self)
        self.pb.setText("Login")
        self.pb.move(100,130)
        self.pb.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Login successful!")
        self.label.move(150,50)


def mywindow():
    app = QApplication(sys.argv)
    win = Eng()
    win.show()
    sys.exit(app.exec_())

mywindow()


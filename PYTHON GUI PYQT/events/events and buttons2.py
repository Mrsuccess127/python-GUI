from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


#creating a class 
class genwindow(QMainWindow):
  def __init__(self):
	super().__init__()
	self.setGeometry(100,200,400,350)
	self.setWindowTitle("embedded Systems")
	self.UI()	

  def UI(self):
 	self.label = QtWidgets.QLabel(self)
	self.label.setText("Welcome to Embedded systems/IOT department\nPlease enter your details for validation\n\nUsername:\nPassword:")
	self.label.move(1,1)
	self.label.adjustSize()

    self.pb = QtWidgets.QPushButton(win)
    self.pb.setText("Login")
	self.pb.move(1,70)


def mywindow():
 	app = QApplication(sys.argv)
 	win = genwindow()
 	win.show()
 	sys.exit(app.exec_())

mywindow()

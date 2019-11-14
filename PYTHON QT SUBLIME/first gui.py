from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


#writiing a function for the button
def clicked():
	print("Successful")

#writing a function for the app
def firstapp():
	app = QApplication(sys.argv) #for system settings and configuration...depends on the system os 
	win = QMainWindow()
	win.setGeometry(200, 200, 300, 300)  #(X-position, Y-position, height, width)
	win.setWindowTitle("George")   #setting the title of the app

	label = QtWidgets.QLabel(win) #setting the label to appear inside win
	label.setText("username:\nPassword:") #adding a text 
	label.move(1,0)

	#creating a button
	pb = QtWidgets.QPushButton(win)
	pb.setText("Login")
	pb.move(1,30)
	pb.clicked.connect(clicked)

	
	win.show()  #display the app
	sys.exit(app.exec_()) #enables the user to exit the app after use

	#calling the app function
firstapp()
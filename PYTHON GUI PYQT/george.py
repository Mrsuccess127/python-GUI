from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#writing a function for the app
def myapp():
	app = QApplication(sys.argv) #for system settings and configuration...depends on the system os 
	win = QMainWindow()
	win.setGeometry(1000,200,300,500)  #(X-position, Y-position, width, height)
	win.setWindowTitle("George")   #setting the title of the app

	#setting label
	label = QtWidgets.QLabel(win) #setting label to appear in the window
	label.setText("Username: \nPassword:")
	label.move(0,0)

	
	win.show()  #display the app
	sys.exit(app.exec_()) #enables the user to exit the app after use

	#calling the app function
myapp()
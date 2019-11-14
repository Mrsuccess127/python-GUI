from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#  creating a function for the app
def firstapp():
    app = QApplication(sys.argv) #system set up for the app...depends on the particular system
    win = QMainWindow()
    win.setGeometry(200,100,300,200)  #(X-position, Y-position, width, height)......setting the size and shape of the APP
    win.setWindowTitle("tutorial")

    #setting the label
    label = QtWidgets.QLabel(win)   #setting label
    label.setText("This is my first GUI") #adding a text
    label.move(50, 50)

    #to display the app
    win.show()
    sys.exit(app.exec_())  #allows a user to exit the app after using it

#calling th app function
firstapp()
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#writing a function to be called when the push button is clicked
def clicked():
    print("login successful") #This will only be displayed on the terminal of the IDE
def app():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("tutorials")
    #Adding label
    label = QtWidgets.QLabel(win)
    label.setText("Username:\nPassword:")
    label.move(1,1)
    

    #Adding a button
    pb = QtWidgets.QPushButton(win) #setting push button in the app environment
    pb.setText("Login")
    pb.move(1,30)
    pb.clicked.connect(clicked) #To map the push button to the function
  
    win.show()
    sys.exit(app.exec_())

app()
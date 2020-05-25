# Main File: Application.py
# This is the main file for the program.
import sys
from PySide2 import QtCore, QtWidgets, QtGui

class Application(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        # Setting up the Window
        self.resize(1050, 525)
        self.setWindowTitle("Location Navigation - An Interactive Python Project")
        #Setting up the window icon
        iconpixmap = QtGui.QPixmap('/Users/anjal/Desktop/Personal Projects/PythonProj/DijkstrasProj/icon.png')
        self.setWindowIcon(QtGui.QIcon(iconpixmap))
        # insert the image
        pixmap = QtGui.QPixmap('/Users/anjal/Desktop/Personal Projects/PythonProj/DijkstrasProj/map.jpg')
        label = QtWidgets.QLabel()
        label.setPixmap(pixmap)

        # Create the Widgets in the centre
        centrelay = QtWidgets.QHBoxLayout() # This is the HBox into which all the things will go
        horLayout = QtWidgets.QGroupBox() # main groupBox
        boxButton = QtWidgets.QDialogButtonBox() # Adds the buttons to this box
        addbutton = QtWidgets.QPushButton("Add Location") # Add location button
        rembutton = QtWidgets.QPushButton("Remove Location") # Remove location button
        textBox = QtWidgets.QTextEdit("Welcome To Location Navigation!\n \n") # TextBox for commands
        textBox.setReadOnly(True) # This makes the textBox Read-Only
        
        # Add buttons to boxButton
        boxButton.addButton(addbutton, QtWidgets.QDialogButtonBox.ActionRole)
        boxButton.addButton(rembutton, QtWidgets.QDialogButtonBox.ActionRole)
        # Add textbox and buttonbox to hbox
        centrelay.addWidget(textBox)
        centrelay.addWidget(boxButton)
        #Add the hbox to the GroupBox
        horLayout.setLayout(centrelay)
        
        # Create the widgets on the left
        button1 = QtWidgets.QPushButton("Find Shortest Time") # Dijkstras Button(layout1)
        button2 = QtWidgets.QPushButton("Find Shortest Path") # TSP Button(layout1)
        innerlay = QtWidgets.QVBoxLayout() # The VBox within the layout VBox (VBoxCeption?)
        layout1 = QtWidgets.QGroupBox() # main groupBox
        layout2 = QtWidgets.QHBoxLayout() # main layout
        location1 = QtWidgets.QRadioButton("Location 1") # RadioButton1
        location2 = QtWidgets.QRadioButton("Location 2") # RadioButton2
        buttonBox = QtWidgets.QDialogButtonBox() 
       
        #Adding Buttons to ButtonBox
        buttonBox.addButton(button1, QtWidgets.QDialogButtonBox.ActionRole) # Adding Button1 to ButtonBox
        buttonBox.addButton(button2, QtWidgets.QDialogButtonBox.ActionRole) # Adding Button2 to ButtonBox
 
        # Adding Widgets to layouts
        innerlay.addWidget(location1) # Adding RadioButton1 to innerlayout
        innerlay.addWidget(location2) # Adding RadioButton2 to innerlayout
        innerlay.addWidget(buttonBox) # Adding buttonBox to the innerLayout
        innerlay.addStretch(1)
        # Then setting the vbox layout to the Groupboxes
        layout1.setLayout(innerlay)
        
        vboxlay = QtWidgets.QVBoxLayout() # Vertical Box layout
        horGroupBox = QtWidgets.QGroupBox() # A new group box for vboxlay
        # Add the image and the horlayout to a vertical layout
        vboxlay.addWidget(label) 
        vboxlay.addWidget(horLayout)
        # Then add vboxlay to a groupBox, and add that groupbox to layout2
        horGroupBox.setLayout(vboxlay)

        # Adding the layouts to the groups
        layout2.addWidget(layout1)
        layout2.addWidget(horGroupBox)

        # adding layouts to self
        self.setLayout(layout2)


if __name__ == '__main__':     
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    applic = Application()
    applic.show()
    # Run the main Qt loop
    sys.exit(app.exec_())




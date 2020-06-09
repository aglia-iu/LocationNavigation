# Main File: Application.py
# This is the main file for the program.
from LocationNavigation import LocationNavigation
from PySide2 import QtCore, QtWidgets, QtGui
import sys

# This is the main application for the Main Dialog of the Project.
class Application(QtWidgets.QDialog): 
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        # Setting up the Window
        self.resize(1250, 925)
        self.setWindowTitle("Location Navigation - An Interactive Python Project")
        #Setting up the window icon
        iconpixmap = QtGui.QPixmap('/Users/anjal/Desktop/Personal Projects/PythonProj/DijkstrasProj/icon.png')
        self.setWindowIcon(QtGui.QIcon(iconpixmap))
        self.locationButtons = []
        
        # insert the image
        self.pixmap = QtGui.QPixmap('/Users/anjal/Desktop/Personal Projects/PythonProj/DijkstrasProj/map.jpg')
        self.label = QtWidgets.QLabel()
        self.label.setPixmap(self.pixmap)

        layout2 = QtWidgets.QHBoxLayout() # main layout
        vboxlay = QtWidgets.QVBoxLayout() # Vertical Box layout
        horGroupBox = QtWidgets.QGroupBox() # A new group box for vboxlay
        # Add the image and the horlayout to a vertical layout
        vboxlay.addWidget(self.label) 
        vboxlay.addWidget(self.CentreBottom())
        # Then add vboxlay to a groupBox, and add that groupbox to layout2
        horGroupBox.setLayout(vboxlay)
        # Adding the layouts to the groups
        layout2.addWidget(self.LeftWidgets())
        layout2.addWidget(horGroupBox)

        # Adding functionality to the buttons
        self.button1.clicked.connect(self.shortestTimeDialogue)
        self.button2.clicked.connect(self.shortestPathDialog)
        self.button3.clicked.connect(self.shortestPathTwo)
        self.addbutton.clicked.connect(self.AddDialogueBox)
        self.rembutton.clicked.connect(self.RemoveDialogueBox)
        # adding layouts to self
        self.setLayout(layout2)
    
    # This sets the Centre - Bottom area of the Dialogue
    def CentreBottom(self):
        # Create the Widgets in the centre
        centrelay = QtWidgets.QHBoxLayout() # This is the HBox into which all the things will go
        horLayout = QtWidgets.QGroupBox() # main groupBox
        self.boxButton = QtWidgets.QDialogButtonBox() # Adds the buttons to this box
        self.addbutton = QtWidgets.QPushButton("Add Location") # Add location button
        self.rembutton = QtWidgets.QPushButton("Remove Location") # Remove location button
        self.textBox = QtWidgets.QTextEdit("Welcome To Location Navigation!\n \n") # TextBox for commands  
        self.textBox.setReadOnly(True)
        # Add buttons to boxButton
        self.boxButton.addButton(self.addbutton, QtWidgets.QDialogButtonBox.ActionRole)
        self.boxButton.addButton(self.rembutton, QtWidgets.QDialogButtonBox.ActionRole)
        # Add textbox and buttonbox to hbox
        centrelay.addWidget(self.textBox)
        centrelay.addWidget(self.boxButton)
        #Add the hbox to the GroupBox
        horLayout.setLayout(centrelay)
        # Functionality of addbutton
        return horLayout
    
    def LeftWidgets(self):
        # Create the widgets on the left
        self.button1 = QtWidgets.QPushButton("Find Shortest Time") 
        self.button2 = QtWidgets.QPushButton("Find Shortest Path (Multiple Locations)") # Dijkstras Button(layout1) 
        self.button3 = QtWidgets.QPushButton("Find Shortest Path (Two Locations)") # Dijkstras Button(layout1)
        self.innerlay = QtWidgets.QVBoxLayout() # The VBox within the layout VBox (VBoxCeption?)
        self.vlay = QtWidgets.QVBoxLayout() # The VBox within the layout
        groupbox = QtWidgets.QGroupBox("Neighbours") 
        layout1 = QtWidgets.QGroupBox() # main groupBox
        #self.location1 = QtWidgets.QRadioButton("Location 1") # RadioButton1
        #self.location2 = QtWidgets.QRadioButton("Location 2") # RadioButton2
        self.buttonBox = QtWidgets.QVBoxLayout()
        groupbutton = QtWidgets.QGroupBox()
        #Adding Buttons to ButtonBox
        #self.buttonBox.addButton(self.button1, QtWidgets.QDialogButtonBox.ActionRole)
        self.buttonBox.addWidget(self.button1) # Adding Button1 to ButtonBox
        self.buttonBox.addWidget(self.button2) # Adding Button2 to ButtonBox
        self.buttonBox.addWidget(self.button3) # Adding Button3 to ButtonBox
        groupbutton.setLayout(self.buttonBox)
        # Adding Widgets to layouts
        groupbox.setLayout(self.vlay)
        self.innerlay.addWidget(groupbox)
        self.innerlay.addWidget(groupbutton) # Adding buttonBox to the innerLayout
        self.innerlay.addStretch(1)
        # Then setting the vbox layout to the Groupboxes
        layout1.setLayout(self.innerlay)
        
        return layout1
    
    # This is the dialogue box that I want to be able to use to add a new Location and to 
    # add a Location to the Location bar.
    def AddDialogueBox(self):
        self.dialogbox = QtWidgets.QDialog()
        self.dialogbox.setModal(True)
        self.dialogbox.resize(300,150)
        self.dialogbox.setWindowTitle("Add Location")

        self.namelabel = QtWidgets.QLabel("Name") # Name Label
        self.neighbourLabel = QtWidgets.QLabel("Neighbour") # Neighbour Label
        self.weightLabel = QtWidgets.QLabel("Distance from Neighbour") # Weight Label
        self.name = QtWidgets.QLineEdit() # Used to enter in the location name
        vboxlay = QtWidgets.QVBoxLayout() # The VBox within the layout VBox
        
        hbox = QtWidgets.QHBoxLayout()
        groupbox = QtWidgets.QGroupBox() # main groupBox
        self.buttonOkBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok) # The button box containing OK button
        self.checklist = list()
        self.weight = QtWidgets.QLineEdit() # Used to get the Weight
        checkIndex = 0
        vboxlay.addWidget(self.namelabel)
        vboxlay.addWidget(self.name)
        vboxlay.addWidget(self.neighbourLabel)
        # For-Loop to create neighbouring buttons
        for x in LocationNavigation.locations:
            checkIndex = LocationNavigation.locations.index(x)
            neighbName = str(LocationNavigation.locations[checkIndex].getName())
            self.radiobut = QtWidgets.QRadioButton(neighbName)
            self.checklist.append(self.radiobut)
            vboxlay.addWidget(self.radiobut)

        if (len(LocationNavigation.locations) > 0):
            vboxlay.addWidget(self.weightLabel)
            vboxlay.addWidget(self.weight)

        # Add the Widgets to vboxlay, then to groupbox   
        
        vboxlay.addWidget(self.buttonOkBox)
        self.buttonOkBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.accept)
        groupbox.setLayout(vboxlay)
        hbox.addWidget(groupbox)
        # Then set the layout to the groupbox
        self.dialogbox.setLayout(hbox)
        self.dialogbox.exec_()
    
    # This is the dialogue box used to remove values from the Program
    def RemoveDialogueBox(self):
        self.remdialogbox = QtWidgets.QDialog()
        self.remdialogbox.setModal(True)
        self.remdialogbox.resize(200,150)
        self.remdialogbox.setWindowTitle("Remove Location")

        self.toplabel = QtWidgets.QLabel("Select Location to Remove: ")
        self.vboxlay = QtWidgets.QVBoxLayout() # The VBox within the layout VBox
        self.OkBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok) # The button box containing OK button
        self.vboxlay.addWidget(self.toplabel)
        self.remchecklist = list()
        # For-Loop to create neighbouring buttons
        for x in LocationNavigation.locations:
            self.checkIndex = LocationNavigation.locations.index(x)
            neighbName = str(LocationNavigation.locations[self.checkIndex].getName())
            self.remneighbbut = QtWidgets.QRadioButton(neighbName)
            self.remchecklist.append(self.remneighbbut)
            self.vboxlay.addWidget(self.remneighbbut)
        self.vboxlay.addWidget(self.OkBox)    
        self.OkBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.remove)
        self.remdialogbox.setLayout(self.vboxlay)
        self.remdialogbox.exec()
    
    
    # This is the dialogue box for the shortest time dialogue box
    def shortestTimeDialogue(self):
        self.stdialogbox = QtWidgets.QDialog() # The dialogbox for the shortest time.
        self.stdialogbox.setModal(True)
        self.stdialogbox.resize(300,150)
        self.stdialogbox.setWindowTitle("Shortest Time")
        self.transport = [] # The transport array of the buttons

        vbox = QtWidgets.QVBoxLayout() # The vboxlayout
        walkRad = QtWidgets.QRadioButton("Time by Walk") # The walk button
        bikeRad = QtWidgets.QRadioButton("Time by Bike") # The bike button
        busRad = QtWidgets.QRadioButton("Time by Bus") # The bus button
        buttonOkBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok) # The OK button
        self.transport.append(walkRad)
        self.transport.append(bikeRad)
        self.transport.append(busRad)

        # Upon selecting the Ok button, we are connected to the shortestTime method
        buttonOkBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.shortestTime)

        #Add the required widgets
        vbox.addWidget(walkRad)
        vbox.addWidget(bikeRad)
        vbox.addWidget(busRad)
        vbox.addWidget(buttonOkBox)

        # Set the layout
        self.stdialogbox.setLayout(vbox)
        self.stdialogbox.exec()
    
    # Shortest path dialogue:
    def shortestPathDialog(self):
        self.spdialogbox = QtWidgets.QDialog()
        self.spdialogbox.setModal(True)
        self.spdialogbox.resize(200,150)
        self.spdialogbox.setWindowTitle("Shortest Path Multiple")
        toplabel = QtWidgets.QLabel("Select Starting Location")

        vboxlayout = QtWidgets.QVBoxLayout() # The VBox within the layout VBox
        vboxlayout.addWidget(toplabel)
        self.spchecklist = list()
        self.spOkBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok) # The button box containing OK button
        for x in LocationNavigation.locations:
            checkIndex = LocationNavigation.locations.index(x)
            neighbName = str(LocationNavigation.locations[checkIndex].getName())
            self.radiobuttons = QtWidgets.QRadioButton(neighbName)
            self.spchecklist.append(self.radiobuttons)
            vboxlayout.addWidget(self.radiobuttons)
        vboxlayout.addWidget(self.spOkBox)    
        self.spOkBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.shortestPathMultiple)
        self.spdialogbox.setLayout(vboxlayout)
        self.spdialogbox.exec()
        
        
    # This is the def that is used when the 'Ok' Button is clicked.
    # -------------------------------------------------------------
    # NO PARAMS, NO RETURN
    def accept(self):
        checkIndex = 0
        neighbarr = list()
        weightarr = list()
        if(len(LocationNavigation.locations) > 0):
            for __ in range(0, len(LocationNavigation.locations)):
                neighbarr.append(-1)
                weightarr.append(-1)
    
        if (len(self.checklist)>0):
            for x in self.checklist:
                if x.isChecked():
                    checkIndex = self.checklist.index(x) 
                    if(len(LocationNavigation.locations) == 0):
                        neighbarr.append(LocationNavigation.locations[checkIndex])
                        weightarr.append(self.weight.text())  
                    else:
                        neighbarr[checkIndex] = (LocationNavigation.locations[checkIndex])
                        weightarr[checkIndex] = (self.weight.text())  
               
        node1 = LocationNavigation.addLocation(self,self.name.text(), neighbarr, weightarr)
        self.location = QtWidgets.QCheckBox(node1.getName())
        self.locationButtons.append(self.location)
        self.vlay.addWidget(self.location, QtWidgets.QDialogButtonBox.ActionRole) # Adding location to ButtonBox
        self.textBox.append(str(node1.getName()) + " added!")
        self.dialogbox.close()
    
    # This is the method that is executed when an item is removed
    # ------------------------------------------------------------
    # NO PARAMS, NO RETURN 
    def remove(self):
        checkIndex = 0
        # This is the method used to remove
        if (len(self.remchecklist) > 0):
            for x in self.remchecklist:
                if x.isChecked():
                    checkIndex = self.remchecklist.index(x)    
        else:
            return None   
        
        b = self.vlay.takeAt(checkIndex)
        self.widget = self.remchecklist[checkIndex]
        self.vlay.removeWidget(self.widget)
        w = b.widget()
        w.setParent(None)

        self.remchecklist.remove(self.remchecklist[checkIndex])
        node = LocationNavigation.locations[checkIndex]
        self.locationButtons.remove(self.locationButtons[checkIndex])
        LocationNavigation.removeLocation(self, node)
        self.textBox.append(str(node.getName()) + " removed!")
        self.remdialogbox.close()

    # This is a helper method that is used to find the selected locations
    # ------------------------------------------------------------------
    # NO PARAMS
    # RETURN: An array of selected nodes.
    def __getLocations__(self):
        nameArray = []
        nodeArray = []
        # First we iterate through the selected nodes and get their names.
        if (len(self.locationButtons) > 0):
            for x in self.locationButtons:
                if x.isChecked():
                    nameArray.append(x.text())
        # Then we get the iterate through the list of names and get those nodes
        # that match the names.
        if(len(LocationNavigation.locations) > 0):
            for x in LocationNavigation.locations:
                for y in nameArray:
                    if x.getName() == y:
                        nodeArray.append(x)
        return nodeArray
   
    # This is the shortest path that is used to display the shortestPath 
    # after being connected to the Dijkstra's algorithm in the LocationNavigation
    # Class.
    #  --------------------------------------------------------------------------
    # NO PARAMS, NO RETURNS
    def shortestPathMultiple(self):
        nodeArray = []
        nodeArray = self.__getLocations__()
       
        # Then we call findShortestPath from the LocationNavigation class, and make 
        # sure that we initiate the startNode as being the node with the lowest index.
        checkIndex = 0
        # This is the method used to remove
        if (len(self.spchecklist) > 0):
            for x in self.spchecklist:
                if x.isChecked():
                    checkIndex = self.spchecklist.index(x)    
        else:
            return None   
        
        startNode = LocationNavigation.locations[checkIndex]
        finalPath = LocationNavigation.findShortestPath(self, nodeArray,startNode)    
        if(finalPath == None):
            self.textBox.append("Sorry, this path is not possible. Please try another location.")
        else:
            self.textBox.append("The shortest possible path is: ")    
            for x in finalPath:
                if finalPath.index(x) == (len(finalPath) - 1):
                    self.textBox.append(str(x.getName()))
                else:
                    self.textBox.append(str(x.getName()) + ",")  
        self.spdialogbox.close()
    
    # This is the shortest path that is used to display the shortestPath 
    # after being connected to the BFS's algorithm in the LocationNavigation
    # Class.
    #  --------------------------------------------------------------------------
    # NO PARAMS, NO RETURNS
    def shortestPathTwo(self):
        nodeArray = []
        nodeArray = self.__getLocations__()

        if(len(nodeArray) > 2):
            self.textBox.append("Please select only two locations.")
            return None
        
        path = LocationNavigation.BFSfunction(self, nodeArray[0], nodeArray[1])
        
        if(path == None):
            self.textBox.append("Sorry, this path is not possible. Please try another location.")
        else:
            self.textBox.append("The shortest possible path is: ")    
            for x in path:
                if path.index(x) == (len(path) - 1):
                    self.textBox.append(str(x.getName()))
                else:
                    self.textBox.append(str(x.getName()) + ",") 

    # This is used to find the shortest time of the list after being 
    # connected to the shortestTime method in locationNavigation.
    # --------------------------------------------------------------
    # NO PARAMS, NO RETURNS
    def shortestTime(self):
        # First we must determine the method of transport
        index = -1
        for x in self.transport:
            if x.isChecked():
                index = self.transport.index(x)
        # Then we get the array of selected nodes
        nodeArray = []
        nodeArray = self.__getLocations__()
        # Finally we use these to call the shortestTime method in location
        # navigation
        timeTaken = LocationNavigation.shortestPathTime(self, index, nodeArray,nodeArray[0])
        self.textBox.append("The shortest possible time is: " + str(timeTaken) + " minutes.")
        self.stdialogbox.close()
    
    # This is the method that we must use to set up the mouse cursor for when we 
    # move onto the map.
    #def mapLocation(self):
    #    mousepixmap = QtGui.QPixmap('/Users/anjal/Desktop/Personal Projects/PythonProj/DijkstrasProj/mapicon.png')
    #    cursor = QtGui.QCursor(mousepixmap)
    #    self.setOverrideCursor(cursor)
    #    self.cursor.clicked.connect(self.restoreOverrideCursor())
if __name__ == '__main__':     
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    applic = Application()
    applic.exec_()
    # Run the main Qt loop
    sys.exit(app.exec_())

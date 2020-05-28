
# This is the test file that tests both the LocationNode class and the Program class
# It contains two vlasses: A NodeTest Class and a ProgramTest class.

import sys
import LocationNode
from LocationNavigation import LocationNavigation
from LocationNode import LocationNode
from PySide2 import QtCore, QtWidgets, QtGui

# Used to test the LocationNode class. Must test the following:
# 1. Creating a node - both correctly and incorrectly *
# 2. Adding neighbours to the node. *
# 3. Getting each of the variables of the node and testing them to be sure they have been set correctly*
# 4. Creates multiple nodes correctly.*

class NodeTest(object):
    
    # Tests the ability to create a Node
    def test1_createNode(self):
        name = "Church"
        value = 0
        node = LocationNode(name, value)

        if (node == None):
            print("test1 failed: node was not correctly initialized.")
        else:
            print("test1 passed!")
    # Tests the ability to add Neighbours
    def test2_addNeighbs(self):
        # Anna and Sarah are neighbours
        name1 = "Anna" 
        name2 = "Sarah"
        value = 0
        # Set 2 location nodes to one another
        node1 = LocationNode(name1, value)
        value += 1
        node2 = LocationNode(name2, value)
        # Add Sarah as Anna's neighbour
        node1.addNeighbour(node2)
        # Setting up the neighbour checkers
        neighbour = node1.getNeighbours()
        neighboursize = len(neighbour)
        neighbour2 = node2.getNeighbours()
        neighbour2size = len(neighbour2)
        # Getting data of Anna
        if(neighboursize != 1) or (neighbour[0].getName() != name2):
            print("test2_a failed: expected size = 1; obtained size = " 
            + str(neighboursize) + "; expected neighb = Sarah")
        else:
            print("test2_a passed!")
        # Getting data of Sarah
        if(neighbour2size != 1) or (neighbour2[0].getName() != name1):  
            print("test2_b failed: expected size = 1; obtained size = " 
            + str(neighbour2size) + "; expected neighb = Sarah")
        else:
             print("test2_b passed!") 

    # Tests the ability to make getters and setters, and making multiple nodes successfully
    def test3_GettersNSetters(self):
        # There is a library next to the Diner
        name1 = "Library"
        name2 = "Joe's Diner"
        value = 0
        # We make two locationNodes out of this
        node4 = LocationNode(name1, value)
        value += 1
        node5 = LocationNode(name2, value)
        # We add the Library and the Diner as neighbours
        node4.addNeighbour(node5)
        # Getting data of Library
        name4test = node4.getName()
        neighbour4test = node4.getNeighbours()
        value4test = node4.getValue()
        # Getting Data of Diner
        name5test = node5.getName()
        neighbour5test = node5.getNeighbours()
        value5test = node5.getValue()
        # Get the tests for Library
        if (name4test != name1) or (len(neighbour4test) != 1)or (neighbour4test[0].getName() != name2) or (value4test != 1):
             print("test3_a failed: expected value = 1; obtained value = " 
            + str(value4test) + "; expected neighb = Joe's Diner, obtained neighb = " + neighbour4test[0].getName() +"; expected name = Library, obtained name: " 
            + name4test + "; expected length = 1, obtained length = " + str(len(neighbour4test)))
        else:
            print("test3_a passed!")
        # Get the tests for Diner
        if (name5test != name2) or (len(neighbour5test) != 1) or (neighbour5test[0].getName() != name1) or (value5test != 2):
             print("test3_b failed: expected value = 2; obtained value = " 
            + str(value5test) + "; expected neighb = Library, obtained neighb = " + neighbour5test[0].getName() + "obtained name: " 
            + name5test+ "; expected length = 1, obtained length = " + str(len(neighbour5test)))
        else:
            print("test3_b passed!")
class NavigTests():
    def test1_createLocation(self):
        return None
    def test2_removelocation(self):
        return None
    #def testE_testLoop(self):
    #    self.box = QtWidgets.QDialogButtonBox() # Adds the buttons to this box
    #    self.checklist = list()
    #    self.checkbut = QtWidgets.QCheckBox()
    #    neighbName = ""
    #    # For-Loop to create neighbouring buttons
    #    for x in LocationNavigation.locations:
    #        neighbName = str(LocationNavigation.locations[x].getName())
    #        self.checkbut = QtWidgets.QCheckBox(neighbName)
    #        self.checklist.append(self.checkbut)
    #        self.box.addButton(self.checkbut)
    #    testbut = self.checklist[len(self.checklist)-1]
    #    if(testbut != self.checkbut):
    #        print("TestEa_Failed: These two buttons aren't the same.")
if __name__ == '__main__': 
    NodeTest().test1_createNode()
    NodeTest().test2_addNeighbs()
    NodeTest().test3_GettersNSetters()

 
    
    
             
        
        



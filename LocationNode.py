#NAME: Anjali Gali
#PROJECT: Location Navigation - An Interactive Python Project
#MAIN FILE: Application.py
#ASSOCIATED FILE(S): LocationNode.py, ApplicTests.py, LocationNavigation.py
#                   BFSAlgo.txt, Dijkstra.txt,ShortestTime_Algo.txt, icon.png, 
#                   map.jpg, mapicon3.png  
#OVERVIEW: A program used to help track the locations, the shortest paths and 
# shortest time taken between locations across teh UW-Madison campus. Made for the 
# convenience of incoming new students and delivery purposes.
#COPYRIGHT: Copyright (c) Anjali Gali. May - June 2020. All Rights Reserved. 
#
#This is the class to note every location in the map. It will keep track of the name, the index
#and the neighbours of this location.
class LocationNode(object):

    # This is the node for each location
    # ----------------------------------
    # name(String): stores the name of each location
    # neighbours(List<Node>): stores the neighbours of each location
    # value(int): this is the unique identifier of each location.
    def __init__(self, name, value):
        self.name = name
        self.neighbours = [-1 for d in range(50)]
        self.value = value
        self.weights = [-1 for d in range(50)]

    # This gets the name of the Node
    # ------------------------------
    # Returns a (String) name
    def getName(self):
        return self.name

    # This gets the set of neighbours 
    # ------------------------------
    # Returns an (Array) neighbours  
    def getNeighbours(self):
        return self.neighbours

    # This gets the unique value of the Node
    # ------------------------------
    # Returns an (int) value
    def getValue(self):
        return self.value
    # This gets the set of weights
    # ------------------------------
    # Returns an (Array) weights
    def getWeights(self):
        return self.weights

    # This gets a single weight in the set of weights
    # ------------------------------
    # Returns a weight from an (Array) weights
    def getWeight(self, index):
        return self.weights[index]

    # This adds Nodes to the neighbours
    # ------------------------------
    # Returns void
    # NOTE: An ideal way for this to work would be to append node to self's neighbours
    # and to append self to node's neighbours as well.
    def addNeighbour(self, node):
        index = node.getValue()
        self.neighbours[index] = node
        node.neighbours[self.getValue()] = self    
 
    # This sets the weight of the Node
    def addWeight(self, weight, node2):
            self.weights[node2.getValue()] = weight
            node2.weights[self.getValue()] = weight

    # Removes a neighbour
    def removeNeighb(self, node):
        self.neighbours.remove(node)    
          
    # This sets the neighbours
    def setNeighbours(self, neighbours):
        #self.neighbours = neighbours
        for x in neighbours:
            if x != -1:
                x.neighbours[neighbours.index(x)] = (self)
                self.neighbours[neighbours.index(x)] = (x)
            else:
                self.neighbours.append(x)
        

    # This sets the name of the Node     
    def setName(self, name):
        self.name = name
   
    # This sets the weights of the node    
    def setWeights(self, weights):
        for x in weights:
            if(x != -1):
                index = weights.index(x)
                self.addWeight(x, self.neighbours[index])
            else: 
                self.weights.append(x)
            

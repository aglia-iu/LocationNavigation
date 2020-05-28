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
        self.neighbours = []
        self.value = value + 1
        self.weights = []

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
        return self.weights[index - 1]

    # This adds Nodes to the neighbours
    # ------------------------------
    # Returns void
    # NOTE: An ideal way for this to work would be to append node to self's neighbours
    # and to append self to node's neighbours as well.
    def addNeighbour(self, node):
        self.neighbours.append(node)
        node.neighbours.append(self)     
 
    # This sets the weight of the Node
    def addWeight(self, weight, node2):
        index = node2.getValue()
        index2 = self.getValue()
        self.weights[index - 1] = weight
        node2.weights[index2 -1] = weight

    # Removes a neighbour
    def removeNeighb(self, node):
        self.neighbours.remove(node)    
          
    # This sets the neighbours
    def setNeighbours(self, neighbours):
        self.neighbours = neighbours
        for x in neighbours:
            x.neighbours.append(self)

    # This sets the name of the Node     
    def setName(self, name):
        self.name = name
   
    # This sets the weights of the node    
    def setWeights(self, weights):
        self.weights = weights

    
        


    

    
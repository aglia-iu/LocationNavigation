# This is the class that is used to create functionality and add functionality to the 
# Application class. It controls how the functionality of the application works.
import sys
from LocationNode import LocationNode
from Graph import Graph

class LocationNavigation(object):
    # GLOBAL VARIABLES
    index = 0
    locations = []
    graph = Graph()
    # This method is used to create and add a location to the function. It 
    # creates a new location using the name, neighbours and weights that are obtained
    # from a dialogue box created when the user clicks 'Add Location'. Adds newly created 
    # locations to an array called locations from which they can be obtained.
    #-----------------------------------------------------------------------------------
    # name: The name of the Location (String)
    # neighbours: The neighbours of the Location (Array - Node)
    # weights: The weights of the respective node (Array - int)
    # RETURNS: the created node
    #
    def addLocation(self, name, neighbours, weights):
        LocationNavigation.index+=1 # increment the index by one
        node = LocationNode(name, LocationNavigation.index) # Add the node
        # Set the nodes Neighbours and Weights
        node.setNeighbours(neighbours)
        node.setWeights(weights)
        # Add the node to the locations graph.
        LocationNavigation.locations.append(node)
        for x in LocationNavigation.locations:
            print(x.getName() + ", ")
        return node
    
    # This method is used to remove a location. Before removing the location we must remove this 
    # from each of it's neighbouring nodes' neighbour arrays. After removing each of the neighbouring 
    # arrays, we can remove the LocationNode. To remove this node, we can use either the node itself 
    # or the index of the node. Must return a boolean value: True if the node was successfully removed
    # False if unsuccessful.
    # ------------------------------------------------------------------------------------------------
    # node: The node to be removed. 
    # RETURNS: A boolean value: True if the node was successfully removed, False if unsuccessful.
    #
    def removeLocation(self, node):
        neighbours = node.getNeighbours() # Getting the array of neighbours from the node
        for x in neighbours:
            if (x != -1):
                x.removeNeighb(node)
        
        LocationNavigation.locations.remove(node)
        #LocationNavigation.graph.removeVertex(node)
    
    # This method uses Dijkstra's Algorithm to find the shortest path between 
    # two nodes and returns an array of the locations to be used between the 
    # two nodes to return the shortest possible path.
    # PARAMS: nodeList(array): The list of selected nodes.
    #         startNode(LocationNode): The node from which we  
    # RETURN: A list containing the shortest path of nodes to the end path
    def findShortestPath(self, nodeList, startNode):
        # Set the distance and path arrays.
        distance = [99 for d in range(len(LocationNavigation.locations))]
        path = []
        # Set the startNode distance in the array to be 0 
        distance[startNode.getValue()] = 0
        # NOTE: path can also be used to track which nodes have already been 
        #  visited and fulfills our need for a visited node.
       
        node = startNode # This is the node we manipulate in the while loop and we begin with the startNode

        # We then start the while loop:
        while (len(nodeList) != 0):
            # The first thing to do with startnode is to get and store its
            # neighbours.
            neighbours = node.getNeighbours() # An array of startNode's neighbours
           
            # Now that we have the neighbours, we can travel to each of the neighbouring
            # nodes and see which one has the smaller weight.
            ultraweight = 0
            nextNode = node
            index = 0
            
            for x in neighbours:
                index = x.getValue()
                if(index != 0):
                    weight = x.getWeight()
                    if(weight <  ultraweight) and (x in nodeList):
                        ultraweight = weight
                        nextNode = x
                else:
                    ultraweight = x.getWeight()
            
            distance[index] = weight
            # Now we get node into the path and out of nodeArray

            for x in nodeList:
                if x == node:
                    nodeList.remove(x)
                    path.append(x)

            # We then update startnode to be the nextNode
            node = nextNode
        
        return path





        

    

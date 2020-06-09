import sys
from LocationNode import LocationNode
from Graph import Graph
from queue import Queue
# This is the class that is used to create functionality and add functionality to the 
# Application class. It controls how the functionality of the application works.
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
        node = LocationNode(name, LocationNavigation.index) # Add the node
        # Set the nodes Neighbours and Weights
        node.setNeighbours(neighbours)
        node.setWeights(weights)
        # Add the node to the locations graph.
        LocationNavigation.locations.append(node)
        LocationNavigation.index+=1 # increment the index by one
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
    # multiple nodes and returns an array of the locations to be used between the 
    # nodes to return the shortest possible path.
    # -----------------------------------------------------------------------
    # PARAMS: nodeList(array): The list of selected nodes.
    #         startNode(LocationNode): The node from which we  
    # RETURN: A list containing the shortest path of nodes to the end path
    def findShortestPath(self, nodeList, startNode):
        # Set the distance and path arrays.
        self.distance = [0 for d in range(len(LocationNavigation.locations))]
        path = []
        # Set the startNode distance in the array to be 0 
        #self.distance[startNode.getValue()] = 0
        
        # NOTE: path can also be used to track which nodes have already been 
        #  visited and fulfills our need for a visited node.
       
        node = startNode # This is the node we manipulate in the while loop and we begin with the startNode

        # Now that we have the neighbours, we can travel to each of the neighbouring
        # nodes and see which one has the smaller weight.
        ultraweight = 0
        nextNode = node
        index = 0
            
        # We then start the while loop:
        while (len(nodeList) != 0):
            # The first thing to do with startnode is to get and store its
            # neighbours.
            neighbours = node.getNeighbours() # An array of startNode's neighbours
           
            if(len(neighbours) > 0):
                if(len(neighbours) == 1):
                    ultraweight = neighbours[0].getWeight(0)
                else:
                    for y in neighbours:
                        if(y != -1):
                            if (y in nodeList):
                                index = neighbours.index(y)  
                                ultraweight = neighbours[index].getWeight(index)
                            elif(len(nodeList) == 1):
                                index = neighbours.index(y)  
                                ultraweight = neighbours[index].getWeight(index + 1)
                for x in neighbours:
                    if(x != -1):
                        index = neighbours.index(x)
                        if(index >= 0):
                            weight = x.getWeight(index)
                            # and (x in nodeList)
                            if((int(weight) <= int(ultraweight))and (int( weight ) > -1)):
                                ultraweight = weight
                                nextNode = x         
            self.distance[index] = ultraweight
            # Now we get node into the path and out of nodeArray

            for x in nodeList:
                if x == node:
                    nodeList.remove(x)
                    path.append(x)

            # We then update startnode to be the nextNode
            node = nextNode
            if ((nextNode not in nodeList) and (len(nodeList) == 1)):
                return None
        return path

    # This is the shortest path time that can be calculated and the means of the 
    # transport and the way that the user should travel for the most efficient 
    # ETA.
    # ___________________________________________________________________________
    # PARAMS: 
    # meansOfTransport(int): A value that indicates whether the user will be traveling by bus or car.
    # nodeList(list): The list of nodes to be used in findShortestPath to calculate distance
    # startNode(Node): The starting node of the list.              
    # RETURN : An integer value containing the time taken
    def shortestPathTime(self, meansOfTransport, nodeList, startNode):
        distance = 0 # The distance required to be travelled
        timeTaken = 0 # The total time taken
        # Calculating the distance.
        for x in self.distance:
            distance = distance + int(x)
        if(meansOfTransport == 0):
            # This calculates the time it would take by walk. The average walking speed is
            # 3 - 4 miles per hour.
            timeTaken = distance/4
        if(meansOfTransport == 1):
            # This calculates the time it would take by bike. The average biking speed is
            # 3 - 4 miles per hour.
            timeTaken = distance/9
        if(meansOfTransport == 2):
            # This calculates the time it would take by car. The average car speed is
            # 25 miles per hour.
            timeTaken = distance/25
        return timeTaken
    
    # This function is used to find the shortest path between two locations
    # using the BFS Shortest Path Algorithm. It then returns a queue containing
    # the shortest path.
    # ----------------------------------------------------------------------
    # PARAMS: 
    #       startNode : The beginning node from which we will iterate
    #
    # RETURN : The shortest path in a queue

    def BFSfunction(self, startNode, endNode):
        # To execute this algorithm, we will need a queue + a list
        # for visiting nodes
        # We can start by adding our current node to the queue.
        queue = [[startNode]]
        visited = []
        path = []
        # While the queue is not empty:
        while(queue):
            # If it is the node we are looking for: 
            #if(node == endNode):
            #    return queue
            # pop the beginning of the queue
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                # Get the neighbours of the node
                neighbours = node.getNeighbours()
                # Iterate through neighbours
                for x in neighbours:
                    if x != -1:
                       # We add x to visited and queue
                        newpath = list(path)
                        newpath.append(x)
                        queue.append(newpath)
                        if (x == endNode):
                            return newpath
                #mark node as explored
                visited.append(node)

        # If we get to this point then we cannot use this

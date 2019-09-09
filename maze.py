import random
import time

#properties for each mazeNode
class mazeNode:
    def __init__(self):
        self.path=False
        self.visited=0

class mazeManager:
    def __init__(self, size, time):
        self.mazeNodes = [[mazeNode() for i in range(mazeSize)] for j in range(mazeSize)]
        self.size = size
        self.time = time

    def getValidNeighbors(self, cords) -> list:
        neighbors = list()
        if int(cords[1])+1 < self.size and self.mazeNodes[cords[0]][cords[1]+1].visited <= 1:
            neighbors.append([cords[0], cords[1]+1])
        if int(cords[0])+1 < self.size and self.mazeNodes[cords[0]+1][cords[1]].visited <= 1:
            neighbors.append([cords[0]+1, cords[1]])
        if int(cords[1])-1 >= 0 and self.mazeNodes[cords[0]][cords[1]-1].visited <= 1:
            neighbors.append([cords[0], cords[1]-1])
        if int(cords[0])-1 >= 0 and self.mazeNodes[cords[0]-1][cords[1]].visited <= 1:
            neighbors.append([cords[0]-1, cords[1]])
        return neighbors

    def incrementAllNeighbors(self, cords):
        if int(cords[1])+1 < self.size:
            self.mazeNodes[cords[0]][cords[1]+1].visited += 1
        if int(cords[1])-1 >= 0:
            self.mazeNodes[cords[0]][cords[1]-1].visited += 1
        if int(cords[0])+1 < self.size:
            self.mazeNodes[cords[0]+1][cords[1]].visited += 1
        if int(cords[0])-1 >= 0:
            self.mazeNodes[cords[0]-1][cords[1]].visited += 1

    def getNode(self, cords) -> mazeNode:
        return self.mazeNodes[cords[0]][cords[1]]


    def generateMaze(self):
        buildStep = 0
        curr = [0, 0] #y, x
        stack = [] #append to add, pop to remove
        self.getNode(curr).path = True
        self.getNode(curr).visited = 2
        currentNeighbors = self.getValidNeighbors(curr)
        stack.append(curr)
        self.incrementAllNeighbors(curr)

        buildStep+=1
        time.sleep(self.time)
        print("building step: " + str(buildStep))
        self.printMaze('#', ' ')

        while(len(stack)>0):
            while( len(currentNeighbors) != 0 ):
                #push to stack
                stack.append(curr)
                #get random new
                curr = random.choice(currentNeighbors)
                #increment on the new choice
                self.incrementAllNeighbors(curr)
                #set new path to true
                self.getNode(curr).path = True
                self.getNode(curr).visited = 2
                #get new neighbors!
                currentNeighbors = self.getValidNeighbors(curr) 

                buildStep+=1
                time.sleep(self.time)
                print("building step: " + str(buildStep))
                self.printMaze('#', ' ')
            
            curr = stack.pop()
            currentNeighbors = self.getValidNeighbors(curr)

    def printMaze(self, c1: chr, c2: chr):
        for i in self.mazeNodes:
            curLine=""
            for j in i:
                if j.path:
                    curLine+=c1
                else:
                    curLine+=c2
            print(curLine)


#get size of maze
print("Maze size?")
mazeSize = int(input())
print("Time inbetween steps? (in seconds)")
mazeTime = float(input())

#initialize mazeManger
mazeInstance = mazeManager(mazeSize, mazeTime)

#generate maze
mazeInstance.generateMaze()

#print maze
print("ITS DONE")
mazeInstance.printMaze(' ', '!')


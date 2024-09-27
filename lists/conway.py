#Conway's Game of Life

import random, time, copy

WIDTH = 60
HEIGHT = 20

#Create a list of list for the cells
nextCells = []

for x in range(WIDTH):
    column = [] #Creates new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0: #Randint is a modifier that picks from the range of numbers
            column.append('#') #Add a living cell
        else:
            column.append(' ') #Add a dead cell
    nextCells.append(column) #Nextcells is a list of column lists

while True:
    print('\n\n\n\n\n') #Each step is separated with newlines
    currentCells = copy.deepcopy(nextCells)
    #Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') #Print the # or space.
        print() #Prints new line at the end of the row
    #Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighboring coordinates
            #`% WIDTH` ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            # Count the number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 #Top-Left Neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 #Top Neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1
            #Set cell based on Conway's rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
    time.sleep(1)


                



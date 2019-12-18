#conway's Game of Life
import random, time, copy
WIDTH=60
HEIGHT=20

#create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = []   #create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')   #Add a living Cell
        else:
            column.append(' ')   #Add a dead Cell
    nextCells.append(column)     #next cells is a list of column lists

while True:   #main program loop
    print('\n\n\n\n\n')   #Seperate each step with newlines
    currentCells = copy.deepcopy(nextCells)

    #Print current cells on the screen 
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')  #print the # or space
        print()                       #print a newline at the end of new row

    #calculate the next step's cell based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get neighboring coordinates
            #%Width ensures leftcord is always between 0 and width -1      
            leftCoord = (x - 1 ) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            #count number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord]=='#':
                  numNeighbors += 1 #Top-left neighbor is alive
            if currentCells[x][aboveCoord]=='#':
                  numNeighbors += 1 #Top neighbor is alive
            if currentCells[rightCoord][aboveCoord]=='#':
                  numNeighbors += 1 #Top-right neighbor is alive 
            if currentCells[leftCoord][y]=='#':
                  numNeighbors += 1 #Left neighbor is alive
            if currentCells[rightCoord][y]=='#':
                  numNeighbors += 1 #Right neighbor is alive
            if currentCells[leftCoord][belowCoord]=='#':
                  numNeighbors += 1 #Bottom-left neighbor is alive
            if currentCells[x][belowCoord]=='#':
                  numNeighbors += 1 #Bottom neighbor is alive
            if currentCells[rightCoord][belowCoord]=='#':
                  numNeighbors += 1 #Bottom-right neighbor is alive

            #Set cells based on Conway's Game of Life Rules  
            if currentCells[x][y]=='#' and (numNeighbors == 2 or numNeighbors == 3):
                  #Living cells with 2 or 3 neigbors stay alive
                  nextCells[x][y] = '#' 
            elif currentCells[x][y]==' ' and numNeighbors == 3:
                #dead cells with 3 neighbors become alive
                  nextCells[x][y] = '#'
            else:
                #Everything else dies or stays dead:
                nextCells[x][y] = ' '

time.sleep(1) #Add a 1-second pause top reduce flickering

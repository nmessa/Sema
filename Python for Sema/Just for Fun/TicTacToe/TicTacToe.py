##Lab Exercise 11.3.2023
##Author: nmessa
##File: TicTacToe.py
#improved drawing location of X's and O's

import pygame, time

#This function will draw an X at a specified location
def drawX(x, y):
    #create a map for drawing 25 rectangles
    #1 = black rectangle
    #0 = white rectangle
    x_list = [[1,0,0,0,1],
              [0,1,0,1,0],
              [0,0,1,0,0],
              [0,1,0,1,0],
              [1,0,0,0,1]]
    #set height and width of rectangles
    width = 30
    height = 30

    #store the original x value
    ex = x

    #draw a 5 x 5 array of 30 pixel x 30 pixel rectangles
    for row in range(5):
        for col in range(5):
            #determine if rectangle is going to be red or white
            if x_list[row][col]:
                color = [255,0,0]
            else:
                color = [255, 255, 255]
            #draw the rectangle
            pygame.draw.rect(screen, color, [x,y, width, height])
            #update x position for next rectangle
            x += width
        #update y position for next row of rectangles
        y += height
        #reset x position for next row
        x = ex

#This function will draw an O at a specified location
def drawO(x, y):
    o_list = [[0,0,1,0,0],
              [0,1,0,1,0],
              [1,0,0,0,1],
              [0,1,0,1,0],
              [0,0,1,0,0]]
    width = 30
    height = 30
    ex = x
    for row in range(5):
        for col in range(5):
            if o_list[row][col]:
                color = [0,255,0]
            else:
                color = [255, 255, 255]
            pygame.draw.rect(screen, color, [x,y, width, height])
            x += width
        y += height
        x = ex

def drawLines():
    #Draw lines for Tic-Tac-Toe board
    pygame.draw.line(screen, [0,0,0],[0,200], [600, 200])
    pygame.draw.line(screen, [0,0,0],[0,400], [600, 400])
    pygame.draw.line(screen, [0,0,0],[200,0], [200, 600])
    pygame.draw.line(screen, [0,0,0],[400,0], [400, 600])
    pygame.display.flip()
    
def showState():
    #this function is used for testing
    for i in range(3):
        for j in range(3):
            print(state[i][j], end = ' ')
        print()

def resetState():
    for i in range(3):
        for j in range(3):
            state[i][j] = 0
            
def resetGame():
    resetState()
    screen.fill((255, 255, 255))
    drawLines()
    turn = 0
    quit = False

#This function determines if a win has occured and which player won
#This is done by checking the contents of the state array
def checkWin():
    #column 1
    if state[0][0] == state[1][0] and state[1][0] == state[2][0]:
        if state[0][0] + state[1][0] + state[2][0] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[100,0], [100, 600], 10)
            return True
        elif state[0][0] + state[1][0] + state[2][0] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[100,0],[100, 600], 10)
            return True

    #column 2
    if state[0][1] == state[1][1] and state[1][1] == state[2][1]:
        if state[0][1] + state[1][1] + state[2][1] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[300,0], [300, 600], 10)
            return True
        elif state[0][1] + state[1][1] + state[2][1] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[300,0], [300, 600], 10)
            return True

    #column 3
    if state[0][2] == state[1][2] and  state[1][2] == state[2][2]:
        if state[0][2] + state[1][2] + state[2][2] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[500,0], [500, 600], 10)
            return True
        elif state[0][2] + state[1][2] + state[2][2] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[500,0], [500, 600], 10)
            return True

    #row 1
    if state[0][0] == state[0][1] and state[0][1] == state[0][2]:
        if state[0][0] + state[0][1] + state[0][2] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[0,100], [600, 100], 10)
            return True
        elif state[0][0] + state[0][1] + state[0][2] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[0,100], [600, 100], 10)
            return True

    #row 2
    if state[1][0] == state[1][1] and state[1][1] == state[1][2]:
        if state[1][0] + state[1][1] + state[1][2] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[0,300], [600, 300], 10)
            return True
        elif state[1][0] + state[1][1] + state[1][2] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[0,300], [600, 300], 10)
            return True

    #row 3
    if state[2][0] == state[2][1] and state[2][1] == state[2][2]:
        if state[2][0] + state[2][1] + state[2][2] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[0,500], [600, 500], 10)
            return True
        elif state[2][0] + state[2][1] + state[2][2] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[0,500], [600, 500], 10)
            return True

    #diagonal 1
    if state[0][0] == state[1][1] and state[1][1] == state[2][2]:
        if state[0][0] + state[1][1] + state[2][2] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[0,0], [600, 600], 10)
            return True
        elif state[0][0] + state[1][1] + state[2][2] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[0,0], [600, 600], 10)
            return True

    #diagonal 2
    if state[2][0] == state[1][1] and state[1][1] == state[0][2]:
        if state[2][0] + state[1][1] + state[0][2] == 3:
            #Player X won
            pygame.draw.line(screen, [255,0,0],[0,600], [600, 0], 10)
            return True
        elif state[2][0] + state[1][1] + state[0][2] == 6:
            #Player O won
            pygame.draw.line(screen, [0,255,0],[0,600], [600, 0], 10)
            return True
    return False #Game not yet won
        
#initialize pygame    
pygame.init()

#set counter to keep track of whose turn
turn = 0

#keep track of state of board - used to check who won
state = [[0,0,0], [0,0,0], [0,0,0]]

#set the drawing screen to 600 x 600
screen = pygame.display.set_mode([600,600])
pygame.display.set_caption("Tic-Tac_Toe")

#fill the screen with white
screen.fill([255, 255, 255])

#draw the lines for the tic-tac-toe board
drawLines()

#Create flag variable for ending game loop
quit = False

#Game loop
while not quit:
    #Check all pygame events
    for event in pygame.event.get():
        #quit event
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        #KEYDOWN events
        elif event.type == pygame.KEYDOWN:
            #clear board event
            if event.key == pygame.K_c:
                resetState()
                screen.fill((255, 255, 255))
                drawLines()
                turn = 0
            #display the state of board
            elif event.key == pygame.K_s:
                showState()
        #MOUSEBUTTON event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                #get position of mouse click and conver to list
                pos = list(pygame.mouse.get_pos())
                
                #Determine row and column selected
                row = pos[1]//200
                col = pos[0]//200
                
                #Adjust x position to properly position X or O
                if pos[0] < 200:
                    pos[0] = 20
                elif pos[0] < 400:
                    pos[0] = 220
                else:
                    pos[0] = 420
                    
                #Adjust y position to properly position X or O
                if pos[1] < 200:
                    pos[1] = 20
                elif pos[1] < 400:
                    pos[1] = 220
                else:
                    pos[1] = 420
                
                #update turn for next player
                if state[row][col] != 0:
                    continue
                turn += 1

                #Player turn
                #draw X or O
                #Update state array
                #Check for win
                if turn%2:
                    drawX(pos[0], pos[1])
                    state[row][col] = 1
                    if checkWin():
                        quit = True
                else:
                    drawO(pos[0], pos[1])
                    state[row][col] = 2
                    if checkWin():
                        quit = True

                #update display
                pygame.display.flip()

time.sleep(4)
pygame.display.quit()
            

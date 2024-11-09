#Game of Nims
#Author: nmessa
#The game of Nims

def playNims(pile, max):
    print ("There are", pile, "stones")
    print ("You may choose up to", max, "stones")
    while pile > 0:
        isValid = False
        win1 = False
        win2 = False
        
        #loop until both player1 and player2 have made valid moves
        while not isValid and not win1 and not win2: 
            player1 = int(input("Player 1: How many stones do you wish to take? "))
            if player1 <= max and player1 <= pile:
                pile -= player1
                if pile == 0:
                    win1 = True
                    break
                else:
                    print (pile, "stones left")
            else:
                break
            player2 = int(input("Player 2: How many stones do you wish to take? "))
            if player2 <= max and player2 <= pile:
                pile -= player2
                if pile == 0:
                    win2 = True
                    break
                else:
                    print (pile, "stones left")
            else:
                break
    if win1:
        print ("Player 1 wins")
    if win2:
        print ("Player 2 wins")
        
playNims(10, 3)

##Sample Output
##There are 10 stones
##You may choose up to 3 stones
##Player 1: How many stones do you wish to take? 3
##7 stones left
##Player 2: How many stones do you wish to take? 3
##4 stones left
##Player 1: How many stones do you wish to take? 1
##3 stones left
##Player 2: How many stones do you wish to take? 3
##Player 2 wins


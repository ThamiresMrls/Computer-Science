#Yeaaahhhh, everything works. The only thing that doesn't work 
#entirely is the end. somehow it always manages to inform 
#the player who has won, and correctly too, but it never really
#knows that it is time to stop. well, it does, but not really on 
#time. When /either/ x or o wins, it decides to give x a bunch
#more turns, until x wins again (or maybe just 
#arbitrarily). Not really very fair. The returns obviously arent 
#working somehow.
#i=row
#e=column.
#for horizontal.
#Working.
def winnertest1(p):
    for i in range(6):
        for e in range(4):
            if board[i][e]==p and board[i][e+1]==p and board[i][e+2]==p and board[i][e+3]==p:
                return True
    return False
#for vertical
#working.
def winnertest2(p):
    for e in range(7):
        for i in range(3):
            if board[i][e]==p and board[i+1][e]==p and board[i+2][e]==p and board[i+3][e]==p:
                return True
    return False
#for diagonal
#working! for right to left diagonal.
def winnertest3(p):
    for i in range(3):
        for e in range(4):
            if board[i][e]==p and board[i+1][e+1]==p and board[i+2][e+2]==p and board[i+3][e+3]==p:
                return True
    return False
#diagonal going other way
#not working! WHYYY
def winnertest4(p):
    for i in range(3):
        for e in range(3,6,4):
            if board[i][e]==p and board[i+1][e-1]==p and board[i+2][e-2]==p and board[i+3][e-3]==p:
                return True
    return False
def test(p):
    if winnertest1(p):
        print p, "Wins!!!"
        return True
    elif winnertest2(p):
        print p, "Wins!!!"
        return True
    elif winnertest3(p):
        print p, "Wins!!!"
        return True
    elif winnertest4(p):
        print p, "Wins!!!"
        return True
    else:
        return False
#prints the board.
def print_board():
    print board[0]
    print board[1]
    print board[2]
    print board[3]
    print board[4]
    print board[5]
#create the board.
#This could be modularized so you can define the size 
#of the board, but why do that, really.
board = [
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
]
#
def drop(col):
    if col=='a':
        return 0,'a'
    elif col=='b':
        return 1,'b'
    elif col=='c':
        return 2,'c'
    elif col=='d':
        return 3,'d'
    elif col=='e':
        return 4,'e'
    elif col=='f':
        return 5,'f'
    elif col=='g':
        return 6,'g'
    else:
        print "That's not a column"
def change_board(y,n,p):
    if board[5][y]==n:
        board[5][y]=p
    elif board[4][y]==n:
        board[4][y]=p
    elif board[3][y]==n:
        board[3][y]=p
    elif board[2][y]==n:
        board[2][y]=p
    elif board[1][y]==n:
        board[1][y]=p
    elif board[0][y]==n:
        board[0][y]=p
    else:
        print "Sorry, that column is full"
        turn(p)
print "Let's play connect 4!"
#p is the player that is playing.
#it's a string, either 'X' or 'O'
def turn(p):
    print_board()
    print p,": It's your turn!"
    x = raw_input("Where would you like to go? ")
    #check where the player wants to go. 
    #if it's the a column, pass a to the drop 
    #function. that will convert the column
    #into a tuple, then pass that tuple, plus the player 
    #variable, to change board, which will
    #check how many pieces have been played 
    #in that column already. then it changes 
    #the board based on that. n is the 
    #name of the column, and y is the number
    #of the column.
    if x=='a':
        y,n=drop('a')
        change_board(y,n,p)
    elif x=='b':
        y,n=drop('b')
        change_board(y,n,p)
    elif x=='c':
        y,n=drop('c')
        change_board(y,n,p)
    elif x=='d':
        y,n=drop('d')
        change_board(y,n,p)
    elif x=='e':
        y,n=drop('e')
        change_board(y,n,p)
    elif x=='f':
        y,n=drop('f')
        change_board(y,n,p)
    elif x=='g':
        y,n=drop('g')
        change_board(y,n,p)
    else:
        print "Sorry, that's not a column"
        turn(p)
#game='on'
##############################
#I know this is not a good way to 
#implement it, but it's not the
#point right now. --Daniel.
#############################
def game():
    while True:
        turn('X')
        if not test('X'):
            turn('O')
            if not test('O'):
                game()
            else:
                return
        else:
            return
game()

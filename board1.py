#i=row
#e=column.
#for horizontal.
#Working.
#All of the gameplay is working, but the tests are...
#some are working, some arent. 
def winnertest1():
    i=0
    while i<6:
        for e in range(0,4):
            if board[i][e]=='x' and board[i][e+1]=='x' and board[i][e+2]=='x' and board[i][e+3]=='x':
                print "x wins!!!!"
                return 'over'
        i+=1
    return 'on'
#for vertical
#working.
def winnertest2():
    e=0
    while e<7:
        for i in range(3):
            if board[i][e]=='X' and board[i+1][e]=='X' and board[i+2][e]=='X' and board[i+3][e]=='X':
                print "X wins!!!!"
                return 'over'
        e+=1
    return 'on'
#for diagonal
#not working! WHYYYY
def winnertest3():
    i=2
    while i!=-1:
        for e in range(4):
            print i,e
            if board[i][e]=='X' and board[i+1][e+1]=='X' and board[i+2][e+2]=='X' and board[i+3][e+3]=='X':
                print "X wins!!!!"
                return 'over'
        i-=1
    return 'on'
#diagonal going other way
#not working! WHYYY
def winnertest4():
    i=2
    while i!=-1:
        for e in range(3,6):
            if board[i][e]=='X' and board[i+1][e-1]=='X' and board[i+2][e-2]=='X' and board[i+3][e-3]=='X':
                print "X wins!!!!"
                return 'over'
        i+=1
    return 'on'
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
game='on'
##############################
#I know this is not a good way to 
#implement it, but it's not the
#point right now. --Daniel.
#############################
while not game=='over':
    turn('X')
    game=winnertest3()
    turn('O')
    game=winnertest3()

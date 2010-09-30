#i=row
#the idea here is to test for a winner, in the horizontal direction.
#iterate through the rows, then go through the columns. if there are 
#four in a row, break and make x the winner
###
###
#so this right now works for any row, four in a row horizontally. 
#sadly, it only works if the four in a row starts at a. Why? No
#idea. It has a try except in it though!
#added a comment.
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
#basically the same as the first test
def winnertest2():
    e=0
    while e<5:
        for i in range(0,1):
            try:
                if board[i][e]=='x' and board[i+1][e]=='x' and board[i+2][e]=='x' and board[i+3][e]=='x':
                    print "x wins!!!!"
                    return 'over'
                else:
                    e+=1
                    break
            except ValueError:
                pass

#for diagonal
def winnertest3():
    i=0
    while i<4:
        for e in range(0,3):
            if board[i][e]=='x' and board[i+1][e+1]=='x' and board[i+2][e+2]=='x' and board[i+3][e+3]=='x':
                print "x wins!!!!"
                return 'over'
            else:
                i+=1
                break
#diagonal going other way
def winnertest4():
    i=0
    while i<4:
        for e in range(3,6):
            if board[i][e]=='x' and board[i+1][e-1]=='x' and board[i+2][e-2]=='x' and board[i+3][e-3]=='x':
                print "x wins!!!!"
                return 'over'
                break
            i+=1
#prints the board.
def print_board():
    print board[0]
    print board[1]
    print board[2]
    print board[3]
    print board[4]
    print board[5]
#create the board.
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
def turn(p):
    print_board()
    print p,": It's your turn!"
    x = raw_input("Where would you like to go? ")
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
# game=winnertest1()
#right now, just trying to get the first test to work.
while not game=='over':
    turn('x')
    winnertest1()
    game=winnertest1()
    turn('o')
    winnertest1()
    game=winnertest1()

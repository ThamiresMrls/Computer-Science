#adding the computer program
#i=row 0 is the top
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
def winnertest2(p):
    for e in range(7):
        for i in range(3):
            if board[i][e]==p and board[i+1][e]==p and board[i+2][e]==p and board[i+3][e]==p:
                return True
    return False


#for right to left diagonal.
def winnertest3(p):
    for i in range(3):
        for e in range(4):
            if board[i][e]==p and board[i+1][e+1]==p and board[i+2][e+2]==p and board[i+3][e+3]==p:
                return True
    return False


#diagonal going other way
def winnertest4(p):
    for i in range(3):
        for e in range(3,6,4):
            if board[i][e]==p and board[i+1][e-1]==p and board[i+2][e-2]==p and board[i+3][e-3]==p:
                return True
    return False

def tietest():
    if not board[0][0]=='z' and not board[0][1]=='z' and not board[0][2]=='z' and not board[0][3]=='z' and not board[0][4]=='z' and not board[0][5]=='z' and not board[0][6]=='z':
        return True
    else:
        return False


#groups all the tests into one.
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
    elif tietest():
        print "Sigh, it's a tie"
        return True
    else:
        return False


#prints the board.
def print_board():
    for i in range(6):
        print board[i]
    print array


def drop(col):
    if col=='a':
        return 0
    elif col=='b':
        return 1
    elif col=='c':
        return 2
    elif col=='d':
        return 3
    elif col=='e':
        return 4
    elif col=='f':
        return 5
    elif col=='g':
        return 6
    else:
        print "That's not a column"
        turn(p)


def change_board(y,p):
    if board[5][y]=='z':

        board[5][y]=p
    elif board[4][y]=='z':
        board[4][y]=p
    elif board[3][y]=='z':
        board[3][y]=p
    elif board[2][y]=='z':
        board[2][y]=p
    elif board[1][y]=='z':
        board[1][y]=p
    elif board[0][y]=='z':
        board[0][y]=p
    else:
        print "Sorry, that column is full"
        turn(p)


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
        y=drop('a')
        change_board(y,p)
    elif x=='b':
        y=drop('b')
        change_board(y,p)
    elif x=='c':
        y=drop('c')
        change_board(y,p)
    elif x=='d':
        y=drop('d')
        change_board(y,p)
    elif x=='e':
        y=drop('e')
        change_board(y,p)
    elif x=='f':
        y=drop('f')
        change_board(y,p)
    elif x=='g':
        y=drop('g')
        change_board(y,p)
    else:
        print "Sorry, that's not a column"
        turn(p)

def players():
    w=input('1 or 2 players?')
    if w==1:
        q=raw_input('Would you like to go first or second?')
        if q=='first':
            game2()
        if q=='second':
            game1()
        else:
            print "Please specify first or second"
            players()
    if w==2:
        hgame()
    else:
        print "Not a valid number"
        players()

def move(r):
    if r==1:
        v='O'
        p='X'
    else:
        v='X'
        p='O'
    for i in range(6):
        for e in range(4):
            if board[i][e]==v and board[i][e+1]==v and board[i][e+2]==v and board[i][e+3]=='z':
                return i,p

    for e in range(7):
        for i in range(3):
            if e!=0:
                if board[i][e]==v and board[i+1][e]==v and board[i+2][e]==v and not board[i+3][e-1]=='z':
                    return i,p
            else:
                if board[i][e]==v and board[i+1][e]==v and board[i+2][e]==v:
                    return i,p
    #etc.
    else:
        return 3,p


def game1():
    y,p=move(1)
    change_board(y,p)
    if not test('X'):
        turn('O')
        if not test('O'):
            game1()
        else:
            print_board()
            print "Good game"
    else:
        print_board()
        print "Good game"


def game2():
    turn('X')
    if not test('X'):
        y,p=move(2)
        change_board(y,p)
        if not test('O'):
            game2()
        else:
            print_board()
            print "Good game"
    else:
        print_board()
        print "Goo d game"

def hgame():
    turn('X')
    if not test('X'):
        turn('O')
        if not test('O'):
            hgame()
        else:
            print_board()
            print "Good game"
    else:
        print_board()
        print "Good game"


#create the board.
#This could be modularized so you can define the size 
#of the board, but why do that, really.
board = [
['z','z','z','z','z','z','z'],
['z','z','z','z','z','z','z'],
['z','z','z','z','z','z','z'],
['z','z','z','z','z','z','z'],
['z','z','z','z','z','z','z'],
['z','z','z','z','z','z','z'],
]

array = ['a','b','c','d','e','f','g']

print "Let's play connect 4!"
players()

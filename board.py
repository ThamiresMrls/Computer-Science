def print_board():
    print board[0]
    print board[1]
    print board[2]
    print board[3]
    print board[4]
    print board[5]
    print board[6]
board = [
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
['a','b','c','d','e','f','g'],
]
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
    if board[6][y]==n:
        board[6][y]=p
    elif board[5][y]==n:
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
    print p,":It's your turn!"
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
def winnertest():
    if board[6][0]=='x' and board[6][1]=='x' and board[6][2]=='x':
        return 'x'
end_game=winnertest()
while not end_game=='x':
    turn('x')
    end_game=winnertest()
    turn('o')
    end_game=winnertest()
print "x wins!!!!"

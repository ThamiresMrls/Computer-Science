def print_board():
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
def change_board(y,n):
    if board[6][y]==n:
        board[6][y]='x'
    elif board[5][y]==n:
        board[5][y]='x'
    elif board[4][y]==n:
        board[4][y]='x'
    elif board[3][y]==n:
        board[3][y]='x'
    elif board[2][y]==n:
        board[2][y]='x'
    elif board[1][y]==n:
        board[1][y]='x'
    elif board[0][y]==n:
        board[0][0]='x'
    else:
        print "Sorry, that row is full"
print_board()
while True:
    x = raw_input("Where would you like to go? ")
    if x=='a':
        y,n=drop('a')
        change_board(y,n)
    elif x=='b':
        y,n=drop('b')
        change_board(y,n)
    elif x=='c':
        y,n=drop('c')
        change_board(y,n)
    elif x=='d':
        y,n=drop('d')
        change_board(y,n)
    elif x=='e':
        y,n=drop('e')
        change_board(y,n)
    elif x=='f':
        y,n=drop('f')
        change_board(y,n)
    else:
        y,n=drop('g')
        change_board(y,n)
    print_board()

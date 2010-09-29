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
print_board()
x = raw_input("Where would you like to go? ")
if x=='a':
    board[6][0]='x'
elif x=='b':
    board[6][1]='x'
elif x=='c':
    board[6][2]='x'
elif x=='d':
    board[6][3]='x'
elif x=='e':
    board[6][4]='x'
elif x=='f':
    board[6][5]='x'
else:
    board[6][6]='x'
print_board()

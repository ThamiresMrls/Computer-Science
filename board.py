#while True:
def print_board():
    print board[1]
    print board[2]
    print board[3]
    print board[4]
    print board[5]
    print board[6]
board = [['a','b','c','d','e','f','g']]*7
print_board()
#a=None
#x = raw_input("Where would you like to go? ")
#if x==a:
board = ['x' for item in board]
print_board()

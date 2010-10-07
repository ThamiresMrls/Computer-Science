#this is rock paper scissors lizard spock.
def rock(move2):
    if move2=="lizard" or move2=="scissors":
        print "rock crushes lizard!"
        print "player 1 wins!"
    else:
        print "player 2 wins!"
def paper(move2):
    if move2=="rock" or move2=="spock":
        print "player 1 wins!"
    else:
        print "player 2 wins!"
def scissors(move2):
    if move2=="paper" or move2=="lizard":
        print "player 1 wins!"
    else:
        print "player 2 wins!"
def lizard(move2):
    if move2=="spock" or move2=="paper":
        print "player 1 wins!"
    else:
        print "player 2 wins!"
def spock(move2):
    if move2=="rock" or move2=="scissors":
        print "player 1 wins!"
    else:
        print "player 2 wins!"
def compare(move, move2):
    if move=="rock":
        rock(move2)
    elif move=="paper":
        paper(move2)
    elif move=="scissors":
        scissors(move2)
    elif move=="lizard":
        lizard(move2)
    elif move=="spock":
        spock(move2)
    else:
        print "Someone's move was not legal, start over. maybe a typo?"
        play()
def play():
    move=raw_input("Player 1:Rock Paper Scissors Lizard Spock? ")
    move=move.lower()
    move2=raw_input("Player 2: Rock Paper Scissors Lizard Spock? ")
    move2=move2.lower()
    compare(move,move2)
play()

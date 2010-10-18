#this is rock paper scissors lizard spock.
import random
def cheatmode():
    #cheat mode!
    # get a random number between 0 and a hundred, 
    # if it's under 40, cheat!
    cheat=random.randint(0,100)
    if cheat <40:
        return "cheat"
    else:
        return "nocheat"
def rock(move2):
    #if player 1 is rock, then he beats lizard and scissors, 
    #but loses in all other cases. he ties if player 2 is rock as 
    #well. All the other functions up here work the same way.
    if move2=="lizard" or move2=="scissors":
        print "player 1 wins!"
    elif move2=="rock":
        print "OMG TIE"
        game()
    else:
        print "player 2 wins!"
def paper(move2):
    if move2=="rock" or move2=="spock":
        print "player 1 wins!"
    elif move2=="paper":
        print "OMG TIE"
        game()
    else:
        print "player 2 wins!"
def scissors(move2):
    if move2=="paper" or move2=="lizard":
        print "player 1 wins!"
    elif move2=="scissors":
        print "OMG TIE"
        game()
    else:
        print "player 2 wins!"
def lizard(move2):
    if move2=="spock" or move2=="paper":
        print "player 1 wins!"
    elif move2=="lizard":
        print "OMG TIE"
        game()
    else:
        print "player 2 wins!"
def spock(move2):
    #if player 1 is spock, there is a chance he just pwns everything as well.
    #i think there is a slight advantage for player two, because if cheat mode 
    #is on and spock gets god powers, it doesnt matter if player one is spock 
    #with god powers as well. That's a feature though, not a bug.
    cheat="nocheat"
    cheat=cheatmode()
    if cheat=="cheat":
        print "Player one's spock vaporized whatever player two decided on"
    else:
        if move2=="rock" or move2=="scissors":
            print "player 1 wins!"
        elif move2=="spock":
            print "OMG TIE"
            game()
        else:
            print "player 2 wins!"
def compare(move, move2, p):
    #if player two is spock, there is chance he just pwns everything.
    if move2=="spock":
        cheat="nocheat"
        cheat=cheatmode()
        if cheat=="cheat":
            print "player two's spock vaporized wahtever player one decided on"
            return
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
        if p==1:
            print "Your move was not legal. Please input rock paper scissors lizard or spock"
            play1()
        elif p==2:
            print "Someone's move was not legal, start over. maybe a typo?"
            play2()
def play1():
    #play one player. get an input for player 1, then choose the
    #input for player two randomly from a list of options.
    move=raw_input("Player 1:Rock Paper Scissors Lizard Spock? ")
    move=move.lower()
    move2=random.choice(["rock", "paper", "scissors", "lizard", "spock"])
    print 'player 2 threw', move2
    compare(move,move2,1)
def play2():
    #play two players. get inputs for both players one and two, then compare 'em.
    move=raw_input("Player 1:Rock Paper Scissors Lizard Spock? ")
    move=move.lower()
    move2=raw_input("Player 2: Rock Paper Scissors Lizard Spock? ")
    move2=move2.lower()
    compare(move,move2,2)
def game():
    players=raw_input("How many players?(1 or 2) ")
    try:
        players=int(players)
    except ValueError:
        print "input a number please"
        game()
    if players==1:
        play1()
    elif players==2:
        play2()
game()

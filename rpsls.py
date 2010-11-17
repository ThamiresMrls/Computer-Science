#this is rock paper scissors lizard spock.
import random
def clear_screen():
    print '\n'*100
def cheatmode(toggle):
    #cheat mode!
    # get a random number between 0 and a hundred, 
    # if it's under 40, cheat!
    cheat=random.randint(0,100)
    if toggle=='on':
        if cheat <40:
            return "cheat"
        else:
            return "nocheat"
    else:
        return "nocheat"
def rock(move2):
    #if player 1 is rock, then he beats lizard and scissors, 
    #but loses in all other cases. he ties if player 2 is rock as 
    #well. All the other functions up here work the same way.
    if move2=="lizard" or move2=="scissors":
        print "player 1 wins!"
        winner='player_1'
        return winner
    elif move2=="rock":
        print "OMG TIE"
        winner='none'
        return winner
    else:
        print "player 2 wins!"
        winner='player_2'
        return winner
def paper(move2):
    if move2=="rock" or move2=="spock":
        print "player 1 wins!"
        winner='player_1'
        return winner
    elif move2=="paper":
        print "OMG TIE"
        winner='none'
        return winner
    else:
        print "player 2 wins!"
        winner='player_2'
        return winner
def scissors(move2):
    if move2=="paper" or move2=="lizard":
        print "player 1 wins!"
        winner='player_1'
        return winner
    elif move2=="scissors":
        print "OMG TIE"
        winner='none'
        return winner
    else:
        print "player 2 wins!"
        winner='player_2'
        return winner
def lizard(move2):
    if move2=="spock" or move2=="paper":
        print "player 1 wins!"
        winner = 'player_1'
        return winner
    elif move2=="lizard":
        print "OMG TIE"
        winner='none'
        return winner
    else:
        print "player 2 wins!"
        winner='player_2'
        return winner
def spock(move2, toggle):
    #if player 1 is spock, there is a chance he just pwns everything as well.
    #i think there is a slight advantage for player two, because if cheat mode 
    #is on and spock gets god powers, it doesnt matter if player one is spock 
    #with god powers as well. That's a feature though, not a bug.
    cheat="nocheat"
    cheat=cheatmode(toggle)
    if cheat=="cheat":
        print "Player one's spock vaporized player two's", move2
        winner='player_1'
        return winner
    else:
        if move2=="rock" or move2=="scissors":
            print "player 1 wins!"
            winner='player_1'
            return winner
        elif move2=="spock":
            print "OMG TIE"
            winner='none'
            return winner
        else:
            print "player 2 wins!"
            winner='player_2'
            return winner
def compare(move, move2, p, toggle):
    #if player two is spock, there is chance he just pwns everything.
    if move2=="spock":
        cheat="nocheat"
        cheat=cheatmode(toggle)
        if cheat=="cheat":
            print "player two's spock vaporized player one's", move
            winner='player_2'
            return winner
    if move=="rock":
        winner=rock(move2)
        return winner
    elif move=="paper":
        winner=paper(move2)
        return winner
    elif move=="scissors":
        winner=scissors(move2)
        return winner
    elif move=="lizard":
        winner=lizard(move2)
        return winner
    elif move=="spock":
        winner=spock(move2, toggle)
        return winner
def play0(toggle):
    #play no players
    move=random.choice(["rock", "paper", "scissors", "lizard", "spock"])
    print "player 1 threw", move
    move2=random.choice(["rock", "paper", "scissors", "lizard", "spock"])
    print "player 2 threw", move2
    winner=compare(move,move2,1, toggle)
    return winner
def play1(toggle):
    #play one player. get an input for player 1, then choose the
    #input for player two randomly from a list of options.
    move=''
    while move!='spock' and move != 'lizard' and move !='paper' and move !='scissors' and move !='rock':
        move=raw_input("Player 1:Rock Paper Scissors Lizard Spock?\n")
        move=move.lower()
    move2=random.choice(["rock", "paper", "scissors", "lizard", "spock"])
    print 'player 2 threw', move2
    winner=compare(move,move2,1, toggle)
    return winner
def play2(toggle):
    #play two players. get inputs for both players one and two, then compare 'em.
    move=''
    while move!='spock' and move != 'lizard' and move !='paper' and move !='scissors' and move !='rock':
        move=raw_input("Player 1:Rock Paper Scissors Lizard Spock? ")
        move=move.lower()
    clear_screen()
    move2=''
    while move2!='spock' and move2 != 'lizard' and move2 !='paper' and move2 !='scissors' and move2 !='rock':
        move2=raw_input("Player 2: Rock Paper Scissors Lizard Spock? ")
        move2=move2.lower()
    print "player 1 threw ",move
    print "player 2 threw ",move2
    winner=compare(move,move2,2, toggle)
    return winner
def game(upto,players, toggle):
    points1=0
    points2=0
    while points1<upto and points2<upto:
        print "player 1 has ", points1, "points"
        print "player 2 has ", points2, "points"
        if players==1:
            winner=play1(toggle)
        elif players==2:
            winner=play2(toggle)
        elif players==0:
            winner=play0(toggle)
        if winner=='player_1':
            points1+=1
        if winner=='player_2':
            points2+=1
    if points2==upto:
        print "player 1 has ", points1, "points"
        print "player 2 has ", points2, "points"
        print "Player 2 is the winner!"
	return
    if points1==upto:
        print "player 1 has ", points1, "points"
        print "player 2 has ", points2, "points"
        print "Player 1 is the winner!"
	return
def init():
    while True:
        players=raw_input("How many players?(0, 1, or 2)\n")
        if players in ('0','1','2'):
            players=int(players)
            break
        else: print 'not allowed.'
    while True:
        upto=False
        try:
            upto=input("What do you want to play up to?\n")
        except:
            print "input a number please"
        if upto >0:
            break
    #secret toggle for turning on cheat mode.
    toggle=raw_input("Is spock really cool (y/n)?\n")
    if toggle=='y' or toggle=='Y':
        toggle='on'
    else:
        toggle='off'
    game(upto,players, toggle)
    again=raw_input("Would you care to play again? (y/n)\n")
    if again=='y' or again=='Y':
        return 'yes'
    else:
        return 'no'
#Much better solution here.
again='yes'
while again !='no':
    again='no'
    again=init()

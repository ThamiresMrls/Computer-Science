"""Plays 3 different versions of Rock Paper Scissors
t=game mode
p=player's pick
c=computer's pick
n=player's score
m=computer's score
g=number of times played (counter)
l=number of players
q=match data
i is a local in game()
w is a way to store win data for analysis
I think those are all of my variables.

Enjoy.
"""

import random

def restart():
    t=ask()
    l=playernumber()
    q=match()
    program(t,0,0,1,l,q)

#determines game mode
#it could be possible that my str to int isn't working properly
def ask():
    print "0 normal RPS"
    print "1 cheaty RPS"
    print "2 lizard RPS"
    t=input("Please make your selection. ")
    return t

def playernumber():
    l=input("0, 1, or 2 players? ")
    if l != 0 and l != 1 and l != 2:
        print "please input a supported number of players"
        playernumber()
    return l

def match():
    q=input("How many games shall the match last? ")
    if type(q)==int and q>=1:
        return q
    else:
        print "Please type a integer greater than 0"
        match()
#gets player's pick and checks whether to cheat
#returns player's pick and creates computer's pick also
def rps(player):
    print "1=Rock"
    print "2=Paper"
    print "3=Scissors"
    p=input(player + ":Please type the number that corresponds to your pick ")
    if p<4 and p>0:
        print player + " chooses " +convert(p)
        return p
    else:
        print "Please type the number 1 to 3 inclusive."
        rps(player)
        
def crps(player):
    p=random.randint(1,3)
    print player + " chooses " + convert(p)
    return p
    
#does as it says
def cheat(c):
    if c==1:
        return 2
    if c==2:
        return 3
    if c==3:
        return 1

def convert(g):
    if g==1:
        return 'rock'
    if g==2:
        return 'paper'
    if g==3:
        return 'scissors'
    if g==4:
        return 'spock'
    if g==5:
        return 'lizard'

#this contains the spockliz version of rps(), it is similar
#except it starts with an input and thus uses the convert function
def spock(player):
    print "1=Rock"
    print "2=Paper"
    print "3=Scissors"
    print "4=Spock"
    print "5=Lizard"
    p=input(player + ": please type the number that corresponds to your pick ")
    if p<6 and p>0:
        print player + " chooses " + convert(p)
        return p
    else:
        print "Please type the number 1 to 5 inclusive."
        spock(player)

def cspock(player):
        p=random.randint(1,5)
        print player + " chooses " + convert(p)
        return p

#determines victory for spockliz
#returns value for score keeping
def wintest(p,c):
    p-=1
    c-=1
    
    q=[[0,1,-1,1,-1],
       [-1,0,1,-1,1],
       [1,-1,0,1,-1],
       [-1,1,-1,0,1],
       [1,-1,1,-1,0]]

    if q[p][c]==1:
        print "Player 2 wins!"
        return 1 
    elif q[p][c]==-1:
        print "Player 1 wins!"
        return 2
    elif q[p][c]==0:
        print "It's a tie!"
        return 0

def game(t,n,m,g,l,q):
    y=raw_input("Do you want to play? (Type help for more commands) ")
    if y=='no':
        return False
    elif y=='change':
        t=ask()
        program(t,n,m,g,l,q)
    elif y=='restart':
        restart()
    elif y=='number of players':
        l=playernumber()
        program(t,n,m,g,l,q)
    elif y=='match':
        q=match()
        program(t,n,m,g,l,q)
    elif y=='' or y=='yes':
        return True
    else:
        print "Type 'no' to end game"
        print "Type 'match' to choose number of games required for victory"
        print "Type 'change' to change game mode"
        print "Type 'number of players' to change the number of players"
        print "Type 'restart' to clear the score and choose game mode"
        print "Press [enter] or type 'yes' to keep playing"
    game(t,n,m,g,l,q)

def program0(t,n,m,g,l,q):
    while game(t,n,m,g,l,q):
        for y in range(q):
            player='Player 1'
            if t==0:
                p=crps(player)
                player='Player 2'
                c=crps(player)
            elif t==1:
                p=crps(player)
                player='Player 2'
                if random.randint(1,1000)<400:
                    c=cheat(p)
                else:
                    c=crps(player)
            elif t==2:
                p=cspock(player)
                player='Player 2'
                c=cspock(player)
            w=wintest(p,c)
            if w==1:
                m+=1
            if w==2:
                n+=1
            print "Current score is:"
            print "Player 2: "+str(n)
            print "Player 1: "+str(m)
            print "after " +str(g) + " games."
            g+=1
        if n>m:
            print "Player 2 wins the match!"
        elif m>n:
            print "Player 1 wins the match!"
        else:
            print "The match ends in a draw!"

def program2(t,n,m,g,l,q):
    while game(t,n,m,g,l,q):
        for y in range(q):
            player='Player 1'
            if t==1:
                t=0
            if t==0:
                p=rps(player)
                player='Player 2'
                c=rps(player)
            if t==2:
                p=spock(player)
                player='Player 2'
                c=spock(player)
            w=wintest(p,c)
            if w==1:
                m+=1
            if w==2:
                n+=1
            print "Current score is:"
            print "Player 2: "+str(n)
            print "Player 1: "+str(m)
            print "after " +str(g) + " games."
            g+=1
        if n>m:
            print "Player 2 wins the match!"
        elif m>n:
            print "Player 1 wins the match!"
        else:
            print "The match ends in a draw!"
def program(t,n,m,g,l,q):
    if l==0:
        program0(t,n,m,g,l,q)
    if l==2:
        program2(t,n,m,g,l,q)
    while game(t,n,m,g,l,q):
        for y in range(q):
            player='Player 1'
            if t==0:
                p=rps(player)
                player='Player 2'
                c=crps(player)
            elif t==1:
                p=rps(player)
                player='Player 2'
                if random.randint(1,1000)<400:
                    cheat(p)
                else:
                    c=crps(player)
            elif t==2:
                p=spock(player)
                player='Player 2'
                c=cspock(player)
            w=wintest(p,c)
            if w==1:
                m+=1
            if w==2:
                n+=1
            print "Current score is:"
            print "Player 2: "+str(n)
            print "Player 1: "+str(m)
            print "after " +str(g) + " games."
            g+=1
        if n>m:
            print "Player 2 wins the match!"
        elif m>n:
            print "Player 1 wins the match!"
        else:
            print "The match ends in a draw!"

restart()

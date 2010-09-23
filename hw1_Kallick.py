#ensure that crashes never happen.
def m():
    if front_is_clear():
        move()
    else:
        pass
tl=turn_left
r=repeat
#turn right
def turn_right():
    r(tl,3)
tr=turn_right
#make a 2x2 box that goes out to the left 
#from the robot and leaves the robot
#in the starting posistion, but ends
#up facing the opposite direction.
def box():
    tl()
    m()
    m()
    tr()
    m()
    m()
    tr()
    m()
    m()
    tr()
    m()
    m()
#begin the program
repeat(m,2)
tl()
#makes a squiggle. That is, the
#robot moves up n spaces, then 
#makes a box, then moves down n 
#spaces. the robot ends up facing
#the opposite direction, so it 
#moves one space to looker's right
#and then faces upwards.
def squiggle(n):
    repeat(m,n)
    box()
    repeat(m,n)
    tl()
    m()
    tl()
#draws n squiggles, of x squiggle
#size.
def draw(n,x):
    i=0
    while i<n:
        squiggle(x)
        n=n-1
def picture(n):
    i=1
    while i<n:
        draw(n,n)
        tl()
        r(m,n-1)
        tr()
        n=n-1
picture(7)
turn_off()

"""Let's make some comments. Yaay! This program is
written mostly entirely by Thomas Schubert. Daniel
fixed some stuff when Thomas' code was broken.
"""
#set zeee variables to zero. ask the user if they 
#want to increase them. Cant make em more than five
#though, and when everything is five, we're done.


#the problem with this right now is the same as 
#it was a while ago. Not sure how to loop it without
#all the rows clearing to zero every time.
def player2():
    global a1
    global b1
    global c1
    global d1
    global e1
    global f1
    global g1
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    #this just doesnt work, if you just set them without the if,
    #it does. well, it does what the comment at the top says it 
    #will.
    if a1 is None:
        a1=0
        b1=0
        c1=0
        d1=0
        e1=0
        f1=0
        g1=0
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        g=0
    str1 = raw_input("Where would player2 like to go? ")
    if str1 == "a":
        if a+a1<5:
            a1+=1
        else: print "Sorry, that row is full"
    elif str1 == "b" and b+b1<5:
        if b+b1<5:
            b1+=1
        else: print "Sorry, that row is full"
    elif str1 == "c" and c+c1<5:
        if c+c1<5:
            c1+=1
        else: print "Sorry, that row is full"
    elif str1 == "d" and d+d1<5:
        if d+d1<5:
            d1+=1
        else: print "Sorry, that row is full"
    elif str1 == "e" and e+e1<5:
        if e+e1<5:
            e1+=1
        else: print "Sorry, that row is full"
    elif str1 == "f" and f+f1<5:
        if f+f1<5:
            f1+=1
        else: print "Sorry, that row is full"
    elif str1 == "g" and g+g1<5:
        if g+g1<5:
            g1+=1
        else: print "Sorry, that row is full"
    else: print "Sorry, fuck you."
    print "a=", a+a1
    print "b=", b+b1
    print "c=", c+c1
    print "d=", d+d1
    print "e=", e+e1
    print "f=", f+f1
    print "g=", g+g1
    if a+a1==5 and b+b1==5 and c+c1==5 and d+d1==5 and e+e1==5 and f+f1==5 and g+g1==5:
        print "Shit, I don't know how to exit.\nOh wait, actually I do. I just break"
        g=5000
def play4():
    global a1
    global b1
    global c1
    global d1
    global e1
    global f1
    global g1
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    #again, same problem as in the player2 function
    if a is None:
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        g=0
        a1=0
        b1=0
        c1=0
        d1=0
        e1=0
        f1=0
        g1=0
    str1 = raw_input("Where would player one like to go? ")
    if str1 == "a":
        if a+a1<5:
            a+=1
        else: print "Sorry, your move was invalid"
    elif str1 == "b":
        if b+b1<5:
            b+=1
        else: print "Sorry, your move was invalid"
    elif str1 == "c":
        if c+c1<5:
            c+=1
        else: print "Sorry, your move was invalid"
    elif str1 == "d":
        if d+d1<5:
            d+=1
        else: print "Sorry, your move was invalid"
    elif str1 == "e":
        if e+e1<5:
            e+=1
        else: print "Sorry, your move was invalid"
    elif str1 == "f":
        if f+f1<5:
            f+=1
    elif str1 == "g":
        if g+g1<5:
            g+=1
    else: print "Sorry, your move was too fucking strange."

    print "a=", a+a1
    print "b=", b+b1
    print "c=", c+c1
    print "d=", d+d1
    print "e=", e+e1
    print "f=", f+f1
    print "g=", g+g1
    if a+a1==5 and b+b1==5 and c+c1==5 and d+d1==5 and e+e1==5 and f+f1==5 and g+g1==5:
        print "Shit, I don't know how to exit.\nOh wait, actually I do. I just break"
        g=5000
def c4():
    global a1
    global b1
    global c1
    global d1
    global e1
    global f1
    global g1
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    g=0
    print "Hi!"
    str1 = raw_input("What do you want to do? ")
    if str1=="play":
        str2 = raw_input("What do you want to play? ")
        #we can play tag!!!!!!!!!!!!!1
        if str2 == "tag":
            print "Tag, you're it!"
            #or, in the real world, we can play connect four.
            #well, not actually. but yeah.
        elif str2 == "connect 4":
            str3 = raw_input("How many players are playing? ")
            if str3 == "2":
                while g<5000:
                    play4()
                    player2()
            else:
                print "Well, actually I don't know how to play, so you need two players"
        else:
            print "Sorry, I don't know that game."
    else:
        print "No thanks, I don't want to do that."
c4()

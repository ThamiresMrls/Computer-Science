def play4():
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    while True:
        str1 = raw_input("Where would you like to go?")
        if str1 == "a":
            if a<5:
                a+=1
            else: print "Sorry, your move was invalid"
        elif str1 == "b":
            if b<5:
                b+=1
            else: print "Sorry, your move was invalid"
        elif str1 == "c":
            if c<5:
                c+=1
            else: print "Sorry, your move was invalid"
        elif str1 == "d":
            if d<5:
                d+=1
            else: print "Sorry, your move was invalid"
        elif str1 == "e":
            if e<5:
                e+=1
            else: print "Sorry, your move was invalid"
        elif str1 == "f":
            if f<5:
                f+=1
        elif str1 == "g":
            if g<5:
                f+=1
        else: print "Sorry, your move was fucking strange."

        print "a=", a
        print "b=", b
        print "c=", c
        print "d=", d
        print "e=", e
        print "f=", f
        print "g=", g
        if a==5 and b==5 and c==5 and d==5 and e==5 and f==5 and g==5:
            print "Shit, I don't know how to exit."
            break

print "Hi!"
str1 = raw_input("What do you want to do?")
if str1=="play":
    str2 = raw_input("What do you want to play?")
    if str2 == "tag":
        print "Tag you are it!"
    elif str2 == "connect 4":
        play4()
    else:
        print "Sorry, I don't know that game."
else:
    print "No thanks, I don't want to do that."

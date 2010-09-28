#zig zag fix
def turn_right():
    repeat(turn_left,3)
def pick():
    while on_beeper():
        pick_beeper()
def go_left():
    pick()
    if front_is_clear():
        move()
    else:
        turn_right()
        if front_is_clear:
            move()
            turn_right()
        else:
            turn_off()
def go_right():
    pick()
    if front_is_clear():
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
            turn_left()
        else:
            turn_off()
while True:
    go_right()
    go_left()




#pp1-1
def turn_right():
    repeat(turn_left,3)
def fix():
    if not on_beeper():
        put_beeper()
def column():
    while front_is_clear():
        fix()
        move()
    repeat(turn_left,2)
    while front_is_clear():
        fix()
        move()
    turn_left()
    if front_is_clear():
        repeat(move,4)
        turn_left()
    else:
        turn_off()
turn_left()
while True:
    column()
#pp1-2
def turn_right():
    repeat(turn_left,3)
def going_right():
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
    turn_left()
    if front_is_clear():
        move()
        turn_left()
    else:
        turn_off()
def going_left():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_right()
    if front_is_clear():
        move()
        turn_right()
    else:
        turn_off()
while True:
    going_right()
    going_left()
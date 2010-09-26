from gasp import *
begin_graphics(width=700, height=600, title="Connect Four", background=color.BLACK)
def draw_across(n):
    x=7
    c=50
    while x>0:
        Circle((c,n), 40, filled=True, color=color.WHITE, thickness=0)
        c +=100
        x -=1
def draw_up():
    x=6
    c=50
    while x>0:
        draw_across(c)
        c +=100
        c -=1
draw_up()
update_when('key_pressed')
end_graphics()

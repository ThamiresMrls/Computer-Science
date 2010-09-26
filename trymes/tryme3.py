from tryme1 import *
from gasp import *
def nine_lines():
    three_lines()
    three_lines()
    three_lines()
def clear_screen():
    nine_lines()
    nine_lines()
    nine_lines()
def repeat(function,n):
    i=0
    while i<n:
        function()
        n -=1
def cat_n_times(s, n):
        print s*n
begin_graphics()

Circle((200, 200), 60)
Line((100, 400), (580, 200))
Box((400,350), 120, 100)
update_when('key_pressed')
end_graphics()

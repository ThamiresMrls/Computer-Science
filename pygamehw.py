'''
File: pygamehw.py
Author: Daniel Dyssegaard Kallick
Description:tanks, or something like that
'''

background_image_filename = 'bg.jpg'
sprite_image_filename = 'mouse.png'
import pygame
from pygame.locals import *
import random
from sys import exit
import math

pygame.init()

my_font = pygame.font.Font("linux-libertine.ttf", 16)
screen = pygame.display.set_mode((1000,600), 0 ,32)
pygame.display.set_caption("Hello, World!")
tank1 = pygame.image.load(sprite_image_filename).convert_alpha()
tank2 = pygame.image.load('sprite2.jpg').convert()
import random

def clear_screen(hp1,hp2,gravity):
    """
    Refreshes the screen. Redraws the scores, the tanks, and the background.
    if there's a winner, shows the winner.
    """
    winner=None
    if hp1==0:
        winner='2'
    if hp2==0:
        winner='1'
    screen.fill((240,200,200))
    screen.blit(tank1, (0,520))
    screen.blit(tank2, (920,520))
    display_hp1 = my_font.render("Player1 HP: " + str(hp1), True, (0,0,0))
    display_hp2 = my_font.render("Player2 HP: " + str(hp2), True, (0,0,0))
    display_gravity = my_font.render("Gravity: " + str(round(gravity,3)), True, (0,0,0))
    display_winner = my_font.render("Player " + str(winner) + " Wins!", True, (0,0,0))
    screen.blit(display_hp1, (0,25))
    screen.blit(display_hp2, (880,25))
    screen.blit(display_gravity, (450,25))
    #make a blockage
    pygame.draw.rect(screen,(0,0,0),Rect(450,400,200,200))
    #if there's a winner...
    if winner!=None:
        #...show the winner
        screen.blit(display_winner, (450,200))
def fire_gun(x,y,xvel,yvel,time_passed_seconds,player):
    """
    Fires the cannon. Returns a posistion, whether or not
    there is a hit, and whether the projectile is in the
    air
    """
    hit=False
    obstacle=False
    #posistion = velocity times time
    distance_moved_x = (time_passed_seconds * xvel)
    distance_moved_y = (time_passed_seconds * yvel)
    x+=distance_moved_x
    y+=distance_moved_y
    #if the ball hits a wall or the ground, it's not in the air
    if y>595 or x>1000 or x<0:
        inair=False
    else:
        inair=True
    #if player one hits player two, hit is true
    if player==1:
        if x>920 and x<1000 and y>520 and y<600:
            hit=True
    if player==2:
        if x>0 and x<80 and y>520 and y<600:
            hit=True
    if x>450 and y>400 and x<650:
        obstacle=True
        inair=False
    return (int(x),int(y),inair,hit,obstacle)

def make_vector(mag,angle):
    """
    makes an angle and a magnitude into two components
    """
    xvel=0
    yvel=0
    yvel=mag*math.sin(math.radians(angle))
    yvel=-yvel
    xvel=mag*math.cos(math.radians(angle))
    return (xvel,yvel)

def explode(x,y):
    """
    Awesome explosion animation at the posistion
    specified. All credit for the explosion pngs
    goes to http://www.pygame.org/project-Asteroids-506-.html
    """
    for n in range(17):
        screen.blit(pygame.image.load("Explode"+str(n+1)+".png").convert_alpha(), (x-40,y-40))
        pygame.display.update()
        #framerate
        pygame.time.wait(33)
        clear_screen(hp1,hp2,gravity)

def get_input(player,variable,hp1,hp2,gravity):
    user_input=''
    typing=True
    while typing==True:
        for event in pygame.event.get():
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                        exit()
                try:
                    if chr(event.key).isdigit():
                        user_input+=chr(event.key)
                    else:
                        if (event.key == K_RETURN) and len(user_input)>0:
                            typing=False
                        if (event.key == K_BACKSPACE):
                            user_input=user_input[:-1]
                        continue
                except:
                    continue
        display_input = my_font.render("Player" + str(player) + variable + "? " + str(user_input), True, (0,0,0))
        screen.blit(display_input, (450,300))
        pygame.display.update()
        clear_screen(hp1,hp2,gravity)
    user_input=int(user_input)
    return user_input

hp1=1
hp2=1
player=1
keepgoing=True
while keepgoing==True:

    gravity = random.choice([random.uniform(0.2,1),random.uniform(1,5)])

    clear_screen(hp1,hp2,gravity)
    pygame.display.update()

    magnitude=get_input(player,' magnitude',hp1,hp2,gravity)
    clear_screen(hp1,hp2,gravity)
    angle=get_input(player,' angle',hp1,hp2,gravity)

    if player==2:
        angle = 180-angle

    vector=make_vector(magnitude,angle)
    xvel,yvel=vector

    if player==1:
        y=519
        x=0
        color=(255,0,0)
    else:
        y=519
        x=920
        color=(0,0,255)
    inair=True
    hit=False
    airclock = pygame.time.Clock()
    time_in_air=0
    while inair==True:
        time = airclock.tick(100)
        time_in_air+=time
        time_passed_seconds = time_in_air / 1000.0
        yvel+=gravity
        pos=fire_gun(x,y,xvel,yvel,time_passed_seconds,player)
        pygame.draw.circle(screen,color,(pos[0],pos[1]),10)
        pygame.display.update()
        clear_screen(hp1,hp2,gravity)
        inair=fire_gun(x,y,xvel,yvel,time_passed_seconds,player)[2]
        hit=fire_gun(x,y,xvel,yvel,time_passed_seconds,player)[3]
        obstacle=fire_gun(x,y,xvel,yvel,time_passed_seconds,player)[4]
        if hit==True:
            inair=False
    if obstacle==True:
        explode(pos[0],pos[1])
    if player==1:
        player=2
        if hit==True and hp1>0 and hp2>0:
            hp2 -=1
            explode(pos[0],pos[1])
    elif player==2:
        player=1
        if hit==True and hp1>0 and hp2>0:
            hp1 -=1
            explode(pos[0],pos[1])
    if hp1==0 or hp2==0:
        explode(100,100)
        explode(800,100)
        explode(100,300)
        explode(800,300)
        keepgoing=False

    pygame.display.update()
exit()

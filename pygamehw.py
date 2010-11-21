background_image_filename = 'bg.jpg'
sprite_image_filename = 'mouse.png'

import pygame
from pygame.locals import *
from random import *
from sys import exit
import math

pygame.init()

screen = pygame.display.set_mode((1000,600), 0 ,32)
pygame.display.set_caption("Hello, World!")

sprite = pygame.image.load(sprite_image_filename).convert_alpha()
sprite2 = pygame.image.load('sprite2.jpg').convert()
gravity = 1
def clear_screen():
    screen.fill((240,200,200))
    screen.blit(sprite, (0,520))
    screen.blit(sprite2, (920,520))
def fire_gun(x,y,xvel,yvel,time_passed_seconds):
    distance_moved_x = (time_passed_seconds * xvel)
    distance_moved_y = (time_passed_seconds * yvel)
    x+=distance_moved_x
    y+=distance_moved_y
    print time_passed_seconds
    if y>595:
        inair=False
    else:
        inair=True
    return (int(x),int(y),inair)
def make_vector(mag,angle):
    xvel=0
    yvel=0
    yvel=mag*math.sin(math.radians(angle))
    yvel=-yvel
    xvel=mag*math.cos(math.radians(angle))
    return (xvel,yvel)
player=1
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    clear_screen()
    pygame.display.update()
    magnitude=input("cannon power?\n")
    angle=input("cannon angle?\n")
    vector=make_vector(magnitude,angle)
    yvel=vector[1]
    if player==1:
        y=519
        x=0
        color=(255,0,0)
    else:
        y=519
        x=920
        color=(0,0,255)

    inair=True
    airclock = pygame.time.Clock()
    time_in_air=0
    while inair==True:
        time = airclock.tick(100)
        time_in_air+=time
        time_passed_seconds = time_in_air / 1000.0
        yvel+=gravity
        pos=fire_gun(x,y,vector[0],yvel,time_passed_seconds)
        pygame.draw.circle(screen,color,(pos[0],pos[1]),10)
        pygame.display.update()
        clear_screen()
        inair=fire_gun(x,y,vector[0],yvel,time_passed_seconds)[2]
    if player==1:
        player=2
    else:
        player=1

    pygame.display.update()

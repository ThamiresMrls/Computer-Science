###
# not_a_swarm_yet.py
#
# author: Kristina Striegnitz
#
# version: 2/3/2010
#
# On the way to a swarm. This program creates a whole bunch of
# creatures that move around and bounce off the edges.
###
import random, math
from boids_display import run_display
from cohesion import cohesion
from align import align
from separate import separate

# These are global constants. That is global variables, with a value
# that never changes while the program runs.
WIDTH = 1000
HEIGHT = 1000

def run_swarm(n):

    boids = []
    for count in range(0,n):
        b_x_pos = random.randint(0,WIDTH)
        b_y_pos = random.randint(0,HEIGHT)
        b_x_vel = random.randint(-400,400)
        b_y_vel = random.randint(-400,400)
        boid = [b_x_pos, b_y_pos, b_x_vel, b_y_vel, random_color()]

        boids = boids + [boid]

    # Call the function run_display which we imported from the
    # file/module boids_display.py. run_display takes a list of boids,
    # the name of a function which describes how each boids position
    # and speed should be updated as time passes, and the width and
    # the height of the display window.
    run_display(boids, update_boids, WIDTH, HEIGHT)


# This function takes two parameters: a list of boids and a time in
# miliseconds. The time parameter indicates how much time has passed
# since the last time update was called. The function specifies how
# each boid from the list of boids given as a parameter gets updated,
# that is how each boid's position and velocity changes given the time
# that has passed since the last update.
# The function update_boids gets called every few milliseconds by
# run_display.
def update_boids(boids, time):

    for index in range(len(boids)):
        b = boids[index]
        b[2] += cohesion(index, boids)[0]*10
        b[3] += cohesion(index, boids)[1]*10
        b[2] += separate(index, boids)[0]*5
        b[3] += separate(index, boids)[1]*5
        b[2] += align(index, boids)[0]
        b[3] += align(index, boids)[1]
        # Limit velocity to 500 pixels per second horizontally and vertically
        b[2] = speed_limit(b[2], 500)
        b[3] = speed_limit(b[3], 500)

        # Update the boid's position based on its velocity and the
        # time that has passed since the last update.
        b[0] += float(b[2])/1000 * time
        b[1] += float(b[3])/1000 * time

        # Make the boid bounce off the walls.
        if b[0] < 0:
            b[0] = 0
            b[2] = -b[2]
        elif b[0] > WIDTH:
            b[0] = WIDTH
            b[2] = -b[2]
        if b[1] < 0:
            b[1] = 0
            b[3] = -b[3]
        elif b[1] > HEIGHT:
            b[1] = HEIGHT
            b[3] = -b[3]

# This function picks a random color from a given list of colors.
def random_color():
    colors = [(255,140,0), (139,0,0), (139,0,139), (0,100,0), (255,69,0)]
    return random.choice(colors)


def speed_limit(vel, limit):
    if vel > 500:
        return 500
    elif vel < -500:
        return -500
    else:
        return vel


### START EVERYTHING ###
run_swarm(50)

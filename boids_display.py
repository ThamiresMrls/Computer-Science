###
# boids_display.py
#
# author: Kristina Striegnitz
#
# version: 1/31/2010
#
# A simple pygame display for a list of boids.
#Modified by Daniel Dyssegaard Kallick
###
import math,pygame

# This function takes a list of boids (specified as a list with 5
# elements: x and y position, x and y velocity, and the color), a
# function describing how the boids get updated each frame and the
# width and the height of the display window. It then creates a pygame
# window, displays the boids and calls the update function in every
# frame.
def run_display(boids, update_function, WIDTH, HEIGHT,sm,cm,ao,sl):
    pygame.init()
    width = WIDTH
    height = HEIGHT
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    
    keepGoing = True
    while (keepGoing):

        dt = clock.tick()

        # go through all events that happened and check ...
        for event in pygame.event.get():
            # ... whether the event was a quit event
            if event.type == pygame.QUIT:
                keepGoing = False

        # update boids
        update_function(boids, dt,sm,cm,ao,sl)

        # draw everything
        screen.fill((25,25,112))

        for b in boids:
            pygame.draw.circle(screen,b[4],(int(round(b[0])),int(round(b[1]))),b[5])
            point_x = b[0] + float(b[2]) / math.sqrt(b[2]**2 + b[3]**2) * 20
            point_y = b[1] + float(b[3]) / math.sqrt(b[2]**2 + b[3]**2) * 20
            pygame.draw.line(screen,b[4],(int(b[0]),int(b[1])),(point_x, point_y), 3)
        
        pygame.display.update()

    pygame.quit()


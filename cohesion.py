###
# cohesion.py
#
# author: Kristina Striegnitz
#
# version: 2/3/2010
#
# Cohesion behavior: try to move toward the center of your group.
#
# This function determines how the the velocity of a given boid should
# be adjusted for the boid to move toward the center of its group.
###

# The function takes two parameters: a list of boids (the group) and a
# number (the index of the boid that we are currently dealing
# with). The function returns a list of two numbers. The first number
# in that list is the amount that should be added to the horizontal
# velocity of the boid and the second number is the amount that should
# be added to the vertical velocity of the boid.
def cohesion(index, boids):
    b = boids[index]

    # Find the perceived center, i.e. the center of all *other* boids.
    perceived_center = [0, 0]
    for other_index in range(len(boids)):
        if other_index != index:
            other_b = boids[other_index]
            perceived_center[0] += other_b[0]
            perceived_center[1] += other_b[1]
    perceived_center[0] =  float(perceived_center[0]) / (len(boids) - 1)
    perceived_center[1] =  float(perceived_center[1]) / (len(boids) - 1)

    # Calculate the amounts that should be added to the boid's
    # horizontal and vertical velocity for the boid to slowly move
    # toward the perceived center.
    v1 = [0, 0]
    v1[0] = (perceived_center[0] - b[0]) / 100
    v1[1] = (perceived_center[1] - b[1]) / 100
    return v1


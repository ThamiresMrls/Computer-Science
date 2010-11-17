import math,random

def separate(index, boids, random_color, current_color):
    """This function take two parameters, the first an integer and the second a list of boids. 
    It returns a list of two integers which should be added to the velocity of the boid in position index.
    The effect is to have the boids alter their velocities as not to crash into one another if they get too close.
    """
    b = boids[index]
    v2 = [0, 0, current_color]
    for other_index in range(len(boids)):
        if other_index != index:
            other_b = boids[other_index]
            distance = math.sqrt((other_b[0] - b[0]) ** 2 + (other_b[1] - b[1]) ** 2)
            if distance < 50:
                v2[0] -= (other_b[0] - b[0])
                v2[1] -= (other_b[1] - b[1])
                v2[2] = random_color()
    return v2

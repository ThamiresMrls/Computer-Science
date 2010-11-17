def align(index, boids):
    """This function take two parameters, the first an integer and the second a list of boids. 
    It returns a list of two integers which should be added to the velocity of the boid in position index.
    The effect is to have the boids alter their velocities follow the direction of every other boid.
    """
    b = boids[index]
    v3 = [0, 0]
    for other_index in range(len(boids)):
        if other_index != index:
            other_b = boids[other_index]

            v3[0] += other_b[2]
            v3[1] += other_b[3]

    v3[0] /= len(boids) - 1
    v3[1] /= len(boids) - 1
    v3[0] = (v3[0] - b[2]) / 8
    v3[1] = (v3[1] - b[3]) / 8
    return v3
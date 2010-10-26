import math

def initial_velocity(height, distance):
    return distance/(math.sqrt(height/4.9))

def time_to_peak(init_v, theta):
    return (init_v*math.sin(theta))/9.8

def max_height(theta, init_v, time_to_p,height):
    return init_v*math.sin(theta)*time_to_p-4.9*time_to_p**2+height

def total_time(time_to_p, max_h):
    return time_to_p+math.sqrt(max_h/4.9)

def total_x(init_v, total_t, theta):
    return init_v*math.cos(theta)*total_t

distance=float(raw_input("initial distance to get initial velocity\n"))
height=float(raw_input("initial height to get initial velocity\n"))
init_v=initial_velocity(height, distance)
print "initial velocity is ", init_v
theta=float(raw_input("What angle?\n"))
theta=math.radians(theta)
print theta
time_to_p=time_to_peak(init_v, theta)
print time_to_p, "time to p"

max_h=max_height(theta, init_v, time_to_p, height)
print max_h, "max h"

total_t=total_time(time_to_p, max_h)
print total_t, "total t"

total_distance=total_x(init_v, total_t, theta)
print total_distance, "total d"

print "the total distance is ", total_distance, "meters"

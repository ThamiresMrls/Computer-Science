import math

#distance=float(raw_input("initial distance to get initial velocity\n"))

#height=float(raw_input("initial height to get initial velocity\n"))

height2=float(raw_input("height at launch point (in meters)"))
#initial_velocity = distance/(math.sqrt(height/4.9))

initial_velocity=400

theta=float(raw_input("What angle?\n"))

theta=math.radians(theta)

print theta

time_to_peak = (initial_velocity*math.sin(theta))/9.8

print time_to_peak, "time to p"

max_height = initial_velocity*math.sin(theta)*time_to_peak-4.9*time_to_peak**2+height2

print max_height, "max_height"

total_time = time_to_peak+math.sqrt(max_height/4.9)
print total_time, "total_time"

total_x = initial_velocity*math.cos(theta)*total_time

print total_x,"meters", "total distance"

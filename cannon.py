#This is a projectile motion program that determines the distance a 
#projectile will go in ideal conditions, given initial velocity and 
#angle of launch. By Daniel Dyssegaard Kallick October 28, 2010
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
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

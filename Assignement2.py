import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import platform
from matplotlib.patches import Arc

def create_rectangle(x, y, width, height):
    rect=patches.Rectangle((x, y), width, height ,edgecolor='red',facecolor='none')
    return rect

def create_circle(x, y, radius):
    circle=patches.Circle((x, y), radius ,edgecolor='r',facecolor='none')
    return circle

def create_semi_circle(x,y, radius,circle_begin, circle_end):
    crease=patches.Arc((x,y), radius, radius, angle=0, theta1=circle_begin, theta2=circle_end, color='red')
    return crease

fig, ax = plt.subplots()

rink = patches.FancyBboxPatch(
    (0, 0), 61, 30,
    boxstyle=patches.BoxStyle("Round", pad=0, rounding_size=9),
    edgecolor='black', facecolor='white', lw=2)


ax.add_patch(rink)
#creating all face off circles
ax.add_patch(create_circle(10.7,21.7,4.5)) #face off circle of the left side
ax.add_patch(create_circle(10.7,8.3,4.5))  #//
ax.add_patch(create_circle(49.3,21.7,4.5)) #face off circle on the right side
ax.add_patch(create_circle(49.3,8.3,4.5))  #//
ax.add_patch(create_circle(30.5,15,4.5))   #faceoff circle in the middle

#creating all face off dots
ax.add_patch(create_circle(10.7,21.7,0.3)) #face off circle of the left side
ax.add_patch(create_circle(10.7,8.3,0.3))  #//
ax.add_patch(create_circle(49.3,21.7,0.3)) #face off circle on the right side
ax.add_patch(create_circle(49.3,8.3,0.3))  #//
ax.add_patch(create_circle(23.17,21.7,0.3)) #face off circle in the neutral zone on the left side
ax.add_patch(create_circle(23.17,8.3,0.3))  #//
ax.add_patch(create_circle(37.83,21.7,0.3)) #face off circle in the neutral zone on the right side
ax.add_patch(create_circle(37.83,8.3,0.3))  #//
ax.add_patch(create_circle(30.5,15,0.3))   #faceoff circle in the middle

# Creating the blue lines
ax.plot([21.67, 21.67], [0, 30], color='blue')
ax.plot([39.33, 39.33], [0, 30], color='blue')

# Creating the red lines
ax.plot([30.5, 30.5], [0, 30], color='red')
ax.plot([4, 4], [1.3, 28.7], color='red')
ax.plot([57, 57],[1.3, 28.7], color='red')

# Creating goal semi_circles
ax.add_patch(create_semi_circle(4,15,3.66,-90,90)) #left goal crease
ax.add_patch(create_semi_circle(57,15,3.66,90,-90)) #right goal crease 
ax.add_patch(create_semi_circle(30.5,0,6,0,180)) # referee's circle

# Create the goal rectangles
ax.add_patch(create_rectangle(3, 14.085, 1, 1.83)) #left goal
ax.add_patch(create_rectangle(57, 14.085, 1, 1.83)) #right goal

# penalty boxes and scorekeepers boxes
ax.add_patch(create_rectangle(21.67, -2, 5.8866, 2)) #left penalty box
ax.add_patch(create_rectangle(27.5566, -2, 5.8866, 2)) #left penalty box
ax.add_patch(create_rectangle(33.4432, -2, 5.8866, 2)) #left penalty box

ax.set_xlim(-15, 80)
ax.set_ylim(-10, 40)
ax.set_aspect('equal')
ax.axis('off')
plt.show()
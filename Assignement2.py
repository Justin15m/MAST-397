import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import platform
from matplotlib.patches import Arc

def create_rectangle(x, y, width, height):
    rect=patches.Rectangle((x, y), width, height ,edgecolor='red',facecolor='none')
    return rect

def create_circle(x, y, radius,ec,fc):
    circle=patches.Circle((x, y), radius ,edgecolor=ec,facecolor=fc)
    return circle

def create_semi_circle(x,y, radius,circle_begin, circle_end):
    crease=patches.Arc((x,y), radius, radius, angle=0, theta1=circle_begin, theta2=circle_end, color='red')
    return crease

# all the dimensions are in feet and we take each foot to be 1 data unit 
# the benigit of this disctionnary is that we can easily change the scale as well as change the dimensions to be that of an international rink
dim={
    "rink_length":200,
    "rink_width":85,
    "corner_radius":28,
    "goal_line":11,
    "goal_width":6,
    "goal_depth":3.333,
    "goal_crease_diameter":8,
    "faceoff_circle_yloc":20.5,
    "faceoff_circle_xloc":33,
    "faceoff_circle_radius":15,
    "faceoff_spot_neutral_xloc":80,
    "faceoff_spot_radius":0.5,
    "blue_line":75,
    

}

def create_rink(scale):
    rink_length=dim["rink_length"]/scale
    rink_width=dim["rink_width"]/scale
    corner_radius=dim["corner_radius"]/scale
    goal_line=dim["goal_line"]/scale
    goal_width=dim["goal_width"]/scale
    goal_depth=dim["goal_depth"]/scale
    goal_crease_diameter=dim["goal_crease_diameter"]/scale
    faceoff_circle_yloc=dim["faceoff_circle_yloc"]/scale
    faceoff_circle_xloc=dim["faceoff_circle_xloc"]/scale
    faceoff_circle_radius=dim["faceoff_circle_radius"]/scale
    faceoff_spot_radius=dim["faceoff_spot_radius"]/scale
    faceoff_spot_neutral_xloc=dim["faceoff_spot_neutral_xloc"]/scale
    faceoff_spot__neutral_radius=dim["faceoff_spot_radius"]/scale
    blue_line=dim["blue_line"]/scale


    fig, ax = plt.subplots()

    rink = patches.FancyBboxPatch(
        (0, 0), rink_length, rink_width,
        boxstyle=patches.BoxStyle("Round", pad=0, rounding_size=corner_radius),
        edgecolor='black', facecolor='white', lw=1)


    ax.add_patch(rink)

    # Creating the red lines
    ax.plot([rink_length/2, rink_length/2], [0, rink_width],linestyle='dotted', color='red')
    ax.plot([goal_line, goal_line], [4, rink_width-4] ,color='red')
    ax.plot([rink_length-goal_line, rink_length-goal_line],[4, rink_width-4], color='red')

    # Creating the blue lines
    ax.plot([blue_line, blue_line], [0, rink_width],lw=4, color='blue')
    ax.plot([rink_length-blue_line, rink_length-blue_line], [0, rink_width],lw=4, color='blue')

    #creating all face off circles
    ax.add_patch(create_circle(faceoff_circle_xloc,rink_width-faceoff_circle_yloc,faceoff_circle_radius,'red','none')) #face off circle of the left side
    ax.add_patch(create_circle(faceoff_circle_xloc,faceoff_circle_yloc,faceoff_circle_radius,'red','none'))  #//
    ax.add_patch(create_circle(rink_length-faceoff_circle_xloc,rink_width-faceoff_circle_yloc,faceoff_circle_radius,'red','none')) #face off circle on the right side
    ax.add_patch(create_circle(rink_length-faceoff_circle_xloc,faceoff_circle_yloc,faceoff_circle_radius,'red','none'))  #//
    ax.add_patch(create_circle(rink_length/2,rink_width/2,faceoff_circle_radius,'blue','none'))   #faceoff circle in the middle

    #creating tick to face off circles
    ax.plot([faceoff_circle_xloc-2.5, faceoff_circle_xloc-2.5], [rink_width-faceoff_circle_yloc+15, rink_width-faceoff_circle_yloc+17], color='red')
    ax.plot([faceoff_circle_xloc+2.5, faceoff_circle_xloc+2.5], [rink_width-faceoff_circle_yloc+15, rink_width-faceoff_circle_yloc+17], color='red')
    ax.plot([rink_length-faceoff_circle_xloc-2.5, rink_length-faceoff_circle_xloc-2.5], [rink_width-faceoff_circle_yloc+15, rink_width-faceoff_circle_yloc+17], color='red')
    ax.plot([rink_length-faceoff_circle_xloc+2.5, rink_length-faceoff_circle_xloc+2.5], [rink_width-faceoff_circle_yloc+15, rink_width-faceoff_circle_yloc+17], color='red')

    ax.plot([faceoff_circle_xloc-2.5, faceoff_circle_xloc-2.5], [rink_width-faceoff_circle_yloc-15, rink_width-faceoff_circle_yloc-17], color='red')
    ax.plot([faceoff_circle_xloc+2.5, faceoff_circle_xloc+2.5], [rink_width-faceoff_circle_yloc-15, rink_width-faceoff_circle_yloc-17], color='red')
    ax.plot([rink_length-faceoff_circle_xloc-2.5, rink_length-faceoff_circle_xloc-2.5], [rink_width-faceoff_circle_yloc-15, rink_width-faceoff_circle_yloc-17], color='red')
    ax.plot([rink_length-faceoff_circle_xloc+2.5, rink_length-faceoff_circle_xloc+2.5], [rink_width-faceoff_circle_yloc-15, rink_width-faceoff_circle_yloc-17], color='red')

    ax.plot([faceoff_circle_xloc-2.5, faceoff_circle_xloc-2.5], [faceoff_circle_yloc+15, faceoff_circle_yloc+17], color='red')
    ax.plot([faceoff_circle_xloc+2.5, faceoff_circle_xloc+2.5], [faceoff_circle_yloc+15, faceoff_circle_yloc+17], color='red')
    ax.plot([rink_length-faceoff_circle_xloc-2.5, rink_length-faceoff_circle_xloc-2.5], [faceoff_circle_yloc+15, faceoff_circle_yloc+17], color='red')
    ax.plot([rink_length-faceoff_circle_xloc+2.5, rink_length-faceoff_circle_xloc+2.5], [faceoff_circle_yloc+15, faceoff_circle_yloc+17], color='red')

    ax.plot([faceoff_circle_xloc-2.5, faceoff_circle_xloc-2.5], [faceoff_circle_yloc-15, faceoff_circle_yloc-17], color='red')
    ax.plot([faceoff_circle_xloc+2.5, faceoff_circle_xloc+2.5], [faceoff_circle_yloc-15, faceoff_circle_yloc-17], color='red')
    ax.plot([rink_length-faceoff_circle_xloc-2.5, rink_length-faceoff_circle_xloc-2.5], [faceoff_circle_yloc-15, faceoff_circle_yloc-17], color='red')
    ax.plot([rink_length-faceoff_circle_xloc+2.5, rink_length-faceoff_circle_xloc+2.5], [faceoff_circle_yloc-15, faceoff_circle_yloc-17], color='red')

    #creating all face off dots
    ax.add_patch(create_circle(faceoff_circle_xloc,rink_width-faceoff_circle_yloc,faceoff_spot_radius,'red','red')) #face off circle of the left side
    ax.add_patch(create_circle(faceoff_circle_xloc,faceoff_circle_yloc,faceoff_spot_radius,'red','red'))  #//
    ax.add_patch(create_circle(rink_length-faceoff_circle_xloc,rink_width-faceoff_circle_yloc,faceoff_spot_radius,'red','red')) #face off circle on the right side
    ax.add_patch(create_circle(rink_length-faceoff_circle_xloc,faceoff_circle_yloc,faceoff_spot_radius,'red','red'))  #//
    ax.add_patch(create_circle(faceoff_spot_neutral_xloc,rink_width-faceoff_circle_yloc,faceoff_spot_radius,'red','red')) #face off circle in the neutral zone on the left side
    ax.add_patch(create_circle(faceoff_spot_neutral_xloc,faceoff_circle_yloc,faceoff_spot_radius,'red','red'))  #//
    ax.add_patch(create_circle(rink_length-faceoff_spot_neutral_xloc,rink_width-faceoff_circle_yloc,faceoff_spot_radius,'red','red')) #face off circle in the neutral zone on the right side
    ax.add_patch(create_circle(rink_length-faceoff_spot_neutral_xloc,faceoff_circle_yloc,faceoff_spot_radius,'red','red'))  #//
    ax.add_patch(create_circle(rink_length/2,rink_width/2,faceoff_spot__neutral_radius,'blue','blue'))   #faceoff circle in the middle



    # Creating goal semi_circles
    ax.add_patch(create_semi_circle(goal_line,rink_width/2,goal_crease_diameter,-90,90)) #left goal crease
    ax.add_patch(create_semi_circle(rink_length-goal_line,rink_width/2,goal_crease_diameter,90,-90)) #right goal crease 
    ax.add_patch(create_semi_circle(rink_length/2,0,20,0,180)) # referee's circle

    # Create the goal rectangles
    ax.add_patch(create_rectangle(goal_line-goal_depth, (rink_width-goal_width)/2, goal_depth, goal_width)) #left goal
    ax.add_patch(create_rectangle(rink_length-goal_line, (rink_width-goal_width)/2, goal_depth, goal_width)) #right goal

    # penalty boxes and scorekeepers boxes
    ax.add_patch(create_rectangle(blue_line, -3, 16.666, 3)) #left penalty box
    ax.add_patch(create_rectangle(blue_line+16.6666, -3, 16.666, 3)) #left penalty box
    ax.add_patch(create_rectangle(blue_line+2*16.666, -3, 16.666, 3)) #left penalty box

    ax.set_xlim(0, rink_length)
    ax.set_ylim(-4, rink_width)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.set_size_inches(20,10) # 10 inches wide, 6 inches high
    return plt

create_rink(1).show()
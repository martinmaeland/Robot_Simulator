# Add libraries to python path
import sys
sys.path.append("../lib")
sys.path.append("../src")

import csv

# Import from local libraries
from robot_beta210405 import Robot
from tools import *

# Import from python libraries
import numpy as np
from sympy import symbols

def main():

    # --- Step 1: define symbolic variables ---
    q1, q2, q3 = symbols("q1 q2 q3")
    variables = [q1, q2, q3]

    # --- Step 2: define link lengths ---
    l1 = 1.5
    l2 = 1.5
    l3 = 1.5

    # --- Step 3: define DH-table using symboilic variables and link lengths ---
    # nb: angles need to be in radians
    dh_1 = [q1, l1, 0.0, degToRad(90)]
    dh_2 = [q2, 0.0, l2, 0.0]
    dh_3 = [q3, 0.0, l3, degToRad(90)]
    dh_table = [dh_1, dh_2, dh_3]

    # --- Step 4: solve inverse kinematics manually ---
    # this function should return symbolic variables values when xyz-coordinate input
    def inverse_kinematics(x, z):

        diagonal = np.sqrt( np.power(x, 2) + np.power(z-l1, 2) ) # calculate diagonal length to point using pythagoras
        if (z>=l1):
            theta = np.arccos((x)/(np.sqrt((np.power(x, 2) + np.power(z-l1, 2))))) # calculate angle of diagonal
        else:
            theta = -np.arccos((x)/(np.sqrt((np.power(x, 2) + np.power(z-l1, 2))))) # calculate angle of diagonal

        q3 = -(np.pi/2 - 2*(np.pi/4 - np.arccos(diagonal/3)))
        q2 = np.arccos(diagonal/3) + theta
        q1 = 0

        #print(np.rad2deg(q2), np.rad2deg(q3))
        return q1, q2, q3

    # --- Step 5: calculate angles using inverse kinematics ---
    n_points = 50

    # Generate points on a circle
    theta = np.linspace(0, 2*np.pi, n_points)

    x = 2 + 0.5*np.cos(theta)
    y = 0*theta
    z = 1.5 + 0.5*np.sin(theta)
    
    #path = [[*x], [*y], [*z]]

    # Insert points from csv-file test
    path = [[], [], []]
    with open("../tools/Robot_Path_Generator/tmp/path.txt", "r") as path_file:
        
        # --- create reader ---
        path_reader = csv.reader(path_file)

        # --- read x and z coordinates ---
        first_row = True
        n_points_skip = 5
        n_points_count = 0
        for row in path_reader:
            for coordinate in row:
                if (n_points_count == n_points_skip):
                    if (first_row):
                        path[0].append(float(coordinate))
                        path[1].append(0.0)
                    else:
                        path[2].append(float(coordinate))
                    
                    n_points_count = 0
                else:
                    n_points_count += 1
            
            first_row = False

        #print(len(path[0]), len(path[1]), len(path[2]))

    print(len(path[0]))


    # Calculate angles from points
    robot_angles = []
    for i in range(len(path[0])):
        point = inverse_kinematics(path[0][i], path[2][i])
        robot_angles.append(point)
    
    # --- Step 6: create robot instance with symbolic variables and dh-table ---
    robot = Robot(variables, dh_table)

    # --- Step 7: plot robot with wanted end effector position ---
    #robot.plot(inverse_kinematics(1.5, 1))

    # --- Step 7: animate robot from angles ---
    robot.animate(robot_angles, path)


if __name__ == "__main__":
    main()

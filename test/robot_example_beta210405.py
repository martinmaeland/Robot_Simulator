# Add libraries to python path
import sys
sys.path.append("../lib")
sys.path.append("../src")

# Import from local libraries
from robot_beta210405 import Robot
from tools import *

# Import from python libraries
import numpy as np
from sympy import symbols

def main():

    # Step 1: define symbolic variables
    q1, q2, q3 = symbols("q1 q2 q3")
    variables = [q1, q2, q3]

    # Step 2: define link lengths
    l1 = 1.5
    l2 = 1.5
    l3 = 1.5

    # Step 3: define DH-table using symboilic variables and link lengths
    # nb: angles need to be in radians
    dh_1 = [q1, l1, 0.0, degToRad(90)]
    dh_2 = [q2, 0.0, l2, 0.0]
    dh_3 = [q3, 0.0, l3, degToRad(90)]
    dh_table = [dh_1, dh_2, dh_3]

    # Step 4: solve inverse kinematics manually
    def inverse_kinematics(x, z):

        diagonal = np.sqrt( np.power(x, 2) + np.power(z-l1, 2) ) # calculate diagonal length to point using pythagoras
        if (z>=l1):
            theta = np.arccos((x)/(np.sqrt((np.power(x, 2) + np.power(z-l1, 2))))) # calculate angle of diagonal
        else:
            theta = -np.arccos((x)/(np.sqrt((np.power(x, 2) + np.power(z-l1, 2))))) # calculate angle of diagonal
        print(theta)

        q3 = -(np.pi/2 - 2*(np.pi/4 - np.arccos(diagonal/3)))
        q2 = np.arccos(diagonal/3) + theta
        q1 = 0

        #print(np.rad2deg(q2), np.rad2deg(q3))
        return q1, q2, q3

    # Step 5: calculate trajectory using inverse kinematics

    n_points = 50

    # Generate points on a circle
    theta = np.linspace(0, 2*np.pi, n_points)

    x = 2 + 0.5*np.cos(theta)
    y = 0*theta
    z = 1.5 + 0.5*np.sin(theta)
    
    path = [[*x], [*y], [*z]]

    # Calculate trajectory from points
    robot_angles = []
    for i in range(n_points):
        point = inverse_kinematics(x[i], z[i])
        robot_angles.append(point)
    
    # Step 6: create robot instance with symbolic variables and dh-table
    robot = Robot(variables, dh_table)

    # Step 7: plot robot with wanted end effector position
    #robot.plot(inverse_kinematics(1.5, 1))

    # Step 7: animate robot
    robot.animate(robot_angles, path)

    # TEST

if __name__ == "__main__":
    main()

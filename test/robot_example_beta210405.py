import sys
sys.path.append("../lib")
sys.path.append("../src")

# Import from local libraries
from robot_beta210405 import Robot
from tools import *

# Import from python libraries
import numpy as np
from sympy import symbols
import math


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
        # Find q3 with respect to x and z
        triangle_q3 = 2*math.asin(math.sqrt(x**2 + z**2) / 3)
        q3 = -round(degToRad(180)-triangle_q3, 2)

        # Find q2 with respect to q3
        z_contribution = 0
        if (z > 0):
             z_contribution = math.atan(x/z)
        elif (z < 0):
            z_contribution = -math.atan(x/z)

        q2 = degToRad(90) - triangle_q3/2 + z_contribution
        q2 = round(q2, 2)

        # Return q1, q2, q2
        # q1 is currently constant at 0 degrees
        return 0, q2, q3

    # Step 5: calculate trajectory using inverse kinematics

    # Generate points on a circle
    theta = np.linspace(0, 2*np.pi, 50)
    z = np.cos(theta)
    x = np.sin(theta)

    # Calculate trajectory from points
    trajectory = []
    for i in range(len(x)):
        trajectory.append(inverse_kinematics(x[i], z[i]+2))

    # Step 6: create robot instance with symbolic variables and dh-table
    robot = Robot(variables, dh_table)

    # Step 7: plot robot with wanted end effector position
    #robot.plot([0, np.pi/4, -np.pi/4])

    # Step 7: animate robot from trajectory
    # nb: be careful to not overwrite your files
    #robot.animate(trajectory, framerate=10, save_as="../res/robot_example")

    # TEST
    robot.plot([0,np.pi/2,-np.pi/4])

if __name__ == "__main__":
    main()

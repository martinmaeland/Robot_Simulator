import sys
import os
sys.path.append("../lib")

# Homemade functions
from tools import *

# Plotting tools
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d, is this safe to remove?
import cv2
import glob

# Symbolic and math tools
import sympy as sym
from sympy.solvers import solve
import numpy as np
import math

class Robot:

    def __init__(self, variables, dh_table):
        self.variables = variables # this is all the variables
        self.dh_table = dh_table # this represents dh-table

        # Run these methods at cronstruction
        self.generate_transformation_matrix()

    # Member variables
    variable_values = [] #this is current variable values
    t_n = [] # this contains all t_n matrices
    t_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]] # this is the t-matrix
    robot_origin = [0,0,0,1]


    # this function generates transformation-matrix from dh-table
    def generate_transformation_matrix(self):
        for row in self.dh_table:
            self.t_n.append(mm(rotZ(row[0]), mm(transZ(row[1]), mm(transX(row[2]), rotX(row[3])))))

        for i in range(len(self.t_n)):
            self.t_matrix = mm(self.t_n[-(i+1)], self.t_matrix)

    # this function plots robot
    def plot(self, var_values, plt_show=True, save=False, save_loc=""):

        # Initiate figure
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Initial values
        last_point = self.t_n[0]
        current_point = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        last_xyz = [0,0,0]
        x = y = z = 0
        axis_limits = 4

        # Plot-settings and show
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')

        ax.set_xlim([-axis_limits,axis_limits])
        ax.set_ylim([-axis_limits,axis_limits])
        ax.set_zlim([-axis_limits,axis_limits])

        # Plotting data
        for i in (range(len(self.t_n))):

            ax.plot([float(x)], [float(y)], [float(z)], marker=".", markersize=13, label='test point', color="grey", zorder=10) # plot joint

            current_point = mm(last_point, current_point)

            f = sym.lambdify(self.variables, current_point[0][3], "numpy") # define function x = f(variables)
            x = f(*var_values) # calcualte x

            g = sym.lambdify(self.variables, current_point[1][3], "numpy") # define function y = g(variables)
            y = g(*var_values) # calculate y

            h = sym.lambdify(self.variables, current_point[2][3], "numpy") # define function z = h(variables)
            z = h(*var_values) # calculate z

            ax.plot([last_xyz[0], x], [last_xyz[1], y], [last_xyz[2], z], color="black", zorder=1) # plot link

            if (n := max([x,y,z])) > axis_limits:
                axis_limits = 1.5*n

            last_point = current_point
            if i != (len(self.t_n)-1):
                current_point = self.t_n[i+1]
            last_xyz = [x,y,z]

        if (plt_show == True):
            plt.show()

        if (save == True):
            plt.savefig(save_loc)

        plt.close()


    def animate(self, trajectory, framerate=1, save_as=""):

        print("Generating animation...")

        # Generate frames
        frame = 1001
        for pos in trajectory:
            self.plot([pos[0], pos[1], pos[2]], plt_show=False, save=True, save_loc="../tmp/frame_" + str(frame) + ".png")
            frame += 1

        # Convert frames to video
        img_array = []
        for filename in sorted(glob.glob('../tmp/*.png')):
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
            os.remove(filename)

        # Write videofile
        out = cv2.VideoWriter(save_as+".mp4",cv2.VideoWriter_fourcc(*'DIVX'), framerate, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

        print("Finished, animation saved at '%s'" % (save_as+".avi"))


    # TESTS: these functions are under progress!

    # this is a test-method that calculates joint positions from variable value input
    def forward_kinematics_test(self, variable_values=[0, 0, 0]):

        t_n = np.array(self.t_n)
        joint_output_coordinates = []
        output = []

        # base
        base = self.robot_origin
        joint_output_coordinates.append(base)

        # joint 1
        joint_1 = list(t_n[0].dot(joint_output_coordinates[0]))
        for coordinate in range(len(joint_1)):
            function = sym.lambdify(self.variables, joint_1[coordinate], "numpy")
            joint_1[coordinate] = function(*variable_values)
        joint_output_coordinates.append(joint_1)

        # joint 2
        t_n[1] = t_n[0].dot(t_n[1])
        joint_2 = list(t_n[1].dot(joint_output_coordinates[1]))
        for coordinate in range(len(joint_2)):
            function = sym.lambdify(self.variables, joint_2[coordinate], "numpy")
            joint_2[coordinate] = function(*variable_values)
        joint_output_coordinates.append(joint_2)

        # joint 3
        t_n[2] = (t_n[0].dot(t_n[1])).dot(t_n[2])
        joint_3 = list(t_n[2].dot(joint_output_coordinates[2]))
        for coordinate in range(len(joint_3)):
            function = sym.lambdify(self.variables, joint_3[coordinate], "numpy")
            joint_3[coordinate] = function(*variable_values)
        joint_output_coordinates.append(joint_3)

        return joint_output_coordinates

    def plot_test(self):

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        joints = self.forward_kinematics_test([0, 0 ,0])

        # plot link 1:
        ax.plot([joints[0][0], joints[1][0]], [joints[0][1], joints[1][1]], [joints[0][2], joints[1][2]], color="black", zorder=1)

        # plot link 2:
        ax.plot([joints[1][0], joints[2][0]], [joints[1][1], joints[2][1]], [joints[1][2], joints[2][2]], color="black", zorder=1)

        plt.show()

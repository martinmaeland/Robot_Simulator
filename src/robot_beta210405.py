import sys
#import os
sys.path.append("../lib")

# Homemade functions
from tools import *

# Plotting tools
import matplotlib.pyplot as plt

# Symbolic and math tools
import sympy as sym
import numpy as np

class Robot:

    def __init__(self, variables, dh_table):
        self.variables = variables # symbolic variables
        self.dh_table = dh_table # dh-table

    # Variables
    robot_origin = [0,0,0,1]
    axis_limits = 4

    # calculate transformation-matrix from dh-table
    def calculate_transformation_matrices(self):

        transformation_n = [] # individual joint transformations
        transformations = [] # total joint transformations

        # first: calculate individual transformations from dh-table
        for row in self.dh_table:
            transformation_n.append(mm(rotZ(row[0]), mm(transZ(row[1]), mm(transX(row[2]), rotX(row[3])))))

        # second: calculate absolute transformation for each joint
        for i in range(len(transformation_n)):
            if (i == 0):
                transformations.append(transformation_n[0])
            else:
                transformations.append(np.dot(transformations[i-1], transformation_n[i]))

        return transformations


    # calculate end effector from variable values
    def forward_kinematics(self, variable_values=[0, 0, 0]):

        # get transformations
        transformations = self.calculate_transformation_matrices()
        point_expr = []
        points = [self.robot_origin[:-1]] # points for each joint in xyz-coordinates

        # iterate through transformations and calculate joint points
        for transform in transformations:
            point = []
            point_expr = np.dot(transform, self.robot_origin)

            # calculate x coordinate
            func_x = sym.lambdify(self.variables, point_expr[0], "numpy")
            point.append(func_x(*variable_values))

            # calculate y coordinate
            func_y = sym.lambdify(self.variables, point_expr[1], "numpy")
            point.append(func_y(*variable_values))

            # calculate z coordinate
            func_z = sym.lambdify(self.variables, point_expr[2], "numpy")
            point.append(func_z(*variable_values))

            # append points to list of points
            points.append(point)

        return points

    def inverse_kinematics(self):
        return None

    def plot(self, variable_values=[0, 0, 0]):

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        points = self.forward_kinematics(variable_values) # get joint coordinates from variables values

        # Plot-settings
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')

        ax.set_xlim([-self.axis_limits,self.axis_limits])
        ax.set_ylim([-self.axis_limits,self.axis_limits])
        ax.set_zlim([-self.axis_limits,self.axis_limits])

        for point in range(len(points)-1):
            ax.plot([points[point][0]], [points[point][1]], [points[point][2]], marker=".", markersize=13, label='test point', color="grey", zorder=10) # plot joint
            ax.plot([points[point][0], points[point+1][0]], [points[point][1], points[point+1][1]], [points[point][2], points[point+1][2]], color="black", zorder=1) # plot link

        plt.show()

    def animate(self, robot_angles, path, loop=False):

        fig = plt.figure(figsize=(10, 8))
        ax = fig.gca(projection='3d')

        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')

        path_index = 1
        for angle in robot_angles:
            # get joint points from forward kinematic
            points = self.forward_kinematics(angle)
            
            # plot path
            ax.plot(path[0][:path_index], path[1][:path_index], path[2][:path_index])
            path_index += 1 

            # plot links and joints
            for point in range(len(points)-1):
                ax.plot([points[point][0]], [points[point][1]], [points[point][2]], marker=".", markersize=13, label='test point', color="grey", zorder=10) # plot joint
                ax.plot([points[point][0], points[point+1][0]], [points[point][1], points[point+1][1]], [points[point][2], points[point+1][2]], color="black", zorder=1) # plot link

            ax.set_xlim([-self.axis_limits,self.axis_limits])
            ax.set_ylim([-self.axis_limits,self.axis_limits])
            ax.set_zlim([-self.axis_limits,self.axis_limits])

            # update plot
            if (angle != robot_angles[-1]):
                plt.draw()
                plt.pause(0.005)
                plt.cla()
                
        plt.show()
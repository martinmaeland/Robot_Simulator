from library.tools import *
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sympy as sym
import numpy as np
import math

class Robot:

    def __init__(self):
        self.dh_table = [] # this contains the dh-table
        self.t_n = [] # this will contain all t_n matrices
        self.t_matrix = [] # this will be the t-matrix


    def generate_dh_table(self, dh):
        for row in dh:
            self.dh_table.append(row)

    def generate_t_matrix(self):
        t_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

        for row in self.dh_table:
            self.t_n.append(mm(rotZ(row[0]), mm(transZ(row[1]), mm(transX(row[2]), rotX(row[3])))))

        for i in range(len(self.t_n)):
            t_matrix = mm(self.t_n[-(i+1)], t_matrix)

        self.t_matrix = t_matrix


    def plot(self):

        q1, q2 = sym.symbols("q1 q2")

        # Initiate figure
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Initial values
        #last_point = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        last_point = self.t_n[0]
        current_point = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        last_xyz = [0,0,0]

        # Plotting data
        #for i in (range(len(self.t_n))):
        for i in (range(len(self.t_n))):

            #current_point = mm(self.t_n[-(i+1)], last_point)
            current_point = mm(last_point, current_point)

            f = sym.lambdify([q1, q2], current_point[0][3], "numpy")
            x = f(0, 0)
            print("x_{}: {}".format(i,x))
            g = sym.lambdify([q1, q2], current_point[1][3], "numpy")
            y = g(0, 0)
            print("y_{}: {}".format(i,y))
            h = sym.lambdify([q1, q2], current_point[2][3], "numpy")
            z = h(0, 0)
            print("z_{}: {}".format(i,z))

            ax.plot([last_xyz[0], x], [last_xyz[1], y], [last_xyz[2], z], color="black", zorder=1)
            ax.plot([x], [y], [z], marker=".", markersize=13, label='test point', color="grey", zorder=10)

            last_point = current_point
            if i != (len(self.t_n)-1):
                current_point = self.t_n[i+1]
            last_xyz = [x,y,z]

        # Plot-settings and show
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')

        axis_limts = 2

        ax.set_xlim(-axis_limts,axis_limts)
        ax.set_ylim(-axis_limts,axis_limts)
        ax.set_zlim(-axis_limts,axis_limts)

        plt.show()

# Homemade functions
from library.tools import *

# Plotting tools
import matplotlib.pyplot as plt
from celluloid import Camera
from mpl_toolkits import mplot3d

# Symbolic and math tools
import sympy as sym
from sympy.solvers import solve
import numpy as np
import math

class Robot:

    def __init__(self):
        self.variables = [] # this is all the variables
        self.variable_values = [] #this is current variable values
        self.dh_table = [] # this represents dh-table
        self.t_n = [] # this contains all t_n matrices
        self.t_matrix = [] # this is the t-matrix

    def initiate_variables(self, vars):
        for var in vars:
            var = sym.symbols("{}".format(var))
            self.variables.append(var)

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

    def plot(self, var_values):

        # Initiate figure
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Initial values
        last_point = self.t_n[0]
        current_point = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
        last_xyz = [0,0,0]
        x = y = z = 0
        axis_limits = 1

        # Plotting data
        for i in (range(len(self.t_n))):

            current_point = mm(last_point, current_point)


            f = sym.lambdify(self.variables, current_point[0][3], "numpy") # define function x = f(variables)
            x = f(*var_values) # calcualte x

            g = sym.lambdify(self.variables, current_point[1][3], "numpy") # define function y = g(variables)
            y = g(*var_values) # calculate y

            h = sym.lambdify(self.variables, current_point[2][3], "numpy") # define function z = h(variables)
            z = h(*var_values) # calculate z

            ax.plot([x], [y], [z], marker=".", markersize=13, label='test point', color="grey", zorder=10) # plot joint
            ax.plot([last_xyz[0], x], [last_xyz[1], y], [last_xyz[2], z], color="black", zorder=1) # plot link

            if (n := max([x,y,z])) > axis_limits:
                axis_limits = 1.5*n

            last_point = current_point
            if i != (len(self.t_n)-1):
                current_point = self.t_n[i+1]
            last_xyz = [x,y,z]

        # Plot-settings and show
        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')

        ax.set_xlim(-axis_limits,axis_limits)
        ax.set_ylim(-axis_limits,axis_limits)
        ax.set_zlim(-axis_limits,axis_limits)

        plt.show()

    def animate(self):

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        camera = Camera(fig)

        t = np.linspace(0, 2*np.pi, 128, endpoint=False)

        for i in t:

            a = i
            b = -a

            # Initial values
            last_point = self.t_n[0]
            current_point = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
            last_xyz = [0,0,0]

            # Plotting data
            for i in (range(len(self.t_n))):

                current_point = mm(last_point, current_point)

                f = sym.lambdify(self.variables, current_point[0][3], "numpy") # define function x = f(variables)
                x = f(a, b) # calcualte x

                g = sym.lambdify(self.variables, current_point[1][3], "numpy") # define function y = g(variables)
                y = g(a, b) # calculate y

                h = sym.lambdify(self.variables, current_point[2][3], "numpy") # define function z = h(variables)
                z = h(a, b) # calculate z

                ax.plot([last_xyz[0], x], [last_xyz[1], y], [last_xyz[2], z], color="black", zorder=1) # plot link
                ax.plot([x], [y], [z], marker=".", markersize=13, label='test point', color="grey", zorder=10) # plot joint

                last_point = current_point
                if i != (len(self.t_n)-1):
                    current_point = self.t_n[i+1]
                last_xyz = [x,y,z]

            camera.snap()

        anim = camera.animate(interval=50, blit=True)
        anim.save('media/robot_01.gif', writer='imagemagick')

import sympy as sym

class Robot:

    def __init__(self):
        self.dh_table = [] # this contains the dh-table for the robot
        self.t_matrix = [] # this will be the t-matrix

    def rotZ(self, theta):
        # Add edge cases as in MATLAB
        c = sym.cos(theta)
        s = sym.sin(theta)
        return [[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    def transZ(self, z):
        return [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, z], [0, 0, 0, 1]]

    def transX(self, x):
        return [[1, 0, 0, x], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    def rotX(self, theta):
        # Add edge cases as in MATLAB
        c = sym.cos(theta)
        s = sym.sin(theta)
        return [[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]]

    def get_t_matrix(self):
        pass

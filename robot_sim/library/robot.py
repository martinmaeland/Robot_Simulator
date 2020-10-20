from library.calculations import *
import math

class Robot:

    def __init__(self):
        self.dh_table = [] # this contains the dh-table
        self.t_matrix = [] # this will be the t-matrix

    def generate_dh_table(self, dh):
        for row in dh:
            self.dh_table.append(row)

    def generate_t_matrix(self):
        t_n = []
        t_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

        for row in self.dh_table:
            t_n.append(mm(rotZ(row[0]), mm(transZ(row[1]), mm(transX(row[2]), rotX(row[3])))))

        for i in range(len(t_n)):
            t_matrix = mm(t_n[-(i+1)], t_matrix)

        self.t_matrix = t_matrix

    def plot(self):
        # will plot the robot
        pass

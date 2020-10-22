from library.robot import Robot
from sympy import symbols
import sympy as sym
import math

# test

# Define symbolic variables
q1, q2 = symbols("q1 q2")

# Define link lengths
l1 = 0.5
l2 = 1

# Define DH-table
dh_1 = [q1, 0, l1, 0]
dh_2 = [q2, 0, l2, 0]

dh = [dh_1, dh_2]

# Define robot
robot = Robot()
robot.generate_dh_table(dh)
robot.generate_t_matrix()

X = robot.t_matrix[0][3]
Y = robot.t_matrix[1][3]
Z = robot.t_matrix[2][3]

robot.plot()

from library.robot import Robot
from library.tools import *
from sympy import symbols
import sympy as sym
import math

# Define symbolic variables
q1, q2 = symbols("q1 q2")

# Define link lengths
l1 = 1
l2 = 1

# Define DH-table
dh_1 = [q1 + 0.7853981634, 0, l1, 0]
dh_2 = [q2 - 0.7853981634, 0, l2, 0]

dh = [dh_1, dh_2]

# Define robot
robot = Robot()
robot.generate_dh_table(dh)
robot.generate_t_matrix()
robot.plot()

# TESTING

t1 = mm(rotZ(0.7853981634), transX(l1))
t2 = transX(l2)
T = mm(t1,t2)

print(robot.t_n[0])
print(t1)

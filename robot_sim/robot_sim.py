from library.robot import Robot
from library.robotMath import *
from sympy import symbols
import math

# Define symbolic variables
q1, l1, d1 = symbols('q1 l1 d1')

# Define DH-table
dh_1 = [q1, 0, l1, 0]
dh_2 = [-45, 0, 0, -90]
dh_3 = [0, d1, 0, 0]

dh = [dh_1, dh_2, dh_3]

# Define t-matrices
t_1 = mm(rotZ(q1), mm(transZ(0), mm(transX(l1), rotX(0))))
t_2 = mm(rotZ(-math.pi/4), mm(transZ(0), mm(transX(0), rotX(-math.pi/2))))
t_3 = mm(rotZ(0), mm(transZ(d1), mm(transX(0), rotX(0))))
t = mm(t_1, mm(t_2, t_3))

x = t[0][3]
print(x)

# Define robot
robot = Robot()
robot.generate_dh_table(dh)
robot.generate_t_matrix()

x = robot.t_matrix[0][3]
print(x)

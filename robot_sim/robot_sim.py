from library.robot import Robot
from sympy import symbols
import math

# Define symbolic variables
q1, l1, d1 = symbols('q1 l1 d1')

# Define DH-table
dh_1 = [q1, 0, l1, 0]
dh_2 = [-math.pi/4, 0, 0, -math.pi/2]
dh_3 = [0, d1, 0, 0]

dh = [dh_1, dh_2, dh_3]

# Define robot
robot = Robot()
robot.generate_dh_table(dh)
robot.generate_t_matrix()

x = robot.t_matrix[0][3]
print(x)

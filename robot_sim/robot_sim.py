from robot.robot import Robot
from sympy import symbols
import math

# Define robot
robot = Robot()

# Define symbolic variables
q1, l1, d1 = symbols('q1 l1 d1')

# Define DH-table and append to robot
dh_1 = [q1, 0, l1, 0]
dh_2 = [-45, 0, 0, -90]
dh_3 = [0, d1, 0, 0]

dh = [dh_1, dh_2, dh_3]

for row in dh:
    robot.dh_table.append(row)

# Define t-matrices
t_1 = robot.rotZ(dh_1[0] * robot.transZ(dh_1[1]) * robot.transX(dh_1[2]) * robot.transX(dh_1[3])
print(t_1)

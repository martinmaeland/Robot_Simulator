from library.robot import Robot
#from library.tools import *
from sympy import symbols
#import sympy as sym
#import math

#----ROBOT 1----
# Define symbolic variables
q1, q2 = symbols("q1 q2")
variables = [q1, q2]

# Define link lengths
l1 = 1
l2 = 1

# Define DH-table
dh_1 = [q1 + 0.7853981634, 0, l1, 0]
dh_2 = [q2 - 0.7853981634, 0, l2, 0]
dh = [dh_1, dh_2]

# Give variables some values
values = [0, 0]

# Define robot
robot = Robot()
robot.initiate_variables(variables)
robot.generate_dh_table(dh)
robot.generate_t_matrix()
robot.plot(values)


#----ROBOT2----
# Define symbolic variables
q1, d1 = symbols("q1 d1")
variables_2 = [q1, d1]

# Define DH-table
dh2_1 = [q1, 0, l1, 0]
dh2_2 = [-0.785398163, 0, 0, -1.57079633]
dh2_3 = [0, d1, 0, 0]
dh2 = [dh2_1, dh2_2, dh2_3]

# Give variables some values
values_2 = [0.1, 2]

# Define test robot
robot2 = Robot()
robot2.initiate_variables(variables_2)
robot2.generate_dh_table(dh2)
robot2.generate_t_matrix()
robot2.plot(values_2)

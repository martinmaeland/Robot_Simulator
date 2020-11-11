from library.robot import Robot
from library.tools import *
from sympy import symbols

# Define symbolic variables
q1, q2, q3 = symbols("q1 q2 q3")
variables = [q1, q2, q3]

# Define link lengths
l1 = 1.5
l2 = 1.5
l3 = 1

# Define DH-table
dh_1 = [q1, l1, 0.0, degToRad(90)]
dh_2 = [q2+degToRad(45.0), 0.0, l2, 0.0]
dh_3 = [q3-degToRad(60), 0.0, l3, degToRad(90)]
dh = [dh_1, dh_2, dh_3]

# Give variables some values
values = [0, 0, 0] # [q1, q2]

# Define robot
robot = Robot()
robot.initiate_variables(variables)
robot.generate_dh_table(dh)
robot.generate_t_matrix()
#robot.plot(values)
#robot.animate()

for i in range(3):
    print(robot.get_p_vector()[i])

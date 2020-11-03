from library.robot import Robot
from sympy import symbols


# Define symbolic variables
q1, q2 = symbols("q1 q2")
variables = [q1, q2]

# Define link lengths
l1 = 1
l2 = 1

# Define DH-table
dh_1 = [q1, 0, l1, 0] # 45deg in rad = 0.7853981634
dh_2 = [q2, 0, l2, 0]
dh = [dh_1, dh_2]

# Give variables some values
values = [0, 0]

# Define robot
robot = Robot()
robot.initiate_variables(variables)
robot.generate_dh_table(dh)
robot.generate_t_matrix()
#robot.animate() # does not work properly
robot.plot(values)

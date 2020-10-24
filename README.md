# Robot Simulator
This code will simulate robot from DH-table.

Does work with python 3.8.

## TODO
- Improve sleekness of creating a robot instance
- Create inverse-kinematics function
-

## Roadmap
. Take DH-table input, calculate all t_n matrices and T matrix.
. Plot all joints and links based on inital values.
. Calculate inverse-kinematics.
. Input point-cloud and calculate robot trajectory.
. Animate robot. 

## Status
Able to plot robot from DH-table, with given initial values.

## Creating a robot example

```python
from library.robot import Robot
from sympy import symbols

# Define symbolic variables
q1, q2 = symbols("q1 q2")
variables = [q1, q2]

# Define link lengths
l1 = 1
l2 = 2

# Define DH-table
dh_1 = [q1, 0, l1, 0]
dh_2 = [q2, 0, l2, 0]
dh = [dh_1, dh_2]

# Give variables some values
values = [0, 0] # [q1, q2]

# Define robot
robot = Robot()
robot.initiate_variables(variables)
robot.generate_dh_table(dh)
robot.generate_t_matrix()
robot.plot(values)
```

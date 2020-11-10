# Robot Simulator
The goal is to create instance of a robot from DH-table and simulate robot trajectory from given points.

Currently using python 3.8.

## Roadmap
[X] Take DH-table input, calculate all t_n matrices and t-matrix
[X] Plot all joints and links based on inital values
[ ] Calculate inverse-kinematics
[ ] Input point-cloud and calculate robot trajectory
[ ] Animate robot

## Status
Able to plot robot from DH-table, with given initial values.
![robot_01](https://github.com/martinmaeland/Robot_Simulator/blob/master/media/robot_01.png)

Animation of robot where q1 is element in [0, 2*pi] and q2 = -q1 . (For now this only works with manual input of range).

![robot_01](https://github.com/martinmaeland/Robot_Simulator/blob/master/media/robot_01.gif)

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
robot.animate()
```

## TODO
[ ] Clean up code, aka make it simpler to create robot instance
[ ] Calculate inverse-kinematics from t-matrix

## Thoughts
* The dots represents the joints. Should the base have a dot as well?
* The tip represents the tool. Should the tool be represented as end of link?


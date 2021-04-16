# Robot Simulator
The goal is to create instance of a robot from DH-table and simulate robot trajectory from given points.

## Plan
Done:
- [x] Take DH-table input, calculate all t_n matrices and t-matrix
- [x] Plot all joints and links based on inital values
- [x] Input path and calculate robot trajectory
- [x] Animate robot
- [x] Plot line where robot has been
- [x] Create external path from inkscape or similar and import it for robot to follow

Next:

Maybe in the future:
- [ ] Simplify creating a robot instance (works for now, but effort)
- [ ] Calculate inverse-kinematics (hard)

## Status
* Plot robot from dh table with given symbolic variables.
* Add inverse kinematics manually and with a point-based path animate the robot.

![](https://github.com/martinmaeland/Robot_Simulator/blob/master/res/robot_example_custom_path.png)

(date: 16.04.21)

Video of robot can be seen here: [/res](res)

![](https://github.com/martinmaeland/Robot_Simulator/blob/master/res/robot_example.png)

(date: )

## Setting up the workspace

1. Clone repo.
2. Install dependencies (from root folder):
```
tools/install_dependencies.sh
```
> Note: you may need to make the script an executable using `sudo chmod +x tools/install_dependencies.sh`.

3. Follow example in `test` folder.

## Updates
Written updates from sessions. Easier to look back at changes this way.

Update 16.03.21:
Custom path now supported. The path generator tools is provisional and unwanted manual work is required for things to work.

Update 11.04.21:
I think the inverse-kinematics problems are fixed. The animation method now does one simulation of the robot following the given path, however, the save figure function is currently unavailable (will look into this later, but cooler to see it 'live'). The inverse kinematics and path points needs to be generated manually; because of this the animation method needs an array with all the angles calculated from the inverse kinematics function and the path points.


# Robot Simulator
The goal is to create instance of a robot from DH-table and simulate robot trajectory from given points.

Currently using python 3.8.

## Plan
Done:
- [x] Take DH-table input, calculate all t_n matrices and t-matrix
- [x] Plot all joints and links based on inital values
- [x] Input path and calculate robot trajectory
- [x] Animate robot

Next:
- [ ] Plot line where robot has been
- [ ] Create external path from inkscape or similar and import it for robot to follow

Maybe in the future:
- [ ] Simplify creating a robot instance (works for now, but effort)
- [ ] Calculate inverse-kinematics (hard)

## Status
* Plot robot from dh table with given symbolic variables.
* Add inverse kinematics manually and with a point-based path animate the robot.

Video of robot can be seen here: [/res](res)

![](https://github.com/martinmaeland/Robot_Simulator/blob/master/res/robot_example.png)

## Setting up the workspace

1. Clone repo.
2. Install dependencies (from root folder):
```
tools/install_dependencies.sh
```
> Note: you may need to make the script an executable using `sudo chmod +x tools/install_dependencies.sh`.

3. Follow example in `test` folder.

## Thoughts

## TODO
- [ ] Check up on inverse kinematics solution, something seems off.

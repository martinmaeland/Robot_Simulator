# Robot Simulator
The goal is to create instance of a robot from DH-table and simulate robot trajectory from given points.

Currently using python 3.8.

## Roadmap

- [x] Take DH-table input, calculate all t_n matrices and t-matrix
- [x] Plot all joints and links based on inital values
- [ ] Calculate inverse-kinematics
- [ ] Input point-cloud and calculate robot trajectory
- [ ] Animate robot

## Status
Able to pot robot from DH-table, with given initial values. Animation of robot where q1 is element in [0, 2*pi] and q2 = -q1 . (For now this only works with manual input of range). 

<p float="left">
  <img src="https://github.com/martinmaeland/Robot_Simulator/blob/master/res/robot_example.png" width="400" />
  <img src="https://github.com/martinmaeland/Robot_Simulator/blob/master/res/robot_example.mp4" width="400" /> 
</p>

## Setting up the workspace

1. Clone repo.
2. Install dependencies (from root folder):
```
tools/install_dependencies.sh
```
> Note: you may need to make the script an executable using `sudo chmod +x tools/install_dependencies.sh`.

3. Follow example in `test` folder.

## Thoughts
* The dots represents the joints. Should the base have a dot as well?
* The tip represents the tool. Should the tool be represented as end of link?

## TODO
- [ ] Clean up code
  - [ ] Make it simpler to create robot instance
- [ ] Calculate inverse-kinematics from t-matrix

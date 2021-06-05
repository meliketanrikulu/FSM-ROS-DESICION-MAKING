# FSM-ROS-DESICION-MAKING
## Package Description
This package contains a simple FSM (Finite State Machine) implementation using smach (ROS-Melodic). In the Gazebo simulation environment, it is aimed for the robot to move away from obstacles by using lidar data. Tested using Turtlebot3. It is recommended to use Turtlebot3 for testing.

### Installation
* $ cd ~/catkin_ws/src/
* $ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
* $ git clone git@github.com:meliketanrikulu/FSM-ROS-DESICION-MAKING.git
* $ sudo apt install ros-melodic-smach-viewer

### Run it with Turlebot3
* $ cd ~/catkin_ws && catkin_make
* $ export TURTLEBOT3_MODEL=burger
* $ roslaunch turtlebot3_gazebo turtlebot3_world.launch
* $ rosrun desicion_making fsm.py
* $ rosrun smach_viewer smach_viewer.py

### Resources
* https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/
* http://wiki.ros.org/smach
* http://wiki.ros.org/smach/Tutorials

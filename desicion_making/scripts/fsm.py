#!/usr/bin/env python

import rospy
import smach 
import smach_ros
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from smach import CBState

random_scan = 0.0 
msg = Twist()
@smach.cb_interface(input_keys = [], output_keys = [], outcomes = ["go", "escape"])
def straight_cb(user_data):
	global msg
	global random_scan
	msg.linear.x = 0.3
	msg.angular.z = 0
	cmd_topic.publish(msg)
	rospy.loginfo("random_scan = %f", random_scan)
	if random_scan > 0.7:
		return "go"
	else:
		return "escape"


@smach.cb_interface(input_keys = [], output_keys = [], outcomes = ["go", "escape"])
def turning_cb(user_data):
	global random_scan
	global msg
	msg.linear.x = 0
	msg.angular.z = 0.5
	cmd_topic.publish(msg)
	if random_scan > 0.7:
		return "go"
	else:
		return "escape"


def callback(scan_msg):
	global random_scan
	random_scan = scan_msg.ranges[0]
	rospy.loginfo(random_scan)


if __name__ == "__main__":

	rospy.init_node("finite_state_machine")
	scan_sub = rospy.Subscriber("/scan", LaserScan, callback)
	cmd_topic  = rospy.Publisher("/cmd_vel", Twist,queue_size = 1)

	sm = smach.StateMachine(outcomes = ["FINISH"])

	with sm:
		smach.StateMachine.add("STRAIGHT",CBState(straight_cb), {"go":"STRAIGHT", "escape":"TURNING"})
		smach.StateMachine.add("TURNING",CBState(turning_cb), {"go":"STRAIGHT", "escape":"TURNING"})

	sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
	sis.start()

	outcome = sm.execute()

	rospy.spin()
	sis.stop()

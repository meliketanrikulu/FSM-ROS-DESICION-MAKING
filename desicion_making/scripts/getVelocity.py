#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState

class Velocity:
    def __init__(self):
        self.on_sol = 0
        self.on_sag = 0
    def joint_states_callback(self,message):
        self.arka_sag = message.velocity[0] 
        #print "arka_sag = ",self.arka_sag
        self.arka_sol = message.velocity[1] 
        #print "arka_sol = ",self.arka_sol
        self.on_sag = message.velocity[2] 
        #print "on_sag = ",self.on_sag
        self.on_sol = message.velocity[3]                       
        #print "on_sol = ",self.on_sol

        
    def listener(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/joint_states", JointState, self.joint_states_callback)
        


#p1 = getVelocity()
#p1.listener()
#!/usr/bin/env python
from getVelocity import Velocity
import rospy

def main():
    p1 = Velocity()
    while not rospy.is_shutdown():
        p1.listener()
        hiz = (p1.on_sol + p1.on_sag) / 2
        print hiz

if __name__ == '__main__':
    main()
    #rospy.spin()
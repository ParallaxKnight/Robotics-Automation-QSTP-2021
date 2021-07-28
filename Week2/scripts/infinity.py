#!/usr/bin/env python

from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
import rospy
from numpy import pi, sin, cos , absolute

rospy.init_node('infinity')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

n = 200
dt = pi/n
rate = rospy.Rate(1/(14.7*dt))


while not rospy.is_shutdown():
    path = Twist()
    path.linear.x = 0.1
    c = -2
    while(c<n+1):
        theta = c*dt
        domin = 3*(absolute(cos(2*theta)))**0.5
        radius = 1/domin

        if(c>51 and c<151):
            radius *=-1
        
        ang_vel = 0.1/radius

        path.angular.z = ang_vel
        pub.publish(path)
        print(c, radius, ang_vel)
        c+=1
        rate.sleep()
        




     

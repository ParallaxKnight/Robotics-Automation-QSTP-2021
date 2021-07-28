#!/usr/bin/env python
import sys
import rospy
from week2.srv import ang_vel, ang_velResponse
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist


def client(radius):
    rospy.wait_for_service('compute_ang_vel')
    try:
        server_call = rospy.ServiceProxy('compute_ang_vel', ang_vel)
        resp1 = server_call(radius)
        ang_velocity = resp1.angular_velocity
        rate = rospy.Rate(2)
        publish = rospy.Publisher('Turtle_Path', Float32, queue_size=1)
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
       
        while not rospy.is_shutdown():
            path = Twist()
            path.linear.x = 0.1
            path.angular.z = ang_velocity
            pub.publish(path)
       	    publish.publish(ang_velocity)
            rate.sleep()


    except rospy.ServiceException as e:
       print("Service call failed: %s"%e)

def subscribe():
	sub = rospy.Subscriber('radius', Float32, callback)
	rospy.spin()

def callback(msg):
	radius = msg.data
	client(radius)

if __name__ == "__main__":
	rospy.init_node('Turtle_Path')
	subscribe()




#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Point, Pose, PoseStamped, Quaternion, Twist
from numpy import pi, sqrt, sign
from tf.transformations import euler_from_quaternion
from math import atan2
from std_msgs.msg import String



x = 0.0
y = 0.0
theta = 0.0

goal_x = -0.1
goal_y = -0.1

def odom_data(msg):
   global x
   global y
   global theta

   x = msg.pose.pose.position.x
   y = msg.pose.pose.position.y

   rot_q = msg.pose.pose.orientation
   (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])


def path_coordinates(msg):
   global goal_x
   global goal_y

   goal_x = msg.pose.position.x
   goal_y = msg.pose.position.y



if __name__ == "__main__":
   rospy.init_node("turtlebot_spy")
   rate = rospy.Rate(30)
   rate2 = rospy.Rate(0.2)

   destination = Point()
   limit = 0
   count = 0
   speed = Twist()

   pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
   pub2 = rospy.Publisher('/found_you', String, queue_size=1)
   sub2 = rospy.Subscriber('/odom', Odometry, odom_data)


   while not rospy.is_shutdown():
      sub = rospy.Subscriber('/thief_pose', PoseStamped, path_coordinates)

      if destination.x != goal_x and destination.y != goal_y:
         destination.x = goal_x
         destination.y = goal_y
         limit +=1

      inc_x = destination.x - x
      inc_y = destination.y - y

      l_sq = inc_y**2 + inc_x**2

      l = sqrt(l_sq)

      angle_to_goal = atan2(inc_y, inc_x)

      angle_destination = (angle_to_goal - theta)

      print(l, angle_destination,limit, count)

      if l > 1.1:

         if abs(angle_destination) > 0.3:
            if abs(angle_destination) > 2:
               speed.angular.z = angle_destination/3

            elif abs(angle_destination) < 2:
               speed.angular.z = 0.15*sign(angle_destination)
   
            speed.linear.x = 0.0
            pub.publish(speed)
            
         elif abs(inc_x) > 0.05 or abs(inc_y) > 0.05:
            speed.linear.x = 0.25
            speed.angular.z = 0.0
            pub.publish(speed)
      else:

         speed.linear.x = 0.0
         speed.angular.z = 0.0
         pub.publish(speed)
         if count<limit:
            pub2.publish('Found you!!')
            count+=1


      rate.sleep()
      

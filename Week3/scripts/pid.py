#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import Point, Pose, PoseStamped, Quaternion, Twist
from numpy import pi
from tf.transformations import euler_from_quaternion
from math import atan2
import sys


x = 0.0
y = 0.0
z = 0.0

goal_x_array = []
goal_y_array = []

def odom_data(msg):
   global x
   global y
   global theta

   x = msg.pose.pose.position.x
   y = msg.pose.pose.position.y

   rot_q = msg.pose.pose.orientation
   (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def usage():
    return "%s [path1 or path2 or path3]"%sys.argv[0]

def path_coordinates(msg):
   global goal_x_array
   global goal_y_array

   temp_x = []
   temp_y = []
   for c in msg.poses:
      temp_x.append(c.pose.position.x) 
      temp_y.append(c.pose.position.y)

   if temp_x != goal_x_array:
      goal_x_array += temp_x
      goal_y_array += temp_y

   rate.sleep()


if __name__ == "__main__":
   rospy.init_node("pid")
   rate = rospy.Rate(10)
   sub2 = rospy.Subscriber('/odom', Odometry, odom_data)
   pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
   args = rospy.myargv(argv = sys.argv)
   if len(args) == 2:
      path_info = args[1]
      if "1" in path_info:
         sub = rospy.Subscriber('/path1', Path, path_coordinates)

      elif "2" in path_info:
         sub = rospy.Subscriber('/path2', Path, path_coordinates)

      elif "3" in path_info:
         sub = rospy.Subscriber('/path3', Path, path_coordinates)

      else:
         print(usage())
         sys.exit(1)

   else:
      print(usage())
      sys.exit(1)

   destination = Point()
   c = 0
   speed = Twist()

   while not rospy.is_shutdown():

      if(c<len(goal_x_array)):
         destination.x = goal_x_array[c]
         destination.y = goal_y_array[c]

         inc_x = destination.x - x
         inc_y = destination.y - y

         angle_to_goal = atan2(inc_y, inc_x)
         angle_destination = (angle_to_goal - theta)

         if angle_destination > pi:
            angle_destination -= 2*pi

         elif angle_destination < -pi:
            angle_destination += 2*pi   


         print(angle_destination, inc_x, inc_y)
         if abs(angle_destination) > 0.1:
            if angle_destination > 0:
               speed.angular.z = 0.2

            elif angle_destination < 0:
               speed.angular.z = -0.2
   
            speed.linear.x = 0.0
            pub.publish(speed)
            

         elif abs(inc_x) > 0.05 or abs(inc_y) > 0.05:
            speed.linear.x = 0.2
            speed.angular.z = 0.0
            pub.publish(speed)            

         else:
            speed.linear.x = 0.0
            speed.angular.z = 0.0
            pub.publish(speed)
            c+=1

      rate.sleep()











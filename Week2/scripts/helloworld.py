#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class HelloWorld:
    def __init__(self):
        self.pub = rospy.Publisher('helloworld', String, queue_size=1)
        self.sub1 = rospy.Subscriber('hello', String, self.callback1)
        self.sub2 = rospy.Subscriber('world', String, self.callback2)
        self.str = String()
        self.hello = None
        self.world = None
    
    def callback1(self,msg):
        self.hello = msg.data
        self.str = str(self.hello) + ', ' + str(self.world) + '!'
        self.pub.publish(self.str)

    def callback2(self,msg):
        self.world = msg.data
        self.str = str(self.hello) + ', ' + str(self.world) + '!'
        self.pub.publish(self.str)
        

if __name__ == "__main__":
    rospy.init_node('helloworld')
    name = HelloWorld()
    rospy.spin()
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class HelloWorld:
    def __init__(self):
        self.pub = rospy.Publisher('helloworld', String, queue_size=1)
        self.sub1 = rospy.Subscriber('hello', String, self.callback1)
        self.sub2 = rospy.Subscriber('world', String, self.callback2)
        self.message = String()
        self.hello = String()
        self.world = String()
        
    
    def callback1(self,msg):
        self.hello = msg.data


    def callback2(self,msg):
        self.world = msg.data
        self.printer()


    def printer(self):
        self.message = str(self.hello) + ', ' + str(self.world) + '!'
        if 'data' not in self.message:
            self.pub.publish(self.message)
            print(self.message)
        

if __name__ == "__main__":
    rospy.init_node('helloworld')
    name = HelloWorld()
    rospy.spin()

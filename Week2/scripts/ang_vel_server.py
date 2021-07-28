#!/usr/bin/env python

from week2.srv import ang_vel, ang_velResponse
import rospy

def velocity_calculator(req):
	radius = req.radius

	angular_velocity = 0.1/radius

	return ang_velResponse(angular_velocity)

def server():
	rospy.init_node('compute_ang_vel')
	s = rospy.Service('compute_ang_vel', ang_vel, velocity_calculator)
	rospy.spin()

if __name__ == "__main__":
    server()

#!/usr/bin/env python

from week2.srv import state, stateResponse
import rospy
import numpy as np

def coord(req):
    x = req.x
    y = req.y
    theta = req.theta
    dt = 0.05
    n = 50

    # Store the points of the trajectory to plot
    x_points = [x]
    y_points = [y]


    v = req.v
    w = req.w

    for c in range(1, n+1):
        time = dt*c

        theta = time*w
        x_ = x + np.cos(theta)*v*time
        y_ = y + np.sin (theta)*v*time

        x_points.append(x_)
        y_points.append(y_)

    return stateResponse(x_points, y_points)

def trajectory_server():
   rospy.init_node('trajectory_server')
   s = rospy.Service('trajectory', state, coord)
   rospy.spin()

if __name__ == "__main__":
    trajectory_server()
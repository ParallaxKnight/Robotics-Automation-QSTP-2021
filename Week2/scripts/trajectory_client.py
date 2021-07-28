#!/usr/bin/env python

import sys
import rospy
import matplotlib.pyplot as plt
from week2.srv import *

def trajectory_client(x, y, theta, v, w):
   rospy.wait_for_service('trajectory')
   try:
       trajectory = rospy.ServiceProxy('trajectory', state)
       resp1 = trajectory(x, y, theta, v, w)
       return resp1.x_points, resp1.y_points

   except rospy.ServiceException as e:
       print("Service call failed: %s"%e)

def usage():
    return "%s [x y theta v w]"%sys.argv[0]

def plot(v, w, x_points, y_points):
    print("plot")
    plt.title("Unicycle Model: "+str(v)+", "+str(w))
    plt.xlabel("X-Coordinates")
    plt.ylabel("Y-Coordinates")
    plt.plot(x_points, y_points, color="red", alpha=0.75)
    plt.grid()

    # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
    plt.show()
    # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
    # plt.savefig(f"Unicycle.png")

if __name__ == "__main__":
    if len(sys.argv) == 6:
       x = float(sys.argv[1])
       y = float(sys.argv[2])
       theta = float(sys.argv[3])
       v = float(sys.argv[4])
       w = float(sys.argv[5])

    else:
       print(usage())
       sys.exit(1)
    print("Requesting")
    x_points = []
    y_points = []
    x_points, y_points = trajectory_client(x, y, theta, v, w)
    plot(v, w, x_points, y_points )

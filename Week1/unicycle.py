"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):

        self.v = v
        self.w = w
        self.n = n

        dt = self.dt

        for c in range(1, n+1):
            time = dt*c

            theta = time*w
            x_ = self.x + np.cos(theta)*v*time
            y_ = self.y + np.sin (theta)*v*time

            self.x_points.append(x_)
            self.y_points.append(y_)


    # def plot(self, v: float, w: float):
    def plot(self):
        plt.title(f"Unicycle Model: {self.v}, {self.w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        plt.show()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        plt.savefig(f"Unicycle_{self.v}_{self.w}.png")

if __name__ == "__main__":

    print("Unicycle Model Assignment")
    model = int(input("1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25 \n2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10\n3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50\n:"))

if model ==1:
    run = Unicycle(0, 0, 0, 0.1)
    run.step(1, 0.5, 25)
    run.plot()

elif model == 2:
    run = Unicycle(0, 0, 1.57, 0.2)
    run.step(0.5, 1, 10)
    run.plot()

elif(model ==3):
    run = Unicycle(0, 0, 0.77, 0.05)
    run.step(5, 4, 50)
    run.plot()

else:
    print("Enter 1, 2, or 3")
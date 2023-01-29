import pandas as pd
import numpy as np
from manim import *

# scene 1
class ThreeBox(ThreeDScene):
    def construct(self):

        pos = np.array(pd.read_csv("ideal_gas/pos.csv"))[1:, 1:]
        vel = np.array(pd.read_csv("ideal_gas/vel.csv"))[1:, 1:]


        axes = ThreeDAxes(
                x_range=[0, 200*10**(0.5), 1], 
                y_range=[0, 200*10**(0.5), 1], 
                z_range=[0, 200*10**(0.5), 1], 
                x_length=5, 
                y_length=5,
                z_length=5, 
                axis_config={"color": WHITE},  
                tips=False).to_edge(DOWN)

        def plot_particles():
            particles = []
            for i in range(10):
                particles.append(Sphere(axes.coords_to_point(
                    *(pos[int(tracker.get_value()), 3 * i: 3 * i + 3])), radius=0.065)) 

            return VGroup(*particles)

        def plot_histogram():

            vx = vel[int(tracker.get_value()), ::2]

            data, bins = np.histogram(vx, bins=np.arange(-10, 10))

            return BarChart(values=data, y_range=[0, 300])


        

        #box = Square(side_length=5.02).move_to(axes.coords_to_point(100*10**(0.5), 100*10**(0.5)))
        #self.add(box)

        tracker = ValueTracker(0)
        print(pos)

        #chart = always_redraw(plot_histogram)

        pog = always_redraw(plot_particles)

        self.add(pog)

        #self.add(chart)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.add(axes)
        
        self.play(tracker.animate.set_value(pos.shape[0] - 1), 
            rate_func=rate_functions.linear,
            run_time = 2.5)

        
import pandas as pd
import numpy as np
from manim import *

f=0.9

# scene 1
class Prototype(Scene):
    def construct(self):

        pos = np.array(pd.read_csv("ideal_gas/pos.csv"))[1:, 1:]
        vel = np.array(pd.read_csv("ideal_gas/vel.csv"))[1:, 1:]

        print(np.sum(pos == 0))

        axes = Axes(
                x_range=[0, 200, 1], 
                y_range=[0, 200, 1], 
                x_length=5*f, 
                y_length=5*f, 
                axis_config={"color": WHITE},  
                tips=False).to_edge(DOWN).to_edge(LEFT)

        def plot_particles():

            particles = []

            for i in range(0, pos.shape[1], 2):
                particles.append(Dot(axes.coords_to_point(
                    *(pos[int(tracker.get_value()), i: i + 2])), radius=0.065*f, color=BLUE)) 
                print(pos[int(tracker.get_value()), i: i + 2])

            return VGroup(*particles)

        def plot_histogram():

            vx = vel[int(tracker.get_value()), ::2]

            data, bins = np.histogram(vx, bins=np.arange(-7, 7))

            chart = BarChart(values=data, y_range=[0, 30, 10], x_length=5, y_length=2.5, bar_width=1, 
                bar_stroke_width=0, y_axis_config={"font_size": 22})\
                .next_to(box, UP)

            labels = chart.get_bar_labels(font_size=22)

            return VGroup(chart, labels)
        
        def plot_histogram2():

            vy = vel[int(tracker.get_value()), 1::2]

            data2, bins2 = np.histogram(vy, bins=np.arange(-7, 7))

            chart2 = BarChart(values=data2, y_range=[0, 30, 10], x_length=5, y_length=2.5, bar_width=1, 
                bar_stroke_width=0, y_axis_config={"font_size": 22})\
                .next_to(box, UP, buff=-3).to_edge(RIGHT)

            labels2 = chart2.get_bar_labels(font_size=22)

            return VGroup(chart2, labels2)
        

        box = Square(side_length=5.05*f).move_to(axes.coords_to_point(100, 100))
        self.add(box)

        tracker = ValueTracker(0)
        print(pos)

        pog = always_redraw(plot_particles)

        chart = always_redraw(plot_histogram)
        chart2 = always_redraw(plot_histogram2)

        self.add(pog)

        self.add(chart)
        self.add(chart2)
        
        self.play(tracker.animate.set_value(pos.shape[0] - 1), 
            rate_func=rate_functions.linear,
            run_time = 35)
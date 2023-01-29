from manim import *
import numpy as np
import pandas as pd


# scene 1
class Scene1(Scene):
    def construct(self):

        num_particles = 100
        box_size = 200
        box_size_manim = 5

        pos = np.array(pd.read_csv("ideal_gas/pos.csv"))[1:, 1:]
        vel = np.array(pd.read_csv("ideal_gas/vel.csv"))[1:, 1:]

        def plot_simulation():
            box = Square(side_length=box_size_manim)\
                .move_to(axes.coords_to_point(box_size/2, box_size/2))
            particles = get_particles()
            return VGroup(box, *particles)
            
        def get_particles():
            particles = []
            for i in range(0, pos.shape[1], 2):
                particles.append(Dot(axes.coords_to_point(
                    *(pos[int(tracker.get_value()), i: i + 2])), 
                    radius=(2/box_size)*box_size_manim, 
                    color=BLUE))
            return particles
        
        #
        tracker = ValueTracker(0)

        #
        axes = Axes(
                x_range=[0, 200], 
                y_range=[0, 200], 
                x_length=5, 
                y_length=5, 
                axis_config={"color": WHITE},  
                tips=False)

        a = always_redraw(plot_simulation)
        dot = Dot(axes.coords_to_point(0, 0), radius=0.1)

        self.add(a)
        self.play(tracker.animate.set_value((pos.shape[0] - 1)/30), 
            rate_func=rate_functions.linear,  
            run_time=2)
        self.play(a.animate.scale(0.5), run_time=1)
        self.play(tracker.animate.set_value((pos.shape[0] - 1)/30 + 100), 
            rate_func=rate_functions.linear,  
            run_time=2)
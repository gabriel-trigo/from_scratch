# imports
import numpy as np
from manim import *

# scene 2
class Scene3(Scene):
    def construct(self):

        # static constants
        v0 = 10.0
        g = 10
        theta = np.pi / 4 + 0.2

        # trajectory function
        def trajectory_func(x):
            return np.tan(theta)*x-g*x**2/(2*(v0*np.cos(theta))**2)

        # trajectory curve and dot
        def draw_curve_and_dot():
            graph = axes.plot(
                trajectory_func, 
                x_range=[0, tracker.get_value()], 
                color=BLUE)
            dot = Dot(
                axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                color=PINK)
            return VGroup(graph, dot)

        # axes
        axes = Axes(
                x_range=[-4, 4, 1], 
                y_range=[0, 4, 1], 
                x_length=7.0, 
                y_length=5.0, 
                axis_config={"color": WHITE}, 
                x_axis_config={"numbers_with_elongated_ticks": np.arange(-4, 6, 2)}, 
                tips = False)

        # tracker
        tracker = ValueTracker(0)

        # angle and the lines that describe it
        line_1 = Line(axes.coords_to_point(0, 0), axes.coords_to_point(1, 0))
        line_2 = Line(axes.coords_to_point(0, 0), axes.coords_to_point(np.cos(theta), np.sin(theta)))
        angle = Angle(line_1, line_2, radius=0.3)
        angle_label = MathTex("\\theta").move_to(
            Angle(
                line_1, 
                line_2, 
                radius=1.0, 
                other_angle=False).point_from_proportion(0.7))

        # arrows
        speed_arrow = Arrow(
            start=axes.coords_to_point(0, 0), 
            end=axes.coords_to_point(2*np.cos(theta), 2*np.sin(theta)), 
            color=YELLOW, 
            buff=0)
        speed_arrow_label = MathTex("v_0").next_to(speed_arrow, UP)

        # always redraw
        curve = always_redraw(draw_curve_and_dot)

        # origin dot
        origin_dot = Dot(axes.coords_to_point(0, 0))

        # animations
        self.wait(2)
        self.add(axes, curve, origin_dot)
        self.play(FadeIn(axes, origin_dot))
        self.wait(2)
        self.play(tracker.animate.set_value(2.7))
        self.wait(1)
        self.add(angle, angle_label, axes, curve, origin_dot)
        self.play(FadeIn(angle, angle_label))
        self.wait(2)
        self.add(speed_arrow, speed_arrow_label, origin_dot)
        self.play(FadeIn(speed_arrow), FadeIn(speed_arrow_label))
        self.wait(4)
        self.play(FadeOut(axes, curve, origin_dot, angle, angle_label, speed_arrow, speed_arrow_label))
        self.wait(2)
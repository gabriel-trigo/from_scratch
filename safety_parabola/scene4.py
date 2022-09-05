import numpy as np
from manim import *

class Scene4(Scene):
    def construct(self):

        # constants
        v0 = 9.6
        g = 10

        # get safety parabola
        def get_safety_parabola():
            graph = axes.plot(lambda x: v0 ** 2 / (2 * g) - g * x ** 2 / (2 * v0 ** 2), x_range = [-10, 10], color = PINK)
            return graph

        tracker_x = ValueTracker(2)
        tracker_y = ValueTracker(2)

        def get_solution_parabola():
            a = 1
            b = -2 * v0 ** 2 / (g * tracker_x.get_value())
            c = 1 + 2 * v0 ** 2 * tracker_y.get_value() / (g * tracker_x.get_value() ** 2)
            graph = other_axes.plot(lambda t: t ** 2 - 2 * v0 ** 2 / (g * tracker_x.get_value()) * t + (1 + 2 * v0 ** 2 * tracker_y.get_value() / (g * tracker_x.get_value() ** 2)), 
            x_range = [-b / (2*a) - 2.3, -b / (2*a) + 2.3])
            return graph

        def get_point():
            return Dot(axes.coords_to_point(tracker_x.get_value(), tracker_y.get_value()))

        # create axis
        axes = Axes(
                x_range = [-10, 10, 1], 
                y_range = [0, 5, 1], 
                x_length = 5.5, 
                y_length = 4.0, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(-10, 12, 2)}, 
                tips = False)
        axes.to_edge(DOWN, buff = 0.5)
        axes.to_edge(LEFT, buff = 1)

        other_axes = Axes(
                x_range = [-5, 5, 1], 
                y_range = [-3, 7, 1], 
                x_length = 5.5, 
                y_length = 4.0, 
                axis_config = {"color": WHITE}, 
                tips = False)
        other_axes.to_edge(DOWN, buff = 0.5)
        other_axes.to_edge(RIGHT, buff = 1)

        safety_parabola = get_safety_parabola()

        solution_parabola = always_redraw(get_solution_parabola)
        dot = always_redraw(get_point)

        equation_text = MathTex(r"tan^2(\theta)-\frac{2 v_0^2}{g x} tan(\theta)+(1 + \frac{2 v_0^2 y}{g x^2})", font_size = 35)
        equation_text.next_to(other_axes, UP)

        #solution_group = VGroup(equation_text, solution_parabola)

        self.add(axes, other_axes, solution_parabola, dot, safety_parabola)
        self.play(tracker_x.animate.set_value(5), run_time = 5)
        self.play(tracker_y.animate.set_value(5), run_time = 5)
        self.play(Write(equation_text))
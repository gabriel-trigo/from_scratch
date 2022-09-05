# imports
import numpy as np
from manim import *

# scene 1
class Scene1(Scene):
    def construct(self):

        # static constants
        v0 = 10
        g = 10

        # individual stream trajectories
        def get_trajectory(theta, tracker):
            graph = axes.plot(
                lambda x: np.tan(theta)*x-g*x**2/(2*(v0*np.cos(theta))**2), 
                x_range=[-tracker.get_value(), 0] if theta>np.pi/2 else [0, tracker.get_value()], 
                color=BLUE)
            return graph

        # safety parabola curve
        def get_safety_parabola():
            graph = axes.plot(lambda x: v0**2/(2*g)-g*x**2/(2*v0**2), 
                x_range=[-12, parabola_tracker.get_value()], 
                color=PINK)
            return graph

        # area inside the safety parabola
        def get_inside():
            graph = axes.plot(
                lambda x: v0**2/(2*g)-g*x**2/(2*v0**2), 
                x_range=[-10, 10], 
                color=PINK)
            inside = axes.get_area(
                graph, 
                x_range=(-10, inside_tracker.get_value()))
            return inside

        # area outside the safety parabola
        def get_outside():
            total = axes.plot(
                lambda x: 6, 
                x_range=[-12, outside_tracker.get_value()])
            graph = axes.plot(
                lambda x: v0**2/(2*g)-g*x**2/(2*v0**2) if (x>-10 and x<10) else 0,
                x_range=[-12, 12], 
                color = PINK)
            outside = axes.get_area(
                total, 
                bounded_graph=graph, 
                x_range=(-12, outside_tracker.get_value()), 
                color=RED, 
                opacity=0.3).set_sheen(0.2)

            return outside

        # get all the trajectory graphs to animate together
        def draw_collection():
            graphs = []
            for i, angle in enumerate(angles):
                if angle < np.pi / 2:
                    graphs.append(get_trajectory(angles[i], trackers[i]))
                else:
                    graphs.append(get_trajectory(angle, trackers[i]))
            return VGroup(*graphs)

        # create axes
        axes = Axes(
                x_range=[-12, 12, 1], 
                y_range=[0, 6, 1], 
                x_length=12, 
                y_length=5.7, 
                axis_config={"color": WHITE}, 
                x_axis_config={"numbers_with_elongated_ticks": np.arange(-10, 12, 2)}, 
                tips=False).to_edge(DOWN)
        dot = Dot(axes.coords_to_point(0, 0), color = WHITE)

        # create all trackers for individual trajectories and their animations
        trackers = []
        animations = []
        angles = np.arange(0, np.pi + np.pi/13, np.pi/13)
        for i in range(len(angles)):
            new_tracker = ValueTracker(0)
            trackers.append(new_tracker)
            animations.append(new_tracker.animate.set_value(12))

        # create text objects
        question_text1 = Text(
            "Imagine you are a bee flying near a sprinkler.", 
            font_size=35)
        question_text2 = Text(
            "How would you path in order to accomplish that?", 
            font_size=35).to_edge(UP)
        parabola_text = Text(
            "Safety Parabola", 
            font_size=60).to_edge(UP)
        parabola_text = Text(
            "Safety Parabola", 
            font_size=60).to_edge(UP)

        # create trackers for safety parabola and inside/outside areas
        parabola_tracker = ValueTracker(-12)
        inside_tracker = ValueTracker(-10)
        outside_tracker = ValueTracker(-12)

        # always redraw elements
        collection = always_redraw(draw_collection)
        parabola = always_redraw(get_safety_parabola)
        inside = always_redraw(get_inside)
        outside = always_redraw(get_outside)

        # animation
        self.play(Write(question_text1), run_time=2.5)
        self.play(question_text1.animate.to_edge(UP), run_time=1)
        self.wait(1.0)
        self.play(FadeIn(axes, run_time=0.5), FadeIn(dot, run_time=0.5))
        self.add(collection, parabola)
        self.add(dot)
        self.wait(1)
        self.play(LaggedStart(*animations, lag_ratio=0.4))
        self.play(FadeOut(question_text1))
        self.wait(1.5)
        self.play(Write(question_text2), run_time=3)
        self.play(parabola_tracker.animate.set_value(12), run_time=8)
        self.wait(2.5)
        self.play(FadeOut(question_text2))
        self.play(Write(parabola_text))
        self.wait(1)
        self.add(inside, axes, collection, parabola, dot)
        self.play(inside_tracker.animate.set_value(10), run_time=1.5)
        self.wait(2)
        self.add(outside, axes, collection, parabola, dot)
        self.play(outside_tracker.animate.set_value(12), run_time=1.5)
        self.wait(8)
        self.play(FadeOut(axes, parabola, outside, dot, inside, parabola_text, collection))
# imports
from manim import *

# scene 3
class Scene3(Scene):
    def construct(self):

        # static constants
        v0 = 10.0
        g = 10
        theta = np.pi / 4 + 0.2

        # trajectory equation
        trajectory_func = lambda x: np.tan(theta)*x-g*x**2/(2*(v0*np.cos(theta))**2)

        # draw the trajectory curve
        def get_trajectory(tracker):
            graph = complete_axes.plot(
                trajectory_func, 
                x_range=[-tracker.get_value(), 0] if theta>np.pi/2 else [0, tracker.get_value()], 
                color=BLUE)
            return graph

        # draw the dot at the tip of the trajectory
        def get_trajectory_dot(tracker):
            dot = Dot(
                complete_axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                color=PINK)
            return dot

        # draw the x projection dot
        def get_x_dot(tracker):
            dot = Dot(
                complete_axes.coords_to_point(tracker.get_value(), 0), 
                color=PINK)
            return dot

        # draw the y projection dot
        def get_y_dot(tracker):
            dot = Dot(
                complete_axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color=PINK)
            return dot
        
        # draw the x projection line
        def get_x_line(tracker):
            line = Line(
                complete_axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                complete_axes.coords_to_point(tracker.get_value(), 0), 
                color=PINK)
            return line

        # draw the y projection line
        def get_y_line(tracker):
            line = Line(
                complete_axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                complete_axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color=PINK)
            return line
        
        # draw the x dashed line
        def get_new_x_line(tracker):
            return DashedLine(
                complete_axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                x_ax.coords_to_point(tracker.get_value(), 0),
                color=PINK)

        # draw the y dashed line
        def get_new_y_line(tracker):
            return DashedLine(
                complete_axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
                y_ax.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color=PINK)

        # draw the stream as a whole
        def draw_curve_and_dot():
            return VGroup(
                get_x_line(tracker), 
                get_y_line(tracker), 
                get_trajectory(tracker), 
                get_trajectory_dot(tracker), 
                get_x_dot(tracker), 
                get_y_dot(tracker))

        # draw the new x dot
        def get_new_x_dot():
            x_dot = Dot(
                x_ax.coords_to_point(tracker.get_value(), 0), 
                color=PINK)
            return x_dot

        # draw the new y dot
        def get_new_y_dot():
            y_dot = Dot(
                y_ax.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color=PINK)
            return y_dot

        # draw new projection lines
        def new_lines_group():
             return VGroup(
                get_new_x_line(tracker), 
                get_new_y_line(tracker))

        # create complete axes
        complete_axes = Axes(
                x_range=[0, 10, 1], 
                y_range=[0, 4, 1], 
                x_length=7.0, 
                y_length=3.0, 
                axis_config={"color": WHITE}, 
                x_axis_config={
                    "numbers_with_elongated_ticks": np.arange(0, 12, 2)}, 
                y_axis_config={
                    "numbers_with_elongated_ticks": np.arange(0, 6, 2)}, 
                tips=False).to_edge(DOWN).to_edge(RIGHT)

        # create x axes
        x_ax = Axes(
                x_range=[0, 10, 1], 
                y_range=[-1, 1, 1], 
                x_length=7.0, 
                y_length=0, 
                axis_config={"color": WHITE}, 
                x_axis_config={
                    "numbers_with_elongated_ticks": np.arange(0, 12, 2)}, 
                tips=False).next_to(complete_axes, UP, buff=1.0)

        # create y axes
        y_ax = Axes(
                x_range=[-1, 1, 1], 
                y_range=[0, 4, 1], 
                x_length=0, 
                y_length=3.0, 
                axis_config={"color": WHITE}, 
                y_axis_config={
                    "numbers_with_elongated_ticks": np.arange(0, 6, 2)}, 
                tips=False).next_to(complete_axes, LEFT, buff=2.5)


        # create text objects
        x_text = MathTex(
            "x_{(t)}=v_0 \\cos(\\theta) t", 
            font_size=35).next_to(x_ax, UP).shift(LEFT)
        y_text = MathTex(
            "y_{(t)}=v_0 \\sin(\\theta) t - \\frac{g t^2}{2}", 
            font_size=35).next_to(y_ax, UP)
        complete_text = MathTex(
            "y_{(t)}=v_0 \\sin(\\theta)", "t", "- \\frac{g}{2}", "t^2", 
            font_size=35).next_to(complete_axes, UP, buff=1.2)
        complete_text2 = MathTex(
            "y_{(x)}=v_0 \\sin(\\theta)", "\\frac{x}{v_0 \\cos(\\theta)}", "-\\frac{g}{2}", "\\left(\\frac{x}{v_0 \\cos(\\theta)} \\right)^2", 
            font_size=35).next_to(complete_text, DOWN)

        # create surrounding rectangle
        t_box = SurroundingRectangle(
            complete_text[1], 
            buff=0.1)
        t2_box = SurroundingRectangle(
            complete_text[3], 
            buff=0.1)
        t_sub_box = SurroundingRectangle(
            complete_text2[1], 
            buff=0.1)
        t2_sub_box = SurroundingRectangle(
            complete_text2[3], 
            buff=0.1)

        # create value tracker
        tracker = ValueTracker(0)

        # always redraw elements
        trajectory = always_redraw(draw_curve_and_dot)
        new_lines = always_redraw(new_lines_group)
        new_x_dot = always_redraw(get_new_x_dot)
        new_y_dot = always_redraw(get_new_y_dot)

        # a few elements that I forgot
        arrow = Arrow(
            start=LEFT, 
            end=RIGHT, 
            color=YELLOW).next_to(x_text, RIGHT)
        origin_dot = Dot(
            complete_axes.coords_to_point(0, 0))
        x_text_inv = MathTex(
            "t_{(x)}=\\frac{x}{v_0 \\cos(\\theta)}", 
            font_size=35).next_to(arrow, RIGHT)

        # animations
        self.play(FadeIn(complete_axes, origin_dot), run_time=0.5)
        self.add(trajectory, origin_dot)
        self.play(tracker.animate.set_value(9), run_time=5)
        self.play(Write(x_text), Write(y_text), FadeIn(x_ax, y_ax))
        self.play(FadeIn(new_lines, new_x_dot, new_y_dot), run_time=1)
        self.play(tracker.animate.set_value(2.5), run_time=3)
        self.play(tracker.animate.set_value(7), run_time=3)
        self.play(FadeOut(new_lines))
        self.play(x_text.animate.shift(2*LEFT))
        self.wait(1)
        self.play(Create(arrow))
        self.play(Write(x_text_inv))
        self.wait(2)
        self.play(Write(complete_text))
        self.play(Write(complete_text2))
        self.play(Create(t_box), Create(t_sub_box))
        self.play(FadeOut(t_box), FadeOut(t_sub_box))
        self.play(Create(t2_box), Create(t2_sub_box))
        self.play(FadeOut(t2_box), FadeOut(t2_sub_box))
        self.play(FadeOut(x_ax, x_text, y_ax, y_text, complete_text, new_x_dot, new_y_dot, origin_dot, trajectory, complete_axes, x_text_inv, arrow))
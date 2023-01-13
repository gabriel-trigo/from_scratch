import numpy as np
from manim import *
import scene2

class Scene3(Scene):
    def construct(self):

        # static constants
        v0 = 10.0
        g = 10
        theta = np.pi / 4 + 0.2

        # trajectory equation
        def trajectory_func(x):
            return np.tan(theta) * x - g * x ** 2 / (2 * (v0 * np.cos(theta)) ** 2)

        # get trajectory
        def get_trajectory(tracker):
            graph = axes.plot(
                trajectory_func, 
                x_range=[-tracker.get_value(), 0] if theta > np.pi / 2 else [0, tracker.get_value()], 
                color=BLUE)
            return graph

        # get the dot at the tip of the trajectory
        def get_trajectory_dot(tracker):
            dot = Dot(
                axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                color = PINK)
            return dot

        # get the x axis dot
        def get_x_dot(tracker):
            dot = Dot(
                axes.coords_to_point(tracker.get_value(), 0), 
                color = PINK)
            return dot

        # get the y axis dot
        def get_y_dot(tracker):
            dot = Dot(
                axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color = PINK)
            return dot
        
        def get_x_line(tracker):
            return Line(axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
            axes.coords_to_point(tracker.get_value(), 0), 
            color = PINK)

        def get_y_line(tracker):
            return Line(axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
            axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
            color = PINK)

        def get_new_x_line(tracker):
            return DashedLine(
                axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                x_ax.coords_to_point(tracker.get_value(), 0),
                color = PINK)

        def get_new_y_line(tracker):
            return DashedLine(
                axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
                y_ax.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color = PINK)

        def draw_curve_and_dot():
            return VGroup(get_x_line(tracker), get_y_line(tracker), get_trajectory(tracker), get_trajectory_dot(tracker), get_x_dot(tracker), get_y_dot(tracker))

        def get_new_x_dot():
            x_dot = Dot(
                x_ax.coords_to_point(tracker.get_value(), 0), 
                color = PINK)
            return x_dot

        def get_new_y_dot():
            y_dot = Dot(
                y_ax.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color = PINK)
            return y_dot

        first_tracker = ValueTracker(0)

        # static constants
        v0 = 10.0
        g = 10
        theta = np.pi / 4 + 0.2

        def trajectory_func(x):
            return np.tan(theta) * x - g * x ** 2 / (2 * (v0 * np.cos(theta)) ** 2)

        # get trajectory
        def get_trajectory(tracker):
            graph = axes.plot(
                trajectory_func, 
                x_range = [-tracker.get_value(), 0] if theta > np.pi / 2 else [0, tracker.get_value()], 
                color = BLUE)
            return graph

        # get the dot at the tip of the trajectory
        def get_trajectory_dot(tracker):
            dot = Dot(
                axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                color = PINK)
            return dot

        # get the x axis dot
        def get_x_dot(tracker):
            dot = Dot(
                axes.coords_to_point(tracker.get_value(), 0), 
                color = PINK)
            return dot

        # get the y axis dot
        def get_y_dot(tracker):
            dot = Dot(
                axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color = PINK)
            return dot
        
        def get_x_line(tracker):
            return Line(axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
            axes.coords_to_point(tracker.get_value(), 0), 
            color = PINK)

        def get_y_line(tracker):
            return Line(axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
            axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
            color = PINK)

        def get_new_x_line(tracker):
            return DashedLine(
                axes.coords_to_point(tracker.get_value(), trajectory_func(tracker.get_value())), 
                x_ax.coords_to_point(tracker.get_value(), 0),
                color = PINK)

        def get_new_y_line(tracker):
            return DashedLine(
                axes.coords_to_point(0, trajectory_func(tracker.get_value())), 
                y_ax.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color = PINK)

        def draw_curve_and_dot():
            return VGroup(get_x_line(tracker), get_y_line(tracker), get_trajectory(tracker), get_trajectory_dot(tracker), get_x_dot(tracker), get_y_dot(tracker))

        def get_new_x_dot():
            x_dot = Dot(
                x_ax.coords_to_point(tracker.get_value(), 0), 
                color = PINK)
            return x_dot

        def get_new_y_dot():
            y_dot = Dot(
                y_ax.coords_to_point(0, trajectory_func(tracker.get_value())), 
                color = PINK)
            return y_dot

        # create axes objects
        complete_axes = Axes(
                x_range = [0, 10, 1], 
                y_range = [0, 4, 1], 
                x_length = 7.0, 
                y_length = 3.0, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 12, 2)}, 
                y_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 6, 2)}, 
                tips = False).to_edge(DOWN).to_edge(RIGHT)

        complete_text = Text("Complete movement", font_size = 25).next_to(complete_axes, UP)

        # x axis
        x_ax = Axes(
                x_range = [0, 10, 1], 
                y_range = [-1, 1, 1], 
                x_length = 7.0, 
                y_length = 0.00000, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 12, 2)}, 
                tips = False)
        x_ax.next_to(complete_text, UP, buff = 0.7)

        y_ax = Axes(
                x_range = [-1, 1, 1], 
                y_range = [0, 4, 1], 
                x_length = 0, 
                y_length = 3.0, 
                axis_config = {"color": WHITE}, 
                y_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 6, 2)}, 
                tips = False)
        y_ax.next_to(complete_axes, LEFT, buff = 2.5)


        
        x_text = MathTex("x_{(t)}=v_0 \\cos(\\theta) t", font_size = 35).next_to(x_ax, UP).shift(LEFT)
        y_text = MathTex("y_{(t)}=v_0 \\sin(\\theta) t - \\frac{g t^2}{2}", font_size = 35).next_to(y_ax, UP)
        complete_text = MathTex("y_{(t)}=v_0 \\sin(\\theta)", "t", "- \\frac{g}{2}", "t^2", font_size = 35).next_to(complete_axes, UP, buff=1.2)
        complete_text2 = MathTex("y_{(x)}=v_0 \\sin(\\theta)", "\\frac{x}{v_0 \\cos(\\theta)}", "-\\frac{g}{2}", "\\left(\\frac{x}{v_0 \\cos(\\theta)} \\right)^2", font_size=35).next_to(complete_text, DOWN)
        t_box = SurroundingRectangle(complete_text[1], buff = 0.1)
        t2_box = SurroundingRectangle(complete_text[3], buff = 0.1)

        t_sub_box = SurroundingRectangle(complete_text2[1], buff = 0.1)
        t2_sub_box = SurroundingRectangle(complete_text2[3], buff = 0.1)


        tracker = ValueTracker(0)
        trajectory = always_redraw(draw_curve_and_dot)

        origin_dot = Dot(complete_axes.coords_to_point(0, 0))

        def new_lines_group():
             return VGroup(get_new_x_line(tracker), get_new_y_line(tracker))


        self.play(FadeIn(complete_axes), FadeIn(origin_dot), run_time = 0.5)
        self.add(trajectory, origin_dot)
        self.play(tracker.animate.set_value(9), run_time = 5)
        new_lines = always_redraw(new_lines_group)
        new_x_dot = always_redraw(get_new_x_dot)
        new_y_dot = always_redraw(get_new_y_dot)
        self.play(Write(x_text), Write(y_text), FadeIn(x_ax), FadeIn(y_ax))
        self.play(FadeIn(new_lines), FadeIn(new_x_dot), FadeIn(new_y_dot), run_time = 1)
        self.play(tracker.animate.set_value(2.5), run_time = 3)
        self.play(tracker.animate.set_value(7), run_time = 3)
 
        self.play(FadeOut(new_lines))

        self.play(x_text.animate.shift(2*LEFT))
        arrow = Arrow(start=LEFT, end=RIGHT, color=YELLOW).next_to(x_text, RIGHT)
        x_text_inv = MathTex("t_{(x)}=\\frac{x}{v_0 \\cos(\\theta)}", font_size = 35).next_to(arrow, RIGHT)

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

        the_group = VGroup(complete_axes, origin_dot, trajectory)

        self.play(FadeOut(x_ax, x_text, y_ax, y_text, complete_text, new_x_dot, new_y_dot, origin_dot, trajectory, complete_axes, x_text_inv, arrow))

        new_axes = Axes(
                x_range = [-12, 12, 1], 
                y_range = [0, 6, 1], 
                x_length = 12, 
                y_length = 5.4, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(-12, 14, 2)}, 
                tips = False)

        new_axes.to_edge(DOWN)
        simplified_text = MathTex("y_{(x)}", "= \\tan(\\theta)", "x", "-\\frac{g }{2 v_0^2 \\cos^2(\\theta)}", "x^2", font_size=35)

        self.play(complete_text2.animate.next_to(new_axes, UP).to_edge(UP))
        simplified_text.next_to(complete_text2, DOWN)
        simplified_rectangle = SurroundingRectangle(simplified_text)
        self.play(Write(simplified_text))
        self.play(Create(simplified_rectangle))
        j = VGroup(simplified_text, simplified_rectangle)
        self.play(FadeOut(complete_text2))
        self.play(j.animate.to_edge(UP))

        origin_dot = Dot(new_axes.coords_to_point(0, 0), color = WHITE)

        self.play(FadeIn(new_axes, origin_dot))

        theta_tracker = ValueTracker(np.pi/4 - 0.4)

        def new_trajectory_func(x):
            return np.tan(theta_tracker.get_value()) * x - g * x ** 2 / (2 * (v0 * np.cos(theta_tracker.get_value())) ** 2)

        def the_trajectory():
            if theta_tracker.get_value()==np.pi/2:
                theplot = new_axes.plot(
                    lambda x: -1000, 
                    x_range = [0, 0], 
                    color = BLUE)
            else:
                theplot = new_axes.plot(
                    new_trajectory_func, 
                    x_range = [-12, 0] if theta_tracker.get_value() > np.pi / 2 else [0, 12], 
                    color = BLUE)
            return theplot

        def get_angle():
            line1 = Line(new_axes.coords_to_point(0, 0), new_axes.coords_to_point(1, 0))
            line2 = Line(new_axes.coords_to_point(0, 0), new_axes.coords_to_point(np.cos(theta_tracker.get_value()), np.sin(theta_tracker.get_value())))
            angle = Angle(line1, line2, radius = 0.3)
            tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line2, radius=0.7, other_angle=False
            ).point_from_proportion(0.5)
        )
            return VGroup(angle, tex)

        the_angle = always_redraw(get_angle)

        new_trajec = always_redraw(the_trajectory)
        self.add(new_trajec, origin_dot)
        self.play(Create(new_trajec))
        self.add(the_angle, origin_dot, new_trajec, origin_dot)
        self.play(FadeIn(the_angle))
        x1, y1 = 5, 2.3
        dot1 = Dot(new_axes.coords_to_point(x1, y1))
        self.play(theta_tracker.animate.set_value(3*np.pi/4 + 0.4), run_time=2.5)
        self.play(theta_tracker.animate.set_value(np.pi/4 - 0.4), run_time=2.5)

        def new_trajectory_func_angle(x, alpha):
            return np.tan(alpha) * x - g * x ** 2 / (2 * (v0 * np.cos(alpha)) ** 2)

        '''
        trajec1 = new_axes.plot(
                    lambda x: new_trajectory_func_angle(x, 0.74536), 
                    x_range = [0, 12], 
                    color = BLUE)

        self.add(trajec1)
        self.play(FadeIn(trajec1))
        '''

        def appear_trajec_1():
            if theta_tracker.get_value() < 0.74536:
                theplot = new_axes.plot(
                    lambda x: -1000, 
                    x_range = [0, 0], 
                    color = BLUE)
            else:
                theplot = new_axes.plot(
                    lambda x: new_trajectory_func_angle(x, 0.74546), 
                    x_range = [0, 12], 
                    color = GREEN)
            return theplot
        trajec1 = always_redraw(appear_trajec_1)

        def appear_trajec_2():
            if theta_tracker.get_value() < 1.256575:
                theplot = new_axes.plot(
                    lambda x: -1000, 
                    x_range = [0, 0], 
                    color = BLUE)
            else:
                theplot = new_axes.plot(
                    lambda x: new_trajectory_func_angle(x, 1.256575), 
                    x_range = [0, 12], 
                    color = GREEN)
            return theplot
        self.play(FadeIn(dot1))
        trajec1 = always_redraw(appear_trajec_1)
        trajec2 = always_redraw(appear_trajec_2)
        self.add(trajec1, trajec2, origin_dot, dot1)
        self.play(theta_tracker.animate.set_value(3*np.pi/4 + 0.4), run_time=5)
        self.play(FadeOut(trajec2, trajec1, dot1))
        self.play(theta_tracker.animate.set_value(np.pi/4 - 0.4), run_time=1.5)
        dot2 = Dot(new_axes.coords_to_point(5, 3.75))

        def appear_trajec_3():
            if theta_tracker.get_value() < 1.107:
                theplot = new_axes.plot(
                    lambda x: -1000, 
                    x_range = [0, 0], 
                    color = BLUE)
            else:
                theplot = new_axes.plot(
                    lambda x: new_trajectory_func_angle(x, 1.107), 
                    x_range = [0, 12], 
                    color = GREEN)
            return theplot
        trajec3 = always_redraw(appear_trajec_3)
        self.add(trajec3, origin_dot, dot2)
        self.play(FadeIn(dot2))
        self.play(theta_tracker.animate.set_value(3*np.pi/4 + 0.4), run_time=5)
        self.play(FadeOut(trajec3, dot2))
        self.play(theta_tracker.animate.set_value(np.pi/4 - 0.4), run_time=1.5)

        dot3 = Dot(new_axes.coords_to_point(6, 4))
        self.play(FadeIn(dot3))
        self.play(theta_tracker.animate.set_value(3*np.pi/4 + 0.4), run_time=5)
        self.play(theta_tracker.animate.set_value(np.pi/4 - 0.4), run_time=1.5)
        self.play(FadeOut(dot3))


        safety_parabola = new_axes.plot(lambda x: v0 ** 2 / (2 * g) - g * x ** 2 / (2 * v0 ** 2), x_range = [-12, 12], color = PINK)
        self.play(FadeIn(safety_parabola))
        self.play(FadeIn(dot1))
        self.add(trajec1, trajec2, origin_dot, dot1)
        self.play(theta_tracker.animate.set_value(3*np.pi/4 + 0.4), run_time=2.5)
        self.play(FadeOut(trajec2, trajec1, dot1))
        self.play(theta_tracker.animate.set_value(np.pi/4 - 0.4), run_time=1)

        self.add(trajec3, origin_dot, dot2)
        self.play(FadeIn(dot2))
        self.play(theta_tracker.animate.set_value(3*np.pi/4 + 0.4), run_time=2.5)
        self.play(FadeOut(trajec3, dot2))
        self.play(theta_tracker.animate.set_value(np.pi/4 - 0.4), run_time=1)

        self.play(FadeIn(dot3))
        self.play(theta_tracker.animate.set_value(3*np.pi/4 + 0.4), run_time=2.5)
        self.play(FadeOut(dot3, new_trajec, the_angle))
        self.play(theta_tracker.animate.set_value(np.pi/4 - 0.4), run_time=0.1)

        inside = new_axes.get_area(safety_parabola, x_range = (-10, 10), color=GREEN, opacity=0.3)
        inside.set_sheen(0.2)
        self.add(inside, safety_parabola)
        self.play(FadeIn(inside))

        new_safety_parabola = new_axes.plot(lambda x: v0 ** 2 / (2 * g) - g * x ** 2 / (2 * v0 ** 2) if (x>-10 and x<10) else 0, x_range = [-12, 12], color = PINK)

        total = new_axes.plot(lambda x: 8, x_range = [-15, 15])
        total_area = new_axes.get_area(total, x_range=(-15, 15), bounded_graph=new_safety_parabola, color=RED, opacity=0.3)
        total_area.set_sheen(1)
        self.add(total_area, j, safety_parabola, new_axes, origin_dot)
        self.play(FadeIn(total_area))

        simplified_text_0 = MathTex("y_0", "= \\tan(\\theta)", "x_0", "-\\frac{g }{2 v_0^2 \\cos^2(\\theta)}", "x_0^2", font_size=35)

        complete_plot = VGroup(inside, total_area, new_axes, safety_parabola, origin_dot)
        self.play(complete_plot.animate.scale(0.6).to_edge(LEFT).to_edge(DOWN, buff=-0.7))
        self.play(j.animate.next_to(complete_plot, UP, buff=1.0))
        self.play(FadeOut(simplified_rectangle))
        trajectory_equation = MathTex("\\text{Trajectory equation}", font_size=40).next_to(j, UP)
        self.play(Write(trajectory_equation))

        simplified_text_0.next_to(j, RIGHT, buff=1.9)
        simplified_text_0_rect = SurroundingRectangle(simplified_text_0, buff=0.1)
        simplified_eq = MathTex("\\text{Equation for $\\theta$}", font_size=40).next_to(simplified_text_0, UP)

        x_tracker = ValueTracker(5)
        y_tracker=ValueTracker(2.3)
        def get_dot():
            dot = Dot(new_axes.coords_to_point(x_tracker.get_value(), y_tracker.get_value()), radius=0.05)
            dot_text = MathTex("(x_0, y_0)", font_size=40).next_to(dot, DOWN)
            return VGroup(dot, dot_text)

        self.wait(2)
        new_dot = always_redraw(get_dot)
        self.play(FadeIn(new_dot))

        self.wait(2)
        self.play(Write(simplified_eq))
        self.play(Write(simplified_text_0))

        x_box_new1 = SurroundingRectangle(simplified_text_0[2])
        x_box_new2 = SurroundingRectangle(simplified_text_0[4])
        y_box_new = SurroundingRectangle(simplified_text_0[0])

        x_box1 = SurroundingRectangle(simplified_text[2])
        x_box2 =  SurroundingRectangle(simplified_text[4])
        y_box = SurroundingRectangle(simplified_text[0])

        self.wait(2)
        self.play(Create(x_box1), Create(x_box2), Create(x_box_new1), Create(x_box_new2))
        self.wait(2)
        self.play(FadeOut(x_box1), FadeOut(x_box2), FadeOut(x_box_new1), FadeOut(x_box_new2))
        self.wait(2)
        self.play(Create(y_box), Create(y_box_new))
        self.wait(2)
        self.play(FadeOut(y_box), FadeOut(y_box_new))

        self.play(Create(simplified_text_0_rect))

        sol_1 = MathTex("\\text{2 solutions for $\\theta$}", font_size=40).next_to(simplified_text_0, DOWN, buff=1.5)
        sol_2 = MathTex("\\text{1 solution for $\\theta $}", font_size=40).next_to(sol_1, DOWN, buff=1)
        sol_3 = MathTex("\\text{0 solutions for $\\theta$}", font_size=40).next_to(sol_2, DOWN, buff=1)\
        
        sol_1_rect = SurroundingRectangle(sol_1, buff=0.3, color=GREEN, fill_color = GREEN, fill_opacity=0.3)
        sol_1_rect.set_sheen(0.4)

        sol_2_rect = SurroundingRectangle(sol_2, buff=0.3, color=PINK, fill_color = PINK, fill_opacity=0.3)
        sol_2_rect.set_sheen(0.4)

        sol_3_rect = SurroundingRectangle(sol_3, buff=0.3, color=RED, fill_color = RED, fill_opacity=0.3)
        sol_3_rect.set_sheen(0.4)


        self.wait(2)
        self.play(Write(sol_1))
        self.add(sol_1_rect, sol_1)
        self.play(FadeIn(sol_1_rect))


        self.wait(2)
        self.play(x_tracker.animate.set_value(5), y_tracker.animate.set_value(3.75))
        self.play(Write(sol_2))
        self.add(sol_2_rect, sol_2)
        self.play(FadeIn(sol_2_rect))


        self.wait(2)
        self.play(x_tracker.animate.set_value(6), y_tracker.animate.set_value(6))
        self.play(Write(sol_3))
        self.add(sol_3_rect, sol_3)
        self.play(FadeIn(sol_3_rect))

        z1 = VGroup(sol_1, sol_1_rect)
        z2 = VGroup(sol_2, sol_2_rect)
        z3 = VGroup(sol_3, sol_3_rect)

        self.wait(14)
        self.play(FadeOut(simplified_text), FadeOut(trajectory_equation), FadeOut(simplified_text_0_rect))
        self.play(FadeOut(z1), FadeOut(z2), FadeOut(z3))


        self.wait(12)
        text_1 = MathTex("y_0", "= \\tan(\\theta)", "x_0", "-\\frac{g }{2 v_0^2 }(1 + \\tan^2(\\theta))", "x_0^2", font_size=35)
        text_1.next_to(simplified_text_0, DOWN)
        self.play(Write(text_1))

        self.wait(3)
        cos_box = SurroundingRectangle(simplified_text_0[3], buff=0)
        tan_box = SurroundingRectangle(text_1[3], buff=0)
        self.play(Create(cos_box), Create(tan_box))
        self.wait(3)
        self.play(FadeOut(cos_box), FadeOut(tan_box))


        self.wait(4)
        text_2 = MathTex("\\frac{g x_0^2}{2 v_0^2}", "\\tan^2(\\theta)", "-", "x_0", "\\tan(\\theta)", "+", "\\left(y_0 + \\frac{g x_0^2}{2 v_0^2}\\right)", "=0", font_size=30)
        text_2.next_to(text_1, DOWN)
        self.play(Write(text_2))

        a_box = SurroundingRectangle(text_2[0], color=BLUE, buff=0.1)
        b_box = SurroundingRectangle(text_2[3], color=PINK, buff=0.1)
        c_box = SurroundingRectangle(text_2[-2], color=GREEN, buff=0.1)

        a_label = MathTex("a", color=BLUE).next_to(a_box, DOWN)
        b_label = MathTex("b", color=PINK).next_to(b_box, DOWN)
        c_label = MathTex("c", color=GREEN).next_to(c_box, DOWN)

        self.wait(1)
        self.play(Create(a_box), FadeIn(a_label))

        self.wait(1)
        self.play(Create(b_box), FadeIn(b_label))

        self.wait(1)
        self.play(Create(c_box), FadeIn(c_label))

        a_group = VGroup(text_2[0], a_label, a_box)
        b_group = VGroup(text_2[3], b_label, b_box)
        c_group = VGroup(text_2[6], c_label, c_box)

        text_3 = MathTex("a", "\\tan^2(\\theta)+", "b", " \\tan(\\theta) + ", "c",  "= 0", font_size=35)
        text_3[0].set_color(BLUE)
        text_3[2].set_color(PINK)
        text_3[4].set_color(GREEN)
        text_3.next_to(text_2, DOWN, buff=1.5)

        self.wait(1)
        self.play(Write(text_3))
        quadratic_box = SurroundingRectangle(text_3)
        self.play(Create(quadratic_box))

        quadratic = VGroup(quadratic_box, text_3)
        quadratic_text = MathTex("\\text{Quadratic equation for $\\tan(\\theta)$}", font_size=40)
        quadratic_text.next_to(new_axes, UP).to_edge(UP)

        self.play(FadeOut(simplified_eq), FadeOut(simplified_text_0), FadeOut(text_1), FadeOut(text_2[1]), FadeOut(text_2[2]), FadeOut(text_2[4]), FadeOut(text_2[5]), 
            quadratic.animate.next_to(quadratic_text, DOWN), FadeOut(text_2[7]), Write(quadratic_text))

        self.play(a_label.animate.next_to(a_box, RIGHT), b_label.animate.next_to(b_box, RIGHT), c_label.animate.next_to(c_box, RIGHT))
        ctes = VGroup(a_group, b_group, c_group)
        self.play(ctes.animate.next_to(quadratic, DOWN))

        sol_axes = Axes(
                x_range = [-10, 10, 2], 
                y_range = [-6, 6, 2], 
                x_length = 5.5, 
                y_length = 4.0, 
                axis_config = {"color": WHITE}, 
                tips = False)
        sol_axes.to_edge(DOWN)
        sol_axes.to_edge(RIGHT)

        sol_text = MathTex("\\text{Solutions}", font_size=40)
        sol_text.next_to(sol_axes, UP).to_edge(UP)
        self.play(Write(sol_text))

        sol_eq = MathTex("s_1, s_2 = \\frac{-b \\pm \\sqrt{b^2 - 4 a c}}{2 a}", font_size = 35)
        sol_eq.next_to(sol_text, DOWN)



        v = ValueTracker(11)
        def get_update():
            dot = Dot(new_axes.coords_to_point(x_tracker.get_value(), v.get_value() ** 2 / (2 * g) - g * x_tracker.get_value() ** 2 / (2 * v.get_value() ** 2)), radius=0.05)
            dot_text = MathTex("(x_0, y_0)", font_size=40).next_to(dot, DOWN)
            return VGroup(dot, dot_text)
        dot_b = always_redraw(get_update)


        def get_solution_parabola():
            a = 1
            b = -2 * v0 ** 2 / (g * x_tracker.get_value())
            c = 1 + 2 * v0 ** 2 * (v.get_value() ** 2 / (2 * g) - g * x_tracker.get_value() ** 2 / (2 * v.get_value() ** 2)) / (g * x_tracker.get_value() ** 2)
            graph = sol_axes.plot(lambda t: t ** 2 - 2 * v0 ** 2 / (g * x_tracker.get_value()) * t + (1 + 2 * v0 ** 2 * (v.get_value() ** 2 / (2 * g) - g * x_tracker.get_value() ** 2 / (2 * v.get_value() ** 2)) / (g * x_tracker.get_value() ** 2)), 
            x_range = [(-b-(b**2 - 4*a*(c-6))**0.5)/(2*a), (-b+(b**2 - 4*a*(c-6))**0.5)/(2*a)], color=BLUE)
            return graph


        self.play(Write(sol_eq))
        sol_parabola = always_redraw(get_solution_parabola)


        #self.play(x_tracker.animate.set_value(1), run_time=3)
        print("poggers")
        self.play(x_tracker.animate.set_value(6), y_tracker.animate.set_value(v.get_value() ** 2 / (2 * g) - g * 6 ** 2 / (2 * v.get_value() ** 2)))
        self.add(dot_b)
        self.play(FadeOut(new_dot))

        self.play(FadeIn(sol_axes))
        self.play(FadeIn(sol_parabola))

        trigger = False

        def get_sols():
            a = 1
            b = -2 * v0 ** 2 / (g * x_tracker.get_value())
            c = 1 + 2 * v0 ** 2 * (v.get_value() ** 2 / (2 * g) - g * x_tracker.get_value() ** 2 / (2 * v.get_value() ** 2)) / (g * x_tracker.get_value() ** 2)

            if trigger:
                sol_1 = (-b)/(2*a)
                dot_1 = Dot(sol_axes.coords_to_point(sol_1, 0), color=PINK)
                label_1 = MathTex("s_1 = s_2", font_size=30).next_to(dot_1, DOWN)
                return VGroup(dot_1, label_1)
            else:
                sol_1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
                sol_2 = (-b - (b**2 -4*a*c)**0.5)/(2*a)
                dot_1 = Dot(sol_axes.coords_to_point(sol_1, 0), color=PINK)
                dot_2 = Dot(sol_axes.coords_to_point(sol_2, 0), color=PINK)
                label_1 = MathTex("s_1", font_size=30).next_to(dot_1, DOWN)
                label_2 = MathTex("s_2", font_size=30).next_to(dot_2, DOWN)
                return VGroup(dot_1, label_1, dot_2, label_2)

        self.play(x_tracker.animate.set_value(10), run_time=2.5)
        self.play(x_tracker.animate.set_value(2), run_time=2.5)
        
        self.play(v.animate.set_value(10.2), run_time=5)
        self.play(x_tracker.animate.set_value(10), run_time=2.5)
        self.play(x_tracker.animate.set_value(6), run_time=2.5)

        self.play(v.animate.set_value(9.4))
        sols = always_redraw(get_sols)
        self.play(FadeIn(sols))
        self.play(x_tracker.animate.set_value(2), run_time=2.5)
        self.play(x_tracker.animate.set_value(8), run_time=2.5)
        #self.play(x_tracker.animate.set_value(6), run_time=5)

        self.play(v.animate.set_value(10))
        trigger = True

        self.play(x_tracker.animate.set_value(2), run_time=2.5)
        self.play(x_tracker.animate.set_value(9), run_time=2.5)

        self.play(FadeOut(sol_axes, sol_parabola, sols))

        self.wait(6)

        discriminant= MathTex("b^2 - 4 a c = 0", font_size=35).next_to(sol_eq, DOWN, buff = 0.5)
        discriminant_sub = MathTex("x_0^2", "-", "4", "\\left(\\frac{g x_0^2}{2 v_0^2} \\right)", "\\left(y_0 + \\frac{g x_0^2}{2 v_0^2}\\right)", "=0", font_size=35).next_to(discriminant, DOWN, buff=0.5)

        discriminant_sub[0].set_color(PINK)
        discriminant_sub[3].set_color(BLUE)
        discriminant_sub[4].set_color(GREEN)
        self.wait(2)
        self.play(Write(discriminant))
        self.wait(2)
        self.play(Write(discriminant_sub))

        discriminant_sol = MathTex("y_{(x)} = \\frac{v_0^2}{2 g} - \\frac{g x_0^2}{2 v_0^2}").next_to(discriminant_sub, DOWN, buff=0.5)
        sol_box = SurroundingRectangle(discriminant_sol)
        self.wait(1.0)
        self.play(Write(discriminant_sol))
        self.wait(1.0)
        self.play(Create(sol_box))
        self.wait(1)

        center = Text("a")

        self.play(FadeOut(discriminant, discriminant_sub, complete_plot, a_group, b_group, c_group, quadratic, quadratic_text, dot_b, sol_eq, sol_text))
        self.play(VGroup(discriminant_sol, sol_box).animate.move_to(center))
        self.play(FadeOut(VGroup(discriminant_sol, sol_box)))
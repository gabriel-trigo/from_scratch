import numpy as np
from manim import *

class Scene2(Scene):
    def construct(self):

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

        first_tracker = ValueTracker(0)

        def draw_first_dot():
            graph = first_axis.plot(trajectory_func, x_range = [0, first_tracker.get_value()], color = BLUE)
            dot = Dot(first_axis.coords_to_point(first_tracker.get_value(), trajectory_func(first_tracker.get_value())), color=PINK)
            return VGroup(graph, dot)

        first_axis = axes = Axes(
                x_range = [-4, 4, 1], 
                y_range = [0, 4, 1], 
                x_length = 7.0, 
                y_length = 5., 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(-4, 6, 2)}, 
                tips = False)

        first_origin_dot = Dot(first_axis.coords_to_point(0, 0))
        first = always_redraw(draw_first_dot)
        self.wait(2)
        self.add(first_axis, first, first_origin_dot)
        self.play(FadeIn(first_axis, first_origin_dot))
        self.wait(2)
        self.play(first_tracker.animate.set_value(2.7))

        line1 = Line(first_axis.coords_to_point(0, 0), first_axis.coords_to_point(1, 0))
        line2 = Line(first_axis.coords_to_point(0, 0), first_axis.coords_to_point(np.cos(theta), np.sin(theta)))
        the_angle = Angle(line1, line2, radius = 0.3)
        tex = MathTex("\\theta").move_to(
            Angle(
                line1, line2, radius=1.0, other_angle=False
            ).point_from_proportion(0.7)
        )
        self.wait(1)
        self.add(the_angle, tex, first_axis, first, first_origin_dot)
        self.play(FadeIn(the_angle), FadeIn(tex))
        self.wait(2)


        total_speed_arrow = Arrow(start=first_axis.coords_to_point(0, 0), end=first_axis.coords_to_point(2*np.cos(theta), 2*np.sin(theta)), color = YELLOW, buff=0)
        total_arrow_label = MathTex("v_0").next_to(total_speed_arrow, UP)
        self.add(total_speed_arrow, total_arrow_label, first_origin_dot)
        self.play(FadeIn(total_speed_arrow), FadeIn(total_arrow_label))

        self.wait(4)

        force_arrow = Arrow(start=first_axis.coords_to_point(first_tracker.get_value(), trajectory_func(first_tracker.get_value())), end=first_axis.coords_to_point(first_tracker.get_value(), trajectory_func(first_tracker.get_value())-1), buff=0, color=GREEN)
        force_label = MathTex("m g").next_to(force_arrow, DOWN)
        self.add(force_arrow, first, first_axis, first, first_origin_dot)
        self.play(FadeIn(force_arrow), FadeIn(force_label))

        self.wait(3)

        self.play(FadeOut(first_axis), FadeOut(first), FadeOut(first_origin_dot), FadeOut(the_angle), FadeOut(tex), FadeOut(total_speed_arrow), FadeOut(force_arrow), FadeOut(force_label), FadeOut(total_arrow_label))

        self.wait(2)


        fma = MathTex("\\vec{F}", "=", "m", "\\vec{a}")
        eq_force_arrow = Arrow(start=UP, end=DOWN, stroke_width=3, color=BLUE).next_to(fma[0], DOWN)
        eq_mass_arrow = Arrow(start=DOWN, end=UP, stroke_width=3, color=PINK).next_to(fma[2], UP)
        eq_accel_arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=3, color=YELLOW).next_to(fma[3], RIGHT)

        eq_force_label = MathTex("\\text{Force vector}", color=BLUE).next_to(eq_force_arrow, DOWN)
        eq_mass_label = MathTex("\\text{Mass}", color=PINK).next_to(eq_mass_arrow, UP)
        eq_accel_label = MathTex("\\text{Acceleration vector}", color=YELLOW).next_to(eq_accel_arrow, RIGHT)

        self.play(Write(fma))
        self.wait(1.5)
        self.play(FadeIn(eq_force_arrow), Write(eq_force_label))
        self.wait(1.5)
        self.play(FadeIn(eq_mass_arrow), Write(eq_mass_label))
        self.wait(1.5)
        self.play(FadeIn(eq_accel_arrow), Write(eq_accel_label))

        self.wait(3)

        self.play(FadeOut(eq_force_arrow), FadeOut(eq_mass_arrow), FadeOut(eq_accel_arrow), FadeOut(eq_force_label), FadeOut(eq_mass_label), FadeOut(eq_accel_label), FadeOut(fma))

        # create axis
        axes = Axes(
                x_range = [0, 10, 1], 
                y_range = [0, 4, 1], 
                x_length = 7.0, 
                y_length = 3.0, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 12, 2)}, 
                y_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 6, 2)}, 
                tips = False)
        axes.to_edge(DOWN)
        axes.to_edge(RIGHT)

        complete_text = Text("Complete movement", font_size = 25).next_to(axes, UP)

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
        x_ax.next_to(complete_text, UP, buff = 0.5)

        y_ax = Axes(
                x_range = [-1, 1, 1], 
                y_range = [0, 4, 1], 
                x_length = 0, 
                y_length = 3.0, 
                axis_config = {"color": WHITE}, 
                y_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 6, 2)}, 
                tips = False)
        y_ax.next_to(axes, LEFT, buff = 2.5)

        complete_text = Text("Complete movement", font_size = 25).next_to(axes, UP)
        x_text = Text("Horizontal movement", font_size = 25).next_to(x_ax, UP)
        y_text = Text("Vertical movement", font_size = 25).next_to(y_ax, UP)
        # top_flash = Line(axes.coords_to_point(0, 4), axes.coords_to_point(10, 4), color = YELLOW)
        #rectangle = Rectangle(width = 5, height = 4, fill_opacity = 0.5, stroke_color = None, stroke_opacity = 0).move_to(axes.coords_to_point(0, 4))

        tracker = ValueTracker(0)
        trajectory = always_redraw(draw_curve_and_dot)

        origin_dot = Dot(axes.coords_to_point(0, 0))

        def new_lines_group():
             return VGroup(get_new_x_line(tracker), get_new_y_line(tracker))
        vertical_group = VGroup(y_ax, y_text)
        horizontal_group = VGroup(x_ax, x_text)
        complete_group = VGroup(axes, complete_text, trajectory)
        framebox1 = SurroundingRectangle(vertical_group, buff = 0.2)
        framebox2 = SurroundingRectangle(horizontal_group, buff = 0.2)
        framebox3 = SurroundingRectangle(complete_group, buff = 0.2)
        
        self.play(FadeIn(axes), FadeIn(origin_dot), run_time = 0.5)
        self.play(Write(complete_text))
        self.add(trajectory, origin_dot)
        self.play(tracker.animate.set_value(9), run_time = 5)
        new_lines = always_redraw(new_lines_group)
        new_x_dot = always_redraw(get_new_x_dot)
        new_y_dot = always_redraw(get_new_y_dot)
        self.play(Write(x_text), Write(y_text), FadeIn(x_ax), FadeIn(y_ax))
        self.play(FadeIn(new_lines), FadeIn(new_x_dot), FadeIn(new_y_dot), run_time = 1)
        self.play(tracker.animate.set_value(2.5), run_time = 3)
        self.play(tracker.animate.set_value(7), run_time = 3)
        #self.play(Create(framebox3))
        self.play(Create(framebox1))
        self.play(Create(framebox2))
        self.play(FadeOut(new_lines))
        self.play(FadeOut(complete_group), FadeOut(origin_dot))

        vertical_group = VGroup(vertical_group, framebox1, new_y_dot)
        horizontal_group = VGroup(horizontal_group, framebox2, new_x_dot)
        complete_group = VGroup(complete_group, framebox3)

        self.play(horizontal_group.animate.to_edge(LEFT).to_edge(UP), run_time = 1)
        self.play(vertical_group.animate.to_edge(DOWN).next_to(horizontal_group, DOWN), run_time = 1)
        self.play(tracker.animate.set_value(0))



















        # SCENE 33333333333333333333333333333333333
        self.play(FadeOut(vertical_group))

        self.wait(4)

        equation_x_1 = MathTex("F_x", "=m", "a_x", font_size = 40).next_to(horizontal_group, RIGHT, buff = 2).to_edge(UP)
        self.play(Write(equation_x_1))
        self.wait(8)
        framebox_Fx = SurroundingRectangle(equation_x_1[0])
        framebox_Ax = SurroundingRectangle(equation_x_1[2])

        equation_x_2 = MathTex("0", "=m", "\\frac{d v_x}{dt}", font_size = 40).next_to(equation_x_1, DOWN, buff = 0.4)
        framebox_Fx_2 = SurroundingRectangle(equation_x_2[0])
        framebox_Ax_2 = SurroundingRectangle(equation_x_2[2])

        self.play(Write(equation_x_2))
        self.play(Create(framebox_Fx), Create(framebox_Fx_2))
        self.wait(1.5)
        self.play(FadeOut(framebox_Fx), FadeOut(framebox_Fx_2))
        self.wait(1.5)
        self.play(Create(framebox_Ax), Create(framebox_Ax_2))
        self.wait(1)
        self.play(FadeOut(framebox_Ax), FadeOut(framebox_Ax_2))

        equation_x_3 = MathTex("\\frac{d v_x}{dt}=0", font_size = 40).next_to(equation_x_2, DOWN, buff = 0.4)
        equation_x_4 = MathTex("\\int\\limits^{v_{x(t)}}_{v_0 \\cos(\\theta)}", "d v_x =","\int\limits^t_0", "0 dt", font_size = 40).next_to(equation_x_3, DOWN, buff = 0.4)
        equation_x_5 = MathTex("v_{x(t)}-v_0 \\cos(\\theta)=0", font_size = 40).next_to(equation_x_4, DOWN, buff = 0.4)
        equation_x_6 = MathTex("v_{x(t)}", "=v_0 \\cos(\\theta)", font_size = 40).next_to(equation_x_5, DOWN, buff = 0.4)

        self.wait(1)
        self.play(Write(equation_x_3))
        self.wait(7)
        self.play(Write(equation_x_4[1:4:2]))
        self.wait(7)
        self.play(Write(equation_x_4[0]))
        self.wait(8)
        self.play(Write(equation_x_4[2]))
        self.wait(6)
        self.play(Write(equation_x_5))
        self.wait(6)
        self.play(Write(equation_x_6))

        framebox_v = SurroundingRectangle(equation_x_6)

        self.play(Create(framebox_v))
        self.wait(17)

        vx_eq = VGroup(equation_x_6, framebox_v)


        speed_axes = Axes(
                x_range = [0, 10, 1], 
                y_range = [0, 8, 1], 
                x_length = 7.0, 
                y_length = 3.0, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 12, 2)}, 
                y_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 10, 2)}, 
                tips = False)
        speed_axes.to_edge(DOWN).to_edge(LEFT)

        labels = speed_axes.get_axis_labels(x_label=MathTex("t"), y_label=MathTex("v_x"))

        self.wait(12)
        self.play(FadeIn(speed_axes), FadeIn(labels))

        def get_speed():
            graph = speed_axes.plot(lambda x: v0 * np.cos(theta), 
            x_range = [0, tracker.get_value()], 
            color = BLUE)
            return graph

        def get_speed_dot():
            return Dot(speed_axes.coords_to_point(tracker.get_value(), v0 * np.cos(theta)), 
            color = PINK)

        speed_plot = always_redraw(get_speed)
        speed_dot = always_redraw(get_speed_dot)

        self.play(FadeIn(speed_plot), FadeIn(speed_dot))
        self.add(speed_axes, speed_dot)
        self.play(tracker.animate.set_value(8), rate_func = rate_functions.linear, run_time = 8)

        self.play(FadeOut(equation_x_1), FadeOut(equation_x_2), FadeOut(equation_x_3), FadeOut(equation_x_4), FadeOut(equation_x_5))
        self.play(vx_eq.animate.to_edge(UP), tracker.animate.set_value(0), FadeOut(framebox_v))
        self.wait(3)

        equation_x_7 = MathTex("\\frac{d x}{dt}", "=v_0 \\cos(\\theta)", font_size = 40).next_to(equation_x_6, DOWN, buff = 0.4)
        self.play(Write(equation_x_7))
        v_box = SurroundingRectangle(equation_x_6[0])
        dv_box = SurroundingRectangle(equation_x_7[0])

        self.wait(3)
        self.play(Create(v_box), Create(dv_box))
        self.wait(3)
        self.play(FadeOut(v_box), FadeOut(dv_box))
        self.wait(3)

        equation_x_8 = MathTex("\\int\\limits^{x_{(t)}}_0", "dx=", "\\int\\limits^t_0", "v_0 \\cos(\\theta) dt", font_size = 40).next_to(equation_x_7, DOWN, buff = 0.4)
        self.play(Write(equation_x_8[1:4:2]))
        self.wait(3)
        self.play(Write(equation_x_8[0]))
        self.wait(4)
        self.play(Write(equation_x_8[2]))
        self.wait(4)

        equation_x_9 = MathTex("x_{(t)}=v_0 \\cos(\\theta) t", font_size = 40).next_to(equation_x_8, DOWN, buff = 0.4)
        self.play(Write(equation_x_9))
        self.wait(3)

        framebox_x = SurroundingRectangle(equation_x_9)

        
        x_group = VGroup(equation_x_9, framebox_x)

        self.play(FadeOut(equation_x_7), FadeOut(equation_x_8))
        self.play(equation_x_9.animate.next_to(equation_x_6, DOWN, buff = 0.4))


        position_axes = Axes(
                x_range = [0, 10, 1], 
                y_range = [0, 45, 5.625], 
                x_length = 5.0, 
                y_length = 3.0, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 12, 2)}, 
                y_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 45 + 5.625, 2 * 5.625)}, 
                tips = False)
        position_axes.to_edge(DOWN).to_edge(RIGHT)

        x_position_labels = position_axes.get_axis_labels(x_label=MathTex("t"), y_label=MathTex("x"))

        def get_x_plot():
            graph = position_axes.plot(
                lambda x: v0 * np.cos(theta) * x, 
                x_range = [0, tracker.get_value()], 
                color = BLUE
            )
            return graph

        def get_x_dot():
            return Dot(position_axes.coords_to_point(tracker.get_value(), v0 * np.cos(theta) * tracker.get_value()), 
            color = PINK)

        def get_the_area():
            area = speed_axes.get_area(get_speed(), x_range = (0, tracker.get_value()), opacity = 0.5)
            return area

        x_plot = always_redraw(get_x_plot)
        x_dot = always_redraw(get_x_dot)
        area = always_redraw(get_the_area)

        self.add(area, speed_axes, speed_plot, speed_dot)
        self.remove(speed_plot)
        self.play(FadeIn(position_axes, x_position_labels))
        self.play(FadeIn(x_plot), FadeIn(x_dot))
        self.add(position_axes, x_dot, x_position_labels)
        self.play(tracker.animate.set_value(8), run_time = 5)
        label = MathTex("v_0 \\cos(\\theta) t", font_size = 40).move_to(area)

        speeed = Line(speed_axes.coords_to_point(0, v0 * np.cos(theta)), speed_axes.coords_to_point(tracker.get_value(), v0 * np.cos(theta)))
        brace_line = Line(speed_axes.coords_to_point(tracker.get_value(), v0 * np.cos(theta)), speed_axes.coords_to_point(tracker.get_value(), 0))
        brace1 = Brace(speeed, direction = np.array([0, 1, 0]), sharpness = 0.7)
        brace2 = Brace(brace_line, direction = np.array([1, 0, 0]), sharpness = 0.7)
        brace_text_t = MathTex("t", font_size = 30).next_to(brace1, UP)
        brace_text_2 = MathTex("v_0 \\cos(\\theta)", font_size = 30).next_to(brace2, RIGHT)
        self.play(FadeIn(brace1), Write(brace_text_t))
        self.wait(3)
        self.play(FadeIn(brace2), Write(brace_text_2))
        self.wait(5)
        #self.play(FadeOut(brace1), FadeOut(brace_text_t))
        self.play(Write(label))
        self.wait(3)
        framebox_x = SurroundingRectangle(equation_x_9)
        self.play(Create(framebox_x))
        self.wait(5)

        self.play(FadeOut(horizontal_group, x_position_labels), FadeOut(x_plot), FadeOut(x_dot), FadeOut(area), FadeOut(speed_axes), FadeOut(position_axes), FadeOut(brace1), 
            FadeOut(brace2), FadeOut(brace_text_t), FadeOut(brace_text_2), FadeOut(equation_x_9), FadeOut(equation_x_6), FadeOut(labels), FadeOut(speed_dot), FadeOut(label), FadeOut(framebox_x))
        tracker.set_value(0)

        self.wait(2)



        self.play(FadeIn(vertical_group))
        self.play(vertical_group.animate.to_edge(LEFT).to_edge(UP))
        
        self.wait(2.5)
        equation_y_1 = MathTex("F_y", "=m", "a_y", font_size = 40).next_to(vertical_group, RIGHT, buff = 1.5).to_edge(UP)
        self.play(Write(equation_y_1))

        self.wait(2.5)
        equation_y_2 = MathTex("-mg", "=m", "\\frac{d v_y}{dt}", font_size = 40).next_to(equation_y_1, DOWN, buff = 0.4)
        self.play(Write(equation_y_2))

        Fy_box = SurroundingRectangle(equation_y_1[0])
        Fy_box2 = SurroundingRectangle(equation_y_2[0])

        self.wait(2)
        self.play(Create(Fy_box), Create(Fy_box2))

        self.wait(1)
        self.play(FadeOut(Fy_box), FadeOut(Fy_box2))

        self.wait(1)
        equation_y_3 = MathTex("\\frac{d v_y}{dt} = -g", font_size = 40).next_to(equation_y_2, DOWN, buff = 0.4)
        self.play(Write(equation_y_3))

        self.wait(0.5)
        equation_y_4 = MathTex("\\int\\limits^{v_{y(t)}}_{v_0 \\sin(\\theta)}", "d v_y", "=", "\\int\\limits^t_0", "-g dt", font_size = 40).next_to(equation_y_3, DOWN, buff = 0.4)
        self.play(Write(equation_y_4))

        self.wait(0.5)
        equation_y_5 = MathTex("v_{y(t)} - v_0 \\sin(\\theta) = -g t", font_size = 40).next_to(equation_y_4, DOWN, buff = 0.4)
        self.play(Write(equation_y_5))

        self.wait(0.5)
        equation_y_6 = MathTex("v_{y(t)}", "= v_0 \\sin(\\theta) - g t", font_size = 40).next_to(equation_y_5, DOWN, buff = 0.4)
        self.play(Write(equation_y_6))
        framebox_11 = SurroundingRectangle(equation_y_6)
        self.play(Create(framebox_11))

        time_tracker=ValueTracker(0)

        y_velocity_axes = Axes(
                x_range = [0, 2, 0.2], 
                y_range = [-10, 10, 2.5], 
                x_length = 5.0, 
                y_length = 3.0, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 2.4, 0.4)}, 
                y_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(-10, 10 +  5, 5)}, 
                tips = False)
        y_velocity_axes.to_edge(UP).to_edge(RIGHT)

        y_velocity_labels = y_velocity_axes.get_axis_labels(x_label=MathTex("t"), y_label=MathTex("v_y"))

        def plot_y_velocity():
            graph = y_velocity_axes.plot(lambda x: v0 * np.sin(theta) - g * x, x_range = [0, time_tracker.get_value()], 
            color = BLUE)
            return graph

        y_velocity = always_redraw(plot_y_velocity)

        def get_new_new_y_dot():
            y_dot = Dot(
                y_ax.coords_to_point(0, v0*np.sin(theta) * time_tracker.get_value() - g* (time_tracker.get_value())**2 /2), 
                color = PINK)
            return y_dot

        def get_new_y_sped_dot():
            y_dot = Dot(
                y_velocity_axes.coords_to_point(time_tracker.get_value(), v0*np.sin(theta) - g*time_tracker.get_value()), 
                color = PINK)
            return y_dot

        new_new_y_dot = always_redraw(get_new_new_y_dot)
        new_sped_dot = always_redraw(get_new_y_sped_dot)

        self.play(FadeIn(y_velocity, y_velocity_labels), FadeIn(y_velocity_axes, new_sped_dot))
        self.remove(new_y_dot)
        self.add(new_new_y_dot)
        self.play(time_tracker.animate.set_value(2*v0 * np.sin(theta) / g), run_time = 8, rate_func = rate_functions.linear)
        lll = VGroup(equation_y_6, framebox_11)
        self.play(FadeOut(equation_y_1, equation_y_2, equation_y_3, equation_y_4, equation_y_5))
        self.play(lll.animate.to_edge(UP), time_tracker.animate.set_value(0))
        self.play(FadeOut(framebox_11))


        self.wait(2)
        equation_vy_1 = MathTex("\\frac{d y}{dt}", "=v_0 \\sin(\\theta) - gt", font_size = 40).next_to(lll, DOWN, buff=0.4)
        self.play(Write(equation_vy_1))

        vybox = SurroundingRectangle(equation_y_6[0])
        dvtbox = SurroundingRectangle(equation_vy_1[0])

        self.wait(1.5)
        self.play(Create(vybox), Create(dvtbox))
        self.wait(1.5)
        self.play(FadeOut(vybox), FadeOut(dvtbox))


        self.wait(1.5)
        equation_vy_2 = MathTex("\\int\\limits^{y_{(t)}}_{0}", "dy =", "\\int\\limits^{t}_{0}", "v_0 \\sin(\\theta) dt", "-", "\\int\\limits^{t}_{0}", "g t dt", font_size=32).next_to(equation_vy_1, DOWN, buff=0.4)
        self.play(Write(equation_vy_2))

        equation_vy_3 = MathTex("y_{(t)} = v_0 \\sin(\\theta) t - \\frac{g t^2}{2}", font_size=40).next_to(equation_vy_2, DOWN, buff=0.4)
        self.play(Write(equation_vy_3))
        framebox_y = SurroundingRectangle(equation_vy_3)
        group = VGroup(framebox_y, equation_vy_3)
        self.play(Create(framebox_y))
        self.play(FadeOut(equation_vy_1, equation_vy_2), group.animate.next_to(lll, DOWN, buff=0.4))







        y_position_axes = axes = Axes(
                x_range = [0, 2, 0.2], 
                y_range = [0, 4, 1], 
                x_length = 5.0, 
                y_length = 3.0, 
                axis_config = {"color": WHITE}, 
                x_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 12, 2)}, 
                y_axis_config = {
                    "numbers_with_elongated_ticks": np.arange(0, 6, 2)}, 
                tips = False)
        y_position_axes.to_edge(DOWN)
        y_position_axes.to_edge(RIGHT)

        y_pos_labels = y_position_axes.get_axis_labels(x_label=MathTex("t"), y_label=MathTex("y"))

        def get_y_pos():
            graph = y_position_axes.plot(lambda x: v0 * np.sin(theta) * x - g * x**2 / 2, x_range = [0, time_tracker.get_value()], 
            color=BLUE)
            return graph

        def get_y_pos_dot():
            y_dot = Dot(
                y_position_axes.coords_to_point(time_tracker.get_value(), v0 * np.sin(theta) * time_tracker.get_value() - g * (time_tracker.get_value())**2 / 2), 
                color = PINK)
            return y_dot

        def get_pos_area():
            area = y_velocity_axes.get_area(plot_y_velocity(), x_range = (0, time_tracker.get_value()), opacity = 0.5)
            return area

        def get_tangent():
            graph = y_position_axes.plot(lambda x: v0 * np.sin(theta) * time_tracker.get_value() - g * (time_tracker.get_value())**2 / 2 + (v0*np.sin(theta)-g*time_tracker.get_value())*(x-time_tracker.get_value()), x_range = [0, 2])
            return graph

        y_pos = always_redraw(get_y_pos)
        y_pos_dot = always_redraw(get_y_pos_dot)
        y_vel_area=always_redraw(get_pos_area)
        tangent_line=always_redraw(get_tangent)
        

        self.play(FadeIn(tangent_line, y_pos_labels, y_pos, y_position_axes, y_pos_dot))
        self.add(y_vel_area, y_velocity_axes, new_sped_dot)
        self.play(time_tracker.animate.set_value(v0*np.sin(theta)/g), run_time=6.5)
        self.wait(1)
        self.play(time_tracker.animate.set_value(2*v0*np.sin(theta)/g), run_time=6.5)

        self.play(FadeOut(y_pos, y_pos_dot, y_vel_area, tangent_line, equation_vy_3, equation_y_6, framebox_y))
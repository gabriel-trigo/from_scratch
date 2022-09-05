# imports
import numpy as np
from manim import *

# scene 5
class Scene5(ThreeDScene):
    def construct(self):

        # static constants
        v0 = 10.0
        g = 10

        # individual stream trajectories
        def get_trajectory(theta):
            curve = ParametricFunction(
                lambda t: np.array([t/3, 0, (np.tan(theta)*t-g*t**2/(2*(v0*np.cos(theta))**2))/3]),
                t_range = [2*v0**2*np.cos(theta)*np.cos(theta)*np.tan(theta)/g, 0] if theta>np.pi/2 else [0, 2*v0**2*np.cos(theta)*np.cos(theta)*np.tan(theta)/g], 
                color=BLUE)
            return curve
        
        # collection of trajectories to animate together
        def draw_collection():
            graphs = []
            for angle in angles:
                graphs.append(get_trajectory(angle))
            return VGroup(*graphs)

        # parametrized safety parabola surface
        def param_gauss(v, u):
            return np.array([v/3*np.cos(u), v/3*np.sin(u), (v0**2/(2*g)-g*v**2/(2*v0**2))/3])

        # draw the surface
        def draw_surface():
            gauss_plane = Surface(
                param_gauss,
                resolution=(16, 16),
                v_range=[-phi_tracker.get_value(), phi_tracker.get_value()],
                u_range=[0, +10])
            gauss_plane.set_style(fill_opacity=1,stroke_color=GREEN)
            gauss_plane.set_fill_by_checkerboard(ORANGE, BLUE, opacity=0.1)
            return gauss_plane

        # create array with all trajectory angles
        angles = np.arange(0, np.pi+np.pi/13, np.pi/13)

        # 3D axes
        threedaxes = ThreeDAxes(
            x_range = [-6, 6, 1], 
            y_range = [-6, 6, 1], 
            z_range = [-12, 12, 2])

        # safety parabola
        threedcurve = ParametricFunction(
            lambda t: np.array([t/3, 0, (v0**2/(2*g)-g*t**2/(2*v0**2))/3]), 
            t_range=[-10, 10], 
            color=PINK)

        # all the individual stream
        collection = draw_collection()

        # phi tracker
        phi_tracker = ValueTracker(0)

        # always redraw elements
        surface = always_redraw(draw_surface)

        # animation
        self.move_camera(phi=75*DEGREES, theta=-60*DEGREES)
        self.play(FadeIn(threedaxes))
        self.play(FadeIn(threedcurve))
        self.add(collection, threedcurve, threedaxes)
        self.play(FadeIn(collection))
        self.add(surface)
        self.play(phi_tracker.animate.set_value(np.pi), run_time=2)
        self.wait(1)
from velocity_plot import VelocityPlotter as VP 

def plot_velocity(d_init: float, h_init: float, r: float, w: float, d_range: list, h_range: list):
    plotter = VP(d_init,h_init,r,w,d_range,h_range)

    plotter.plot_mesh()

plot_velocity(3.0, 2.5, 0.1, 25, [0, 500], [0,100])
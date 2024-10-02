import math 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

class VelocityPlotter():

    def __init__(self, d_init: float, h_init: float, r: float, w: float, d_range: list, h_range: list):

        self.d_init = d_init
        self.h_init = h_init
        self.r = r
        self.w = w
        self.d_range = d_range
        self.h_range = h_range

    def initialize_mesh(self):

        d_mesh, h_mesh = np.meshgrid(self.d_range, self.h_range)

        return d_mesh, h_mesh

    def velocity_function(self,d,h):
        return ((2*self.r*self.w)/(math.pi))*math.sqrt((1-((d/self.r) + (h/self.r) - 1))**2)
    
    def apply_velocity_to_mesh(self):
        d_mesh, h_mesh = self.initialize_mesh()

        # Use numpy.vectorize to apply the velocity_function to each element of the meshgrid
        vectorized_velocity = np.vectorize(self.velocity_function)
        velocity_mesh = vectorized_velocity(d_mesh, h_mesh)

        return velocity_mesh
    
    def plot_mesh(self):

        d_mesh, h_mesh = self.initialize_mesh()
        velocity_grid = self.apply_velocity_to_mesh()

        colormin = np.min(velocity_grid)
        colormplt = np.max(velocity_grid)

        plt.figure()
        im = plt.contourf(d_mesh, h_mesh, velocity_grid, levels=np.linspace(colormin, colormplt, 70), cmap = 'viridis', origin = 'lower', extent=(self.d_range[0], self.d_range[1], self.h_range[0], self.h_range[1]))
        plt.title('Velocity Grid')
        plt.xlabel("D (depth of insertion, m)")
        plt.ylabel("H (height to belly, m)")
        plt.ticklabel_format(useOffset=False)
        plt.tick_params(axis='both', which='major', labelsize=7)
        axs = plt.gca()
        axs.xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
        axs.set_xticks(axs.get_xticks(), axs.get_xticklabels(), rotation=90)
        axs.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
        axs.set_yticks(axs.get_yticks(), axs.get_yticklabels(), rotation=90)
        cbar = plt.colorbar(im, ax=axs, shrink=0.9)
        cbar.ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
        cbar.set_label("Velocity (m/s)", rotation = 270, labelpad = 20)

        plt.tight_layout()
        plt.show()

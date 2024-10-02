import math 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

class VelocityPlotter():

    def __init__(self, d_dict: dict, h: float, r: float, w: float):

        self.d_dict = d_dict
        self.h = h
        self.r = r
        self.w = w

        

    def plot(self):
        """This is the plotting function that you call to plot the velocity mesh for
        all stiffness grids predicted by the heatmap. 
        """

        for d_mesh in self.d_dict.values():
            if isinstance(d_mesh, np.ndarray):
                self.plot_mesh(d_mesh)
            else:
                raise ValueError("Input mesh is of wrong type.")

    def velocity_function(self,d):
        return ((2*self.r*self.w)/(math.pi))*math.sqrt((1-((d/self.r) + (self.h/self.r) - 1))**2)
    
    def apply_velocity_to_mesh(self, d_mesh: np.ndarray):
        
        vectorized_velocity = np.vectorize(self.velocity_function)
        velocity_mesh = vectorized_velocity(d_mesh)

        return velocity_mesh
    
    def plot_mesh(self, d_mesh):

        velocity_grid = self.apply_velocity_to_mesh(d_mesh)

        colormin = np.min(velocity_grid)
        colormplt = np.max(velocity_grid)


        plt.figure()
        nrows, ncols = d_mesh.shape
        extent = (0, ncols, 0, nrows)
        im = plt.imshow(velocity_grid, cmap = 'viridis', origin = 'lower', extent=extent)
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

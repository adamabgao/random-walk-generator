import matplotlib.pyplot as plt
from randomwalk import RandomWalk

class RWGenerator:
    '''A generator class for random walk objects that creates different plots.'''

    def __init__(self, num_steps = 5000):
        self.num_steps = num_steps
        self.rw = RandomWalk(num_steps = self.num_steps)

    def scatter(self, dot_size = 10, savefig = False):
        '''Creates a scatterplot of a RandomWalk object.'''
        #creates instant scatterplot w/rw object
        rw = self.rw
        a, b = rw.go_for_walk()

        #container
        plt.style.use('ggplot')
        fig, ax = plt.subplots(1, 1, figsize = (10, 5))

        #style
        ax.set_title('A Random Walk')
        ax.text(0.5, -0.05, f"steps: {self.num_steps}", fontsize = 8, ha = "center",
                 transform = ax.transAxes)
        ax.set_xlabel('x pos')
        ax.set_ylabel('y pos')
        ax.set_aspect('equal')
        ax.tick_params('both', labelsize = 10)
        point_numbers = range(rw.num_steps)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        #plot graph
        ax.scatter(a, b, c = point_numbers, cmap = plt.cm.plasma, edgecolors= 'none', s = dot_size)
        ax.scatter(0, 0, c = 'green', edgecolors= 'none', s = 100)
        ax.scatter(rw.x_list[-1], rw.y_list[-1], c = 'red', edgecolor = 'none', s = 100)

        if savefig:
            plt.savefig(f"rw_plot.png", dpi = 300, bbox_inches='tight')
        else:
            plt.show()
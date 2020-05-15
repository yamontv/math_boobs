import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Boobs:
    def __init__(self, px_num=100):
        ls = np.linspace(-10, 10, px_num)
        points = []
        for x in ls:
            for y in ls:
                points.append((x, y, self._calculate(x, y)))
        self.df = pd.DataFrame(points, columns=['X', 'Y', 'Z'])

    def render(self):
        # Make the plot
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot_trisurf(self.df['X'],
                        self.df['Y'],
                        self.df['Z'],
                        cmap=plt.cm.viridis)
        # Hide grid lines
        plt.axis('off')
        plt.grid(b=None)
        #set normal scale
        ax.auto_scale_xyz([-7, 7], [-7, 7], [0, 2])
        plt.show()

    def _calculate(self, x, y):
        left = -((x + 4)**2 + (y + 4)**2)**2
        right = -((x - 4)**2 + (y - 4)**2)**2
        return np.exp(left / 1000) + np.exp(
            right / 1000) + 0.1 * (np.exp(left) + np.exp(right))


if __name__ == "__main__":
    boobs = Boobs()
    boobs.render()

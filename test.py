import numpy
import matplotlib.pyplot as plt

a = 3
a += 4


class Test:
    def __init__(self):
        self.x = numpy.linspace(0, 10, 100)
        self.y = numpy.sin(self.x)

    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()

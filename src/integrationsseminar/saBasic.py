import matplotlib.pyplot as plt
import numpy as np

def pyplotPlot():
    xpoints = [0, 6]
    #ypoints = [0, 250]
    ypoints = np.array([3, 8, 1, 10])
    #plt.plot(xpoints, ypoints)
    #plt.plot(ypoints, marker = 'o')

    plt.title('Verteilung der Reichweite der E-Scooter')
    plt.show()


pyplotPlot()
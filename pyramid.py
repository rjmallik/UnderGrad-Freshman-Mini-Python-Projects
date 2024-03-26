import numpy as np
import matplotlib.pyplot as plt
def pyramid(n, height):
    theta = np.linspace(0, 2*np.pi, n+1)
    r = np.linspace(-1, n, n+1)

    height, Theta = np.meshgrid(theta, r)

    a = height * np.cos(Theta)
    b = height * np.sin(Theta)
    c = -height

    return a, b, c

if __name__ == '__main__':
   
    fig = plt.figure(tight_layout=True)
    ax = fig.add_subplot(121, projection='3d')
    x, y, z = pyramid(4, 5)
    ax.contour3D (x, y, z, 50)
    ax = fig.add_subplot(122, projection='3d')
    x, y, z = pyramid(6, 10)
    ax.contour3D(x, y, z, 50)
    plt.show()

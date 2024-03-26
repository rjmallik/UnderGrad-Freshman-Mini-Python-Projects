import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 
figure1 = plt.figure()

#use plot_wireframe for hyperbolic paraboloid
ax = figure1.add_subplot(4, 2, 1, projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30) 
X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Y
a,b = 0.5, 1
Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z
ax.plot_wireframe(X, Y, Z)
ax.set_title('Hyperbolic Paraboloid')

#use plot_wireframe for elliptic paraboloid
ax = figure1.add_subplot(4, 2, 2, projection='3d')
x = np.linspace(-7, 7, 100)
y = np.linspace(-7, 7, 100)
X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Y
Z = (X**2)/50 + (Y**2)/100             # make a 2D array and assign it to Z
ax.plot_wireframe(X, Y, Z)
ax.set_title('Elliptic Paraboloid')

#use plot_wireframe for hyperbolic hyperboloid
ax = figure1.add_subplot(4, 2, 3, projection='3d')
x = np.linspace(-1, 1, 100)
y = np.linspace(0, np.pi*2, 50)
x, y = np.meshgrid(x,y)
X = np.cosh(x)*np.cos(y)
Y = np.cosh(x)*np.sin(y)
Z = np.sinh(x)
ax.plot_wireframe(X, Y, Z)
ax.set_title('Hyperbolic Hyperboloid')

#use plot_wireframe for Elliptic hyperboloid
ax = figure1.add_subplot(4, 2, 4, projection='3d')
x = np.linspace(0, np.pi*2, 50)
y = np.linspace(0, np.pi*2, 50)
x, y = np.meshgrid(x,y)
X = np.sinh(x)*np.cos(y)
Y = np.sinh(x)*np.sin(y)
Z = np.cosh(x)
ax.plot_wireframe(X, Y, Z)
ax.set_title('Elliptic Hyperboloid')

#use plot_wireframe for sphere
ax = figure1.add_subplot(4, 2, 5, projection='3d')
x = np.linspace(0, np.pi, 50)
y = np.linspace(0, np.pi*2, 50)
x, y = np.meshgrid(x,y)
r = 5
X = r*np.sin(x)*np.cos(y)
Y = r*np.sin(x)*np.sin(y)
Z = np.cos(x)
ax.plot_wireframe(X, Y, Z)
ax.set_title('Sphere')

#use plot_wireframe for cone
ax = figure1.add_subplot(4, 2, 6, projection='3d')
angle = np.linspace(0, np.pi*2, 50)
y = np.linspace(-2, 0, 50)
angle, y = np.meshgrid(angle,y)
X = y*np.cos(angle)
Y = y*np.sin(angle)
Z = 5*y
ax.plot_wireframe(X, Y, Z) 
ax.set_title('Cone')

#use plot_wireframe for square pyramid
ax = figure1.add_subplot(4, 2, 7, projection='3d')
zeros = np.zeros([512, 512])
x = zeros.shape[0]
y = zeros.shape[1]
for item in range(x // 2):
    for next in range(item, x - item):
        for last in range(item, x - item):
            zeros[next, last] = item
X, Y = np.meshgrid(range(x), range(y))
ax.plot_wireframe(X, Y, zeros)
ax.set_title('Pyramid')

#use plot parallelepiped
ax = figure1.add_subplot(4, 2, 8, projection='3d')
x = np.array([0, 5, 6, 5, 0,-1, 0, 0, 5, 5, 5, 5, 5, -1, 0, 0, 0, 0, 5, 5, 6, 6, -1])
y = np.array([0, 3, 6, 7, 6, 1, 0, 0, 3, 3, 7, 7, 3, 1, 0, 0, 5, 6, 7, 7, 6, 6, 1])
z = np.array([0, 1, 6, 10, 7, 4, 0, 0, 1, 8, 10, 10, 8, 4, 0, 0, 3, 7, 10, 10, 6, 6, 4])
ax.plot3D(x, y, z)
ax.scatter3D(x, y, z)
ax.set_title('Parallelepiped')

figure1.tight_layout()
plt.show()
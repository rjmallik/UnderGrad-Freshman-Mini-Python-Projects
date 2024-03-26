# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# main
figure1 = plt.figure(figsize=(8,8))

sample = figure1.add_subplot(1, 1, 1, polar=True)
sample.set_title("Rose Curve", pad = 20)

a , z = 5, 1
theta = np.linspace(0, z/a*30*np.pi, 800)
r = np.cos(theta * a / z)
line, = plt.plot(theta+(r<0)*np.pi, np.abs(r))

coord1 = plt.axes([0.25, 0.15, 0.65, 0.03])
coord2 = plt.axes([0.25, 0.1, 0.65, 0.03])

slide1 = Slider(coord1, 'n', 1, 7, 5)
slide2 = Slider(coord2, 'd', 1, 9, 1)

def change(val):
    n = int(slide1.val)
    d = int(slide2.val)
    line.set_ydata(np.cos(theta * n / d))

slide1.on_changed(change)
slide2.on_changed(change)

# display graph
plt.show()
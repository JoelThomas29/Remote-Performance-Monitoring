""" This program takes the cpu input and plots continuous graph """

import matplotlib.pyplot as pyp
import matplotlib.animation as animation

figure = pyp.figure()
subplot = figure.add_subplot(1,1,1)

def animate(i):
    cpu_info = open("config_output.txt", 'r').readlines()

    temp = []
    for each_line in cpu_info:
        if len(each_line) > 1:
            temp.append(float(each_line))

    # Clearing/refreshing the figure to avoid unnecessary overwriting for each new poll
    subplot.clear()

    # Plotting values in the temp list
    subplot.plot(temp)

graph = animation.FuncAnimation(figure, animate, interval=5000)
pyp.show()

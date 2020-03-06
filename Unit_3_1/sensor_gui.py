from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
import gdx, matplotlib.pyplot as plt, numpy as np


gdx = gdx.gdx()
gdx.open_usb()
gdx.select_sensors(sensors=[5,6,7])
root = Tk()


def start_recording():
    seconds = int(seconds_entry.get())
    samples = int(samples_entry.get())
    axis = np.arange(0,seconds,1/samples)
    gdx.start(1000//samples)
    red = []
    green =[]
    blue = []
    # fig, ax = plt.subplots(1,1)
    ax.cla()

    for _ in range(seconds * samples):
        # print(gdx.read())
        vals = gdx.read()
        if vals == None:
            break
        r,g,b = vals
        red.append(r)
        green.append(g)
        blue.append(b)
    
    gdx.stop()

    print(axis)
    ax.plot(axis,red, color = 'r')
    ax.plot(axis, green, color = 'g')
    ax.grid()
    ax.plot(axis,blue, color = 'b')
    ax.legend(['r', 'g', 'b'])
    ax.set_title("Lights")
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('lux')
    # chart.show()
    


seconds_label = Label(root, text= 'How Many seconds?')
seconds_label.grid(row = 1, column = 0)
seconds_entry = Entry(root)
seconds_entry.grid(row = 2, column = 0)


samples_label = Label(root, text= 'How many samples/seconds')
samples_label.grid(row = 3, column = 0)
samples_entry = Entry(root)
samples_entry.grid(row = 4, column = 0)

start_button = Button(root, text= 'Start Recording', command = start_recording)
start_button.grid(row = 5, column = 0)

fig, ax = plt.subplots(1,1)   
chart = FigureCanvasTkAgg(fig, root)
chart.get_tk_widget().grid(row = 2, column = 1, rowspan = 100)

plt.ion()




root.mainloop()
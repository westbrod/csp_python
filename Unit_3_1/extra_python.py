import gdx, numpy as np
from tkinter import *


root = Tk()

grip_sensor = gdx.gdx()
grip_sensor.open_usb()

grip_data_label = Label(root, text=0)
grip_data_label.pack()

root.geometry('400x300')

def start_grip_recording():
    samples = (10)
    grip_sensor.start(1000/samples)
    count.set(0)
    change_text()
    
    #for _ in range(seconds * samples):
        
        #print(grip_data)
        
def change_text():
    grip_data = grip_sensor.read()[0]
    grip_data_label.config(text=int(grip_data))
    if count.get() < 35:
        count.set(count.get() + 1)
        root.after(100, change_text)
    else:
        grip_sensor.stop()

        print('Done')

count = IntVar()
count.set(0)
start_button = Button(root, text='Start Recording', command=start_grip_recording)
start_button.pack()


root.mainloop()
        


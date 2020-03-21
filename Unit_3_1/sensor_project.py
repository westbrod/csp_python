import gdx, numpy as np
from tkinter import *


root = Tk()

root.geometry('210x150')
root.title('Strenght game')

grip_sensor = gdx.gdx()
grip_sensor.open_usb()

grip_data_label = Label(root, text=0)
grip_data_label.grid()


questionlabel = Label(root, text = "what's your name?")
questionlabel.grid(row=0, column= 0)

question1Entry = Entry(root)
question1Entry.grid(row=1, column= 0)


leaderboard = []
question2Entry = Entry(root)

def submit_button():
        leaderboard.append(question1Entry.get())
        root.geometry('700x150')
        questionlabel.config(text= 'Welcome '+ leaderboard [0] + '! ' + 'press start recored and grip the sensor, test your strenght with your friends!')
        submitbutton.grid_forget()
 
        

submitbutton = Button(root, text = 'sumbit', command= submit_button )
submitbutton.grid(row=3, column= 0)



grip_data_label = Label(root, text=0)
grip_data_label.grid(row=4, column= 0)


def start_grip_recording():
    samples = (10)
    grip_sensor.start(1000/samples)
    count.set(0)
    change_text()
    

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
start_button.grid(row=5, column= 0)


root.mainloop()

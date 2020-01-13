import tkinter as tk 

def callback():
    print ("button pressed")

root = tk.Tk()
root.geometry("400x300")

user_label = tk.Label(root, text='Username')
user_label.pack()

user_text =tk.Entry(root)
user_text.pack()
user_submit = user_text.get()


user_label = tk.Label(root, text='Password ')
user_label.pack()

Pass_text =tk.Entry(root)
Pass_text.pack()
Pass_text = tk.Entry(root, show='*')

Pass_submit = tk.Button(root, text= 'submit', command= callback)
Pass_submit.pack()

root.mainloop()

import tkinter as tk 

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
Pass_submit = Pass_text.get()

def callback():
    print ("click!")

b = button(master, text="Submit", command=callback)
b.pack()




root.mainloop()
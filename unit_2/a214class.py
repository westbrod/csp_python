import tkinter as tk 
import string

def callback():
    print ("User:", user_entry.get())
    print ("Pass:", Pass_text.get())


root = tk.Tk()
root.geometry("400x300")

user_label = tk.Label(root, text='Username')
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack(pady=5)

user_label = tk.Label(root, text='Password ')
user_label.pack()

Pass_text = tk.Entry(root, show='')
Pass_text.pack()


Pass_submit = tk.Button(root, text= 'submit', command= callback)
Pass_submit.pack()



def pass_check():
    if len(Pass_text.get()) <= 8:
        print("Good")
    else:
        print("Please enter a password longer than 8 characters. ")

def special_check():
    if (Pass_test.get()) == Special:
        print(Good)
    else:
        print("please enter at least one special character.")



def submit_sign_up():
    password = password_entry.get()



def is_valid_password(password):
    if len(password) < 8:



    





signup_submit = tk.Button(root, text= 'sighup', command= pass_check )
signup_submit.pack()





root.mainloop()

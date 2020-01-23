import tkinter as tk 
import string
from passlib.hash import pbkdf2_sha256

#pbkdf2_sha256.verify(Pass_text.get(), users[user_entry.get()])

result = ("you have been signed up")
users = {}


def callback():
    if user_entry.get() not in users:
        result_label.config(text = 'Username not found. ')
    elif pbkdf2_sha256.verify(Pass_text.get(), users[user_entry.get()]):
        result_label.config(text="valid log in")
    else:
        result_label.config(text='invalid password')



def submit_sign_up():
    hash_pass = pbkdf2_sha256.hash(Pass_text.get())   

    if user_entry.get() in users:
        result_label.config(text='username is already in use.')

    else: 
        user1 = users[user_entry.get()] = hash_pass
        if is_valid_password(Pass_text.get()):
            result_label.config(text= 'valid sign up ')
        else:
            result_label.config(text= 'Not a valid sign up')


def is_valid_password(password):
    if len(password) < 8:
        return False 

    has_upper = False 
    has_lower = False 
    has_digit = False
    has_special = False 

    for char in password:
        if char.islower():
            has_lower = True 
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    return has_lower and has_upper and has_digit and has_special


root = tk.Tk()
root.geometry("400x300")

#user label and txt box 
user_label = tk.Label(root, text='Username')
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack(pady=5)

pass_label = tk.Label(root, text='Password ')
pass_label.pack()

  

#password txt box and label
Pass_text = tk.Entry(root, show='')
Pass_text.pack()

login = tk.Button(root, text= 'Login', command= callback)
login.pack()


result_label = tk.Label(root, text = 'result')
result_label.pack(pady=20)


signup_submit = tk.Button(root, text= 'sighup', command= submit_sign_up )
signup_submit.pack()


root.mainloop()

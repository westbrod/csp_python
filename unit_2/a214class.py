import tkinter as tk 
import string

result = ("you have been signed up")
users = {}

def callback():
    print ("User:", user_entry.get())
    print ("Pass:", Pass_text.get())





# def import_users():
#     # users ['simmonsjo5'] = 'password'
#     users [user_entry.get] = pass_text.get 
    

def is_valid_password(password):
    if len(password) < 8:
        return False  
    # return True

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

#user label anf txt box 
user_label = tk.Label(root, text='Username')
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack(pady=5)

user_label = tk.Label(root, text='Password ')
user_label.pack()

#password txt box and label
Pass_text = tk.Entry(root, show='')
Pass_text.pack()


Login= tk.Button(root, text= 'Login', command= callback)
Login.pack()

def submit_sign_up():
    namelater = Pass_text.get()
    
    if is_valid_password(namelater):
        result_label.config(text= 'valid sign up ')
    else:
        result_label.config(text= 'Not a valid sign up') 
    
    users.append[user_entry.get()] = pass_text.get()
    


signup_submit = tk.Button(root, text= 'sighup', command= submit_sign_up)
signup_submit.pack()

result_label = tk.Label(root, text = result )
result_label.pack(pady=20)




root.mainloop()

from tkinter import *
root=Tk()
root.title("Password checker")
root.geometry("300x200")
def check_password():
    password=entry.get()
    if len(password)==0:
        result_label.config(text="Please enter a password")
    elif len(password)<5:
        result_label.config(text="Weak password",fg="red")
    elif len(password)<8:
        result_label.config(text="Mediuim password",fg="orange")
    else:
        result_label.config(text="Strong password",fg="green")
Label(root,text="Enter password: ").pack(pady=10)
entry=Entry(root,show="*")
entry.pack(pady=5)
Button(root,text="Check",command=check_password).pack(pady=10)
result_label=Label(root,text="")
result_label.pack(pady=10)
root.mainloop()
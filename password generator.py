# Importing Libraries
from tkinter import *
import random, string
import pyperclip

### initialize window
root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("edSlash Coding Hub - PASSWORD GENERATOR")

# heading
Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='edSlash Coding Hub', font='arial 15 bold').pack(side=BOTTOM)

### select password length
Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
pass_len = IntVar(value=8)  # Default length
Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

##### define function
pass_str = StringVar()

def Generator():
    password = []

    # Ensure at least one character from each category
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))

    if pass_len.get() < 4:
        pass_str.set("Length must be >= 4")
        return

    # Fill the rest of the password length
    for _ in range(pass_len.get() - 4):
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    # Join and update StringVar
    pass_str.set(''.join(password))

### button
Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str, width=30).pack()

######## function to copy
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

# loop to run program
root.mainloop()

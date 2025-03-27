from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
import json
import os
from auth_sha256 import hash_password, authenticate_user

class AuthApp:
    def __init__(self, master):
        self.master = master
        master.title("Authentication App")

        self.username_label = Label(master, text="Username:")
        self.username_label.pack()

        self.username = StringVar()
        self.username_entry = Entry(master, textvariable=self.username)
        self.username_entry.pack()

        self.password_label = Label(master, text="Password:")
        self.password_label.pack()

        self.password = StringVar()
        self.password_entry = Entry(master, textvariable=self.password, show='*')
        self.password_entry.pack()

        self.register_button = Button(master, text="Register", command=self.register_user)
        self.register_button.pack()

        self.login_button = Button(master, text="Login", command=self.login_user)
        self.login_button.pack()

    def register_user(self):
        username = self.username.get()
        password = self.password.get()
        hashed_password = hash_password(password)

        if os.path.exists("data.json"):
            with open("data.json", "r") as file:
                users = json.load(file)
        else:
            users = []

        users.append({"username": username, "password": hashed_password})

        with open("data.json", "w") as file:
            json.dump(users, file, indent=4)

        messagebox.showinfo("Success", f"User {username} registered successfully!")

    def login_user(self):
        username = self.username.get()
        password = self.password.get()
        hashed_password = hash_password(password)

        if os.path.exists("data.json"):
            with open("data.json", "r") as file:
                users = json.load(file)

            for user in users:
                if user.get('username') == username and user.get('password') == hashed_password:
                    messagebox.showinfo("Welcome", f"Welcome {username}")
                    return
            messagebox.showerror("Error", "Incorrect username or password!")
        else:
            messagebox.showerror("Error", "No registered users.")

if __name__ == "__main__":
    root = Tk()
    app = AuthApp(root)
    root.mainloop()
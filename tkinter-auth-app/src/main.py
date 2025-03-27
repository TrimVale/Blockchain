import tkinter as tk
from tkinter import messagebox
from auth_sha256 import hash_password, register_user, authenticate_user
import os
import json

def authenticate_user(username, password):
    """Authenticate a user by username and password."""
    hashed_password = hash_password(password)

    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            users = json.load(file)
        
        for user in users: 
            if user.get('username') == username and user.get('password') == hashed_password:
                return True
        return False
    else:
        return False

def registra_utente():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        register_user(username, password)
        messagebox.showinfo("Successo", f"Utente {username} registrato con successo!")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        messagebox.showwarning("Errore", "Inserisci sia username che password.")

def accedi():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        if authenticate_user(username, password):  # Passa i parametri
            messagebox.showinfo("Successo", f"Benvenuto {username}!")
        else:
            messagebox.showerror("Errore", "Nome utente o password errati!")
    else:
        messagebox.showwarning("Errore", "Inserisci sia username che password.")

# Creazione della finestra principale
root = tk.Tk()
root.title("Sistema di Autenticazione")

# Creazione dei widget
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_register = tk.Button(root, text="Registrati", command=registra_utente)
button_register.grid(row=2, column=0, padx=10, pady=10)

button_login = tk.Button(root, text="Accedi", command=accedi)
button_login.grid(row=2, column=1, padx=10, pady=10)

# Avvio del loop principale di Tkinter
root.mainloop()
import tkinter as tk
from tkinter import messagebox
from auth_sha256 import hash_password, register_user, authenticate_user
import os
import json

def registra_utente():
    try:
        username = entry_username.get()
        password = entry_password.get()

        if not username or not password:
            messagebox.showerror("Errore", "Nome utente e password sono obbligatori!")
            return

        risultato = register_user(username, password)
        if risultato == "Utente già esistente":
            messagebox.showwarning("Attenzione", "Utente già esistente!")
        else:
            messagebox.showinfo("Successo", "Registrazione completata!")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

def accedi():
    username = entry_username.get()
    password = entry_password.get()

    if authenticate_user(username, password):
        messagebox.showinfo("Successo", "Accesso effettuato!")
    else:
        messagebox.showerror("Errore", "Nome utente o password errati!")

# Creazione della finestra principale
root = tk.Tk()
root.title("Autenticazione Utente")

# Creazione dei widget
label_username = tk.Label(root, text="Nome utente:")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_register = tk.Button(root, text="Registra", command=registra_utente)
button_register.grid(row=2, column=0, padx=10, pady=10)

button_login = tk.Button(root, text="Accedi", command=accedi)
button_login.grid(row=2, column=1, padx=10, pady=10)

# Avvio del loop principale di Tkinter
root.mainloop()

# filepath: /home/ifts/Desktop/Blockchain/tkinter-auth-app/src/auth_sha256.py
def register_user(username, password):
    """Register a new user with a hashed password."""
    hashed_password = hash_password(password)
    user = {"username": username, "password": hashed_password}

    # Load existing users or initialize an empty list
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            try:
                users = json.load(file)
                # Verifica che ogni elemento sia un dizionario valido
                if not all(isinstance(u, dict) and "username" in u and "password" in u for u in users):
                    raise ValueError("Dati non validi in data.json")
            except (json.JSONDecodeError, ValueError):
                users = []  # Se i dati sono corrotti, inizializza una lista vuota
    else:
        users = []

    # Check if the username already exists
    for existing_user in users:
        if existing_user["username"] == username:
            return "Utente già esistente"

    # Add the new user
    users.append(user)

    # Save the updated users list
    with open("data.json", "w") as file:
        json.dump(users, file)

    return "Registrazione completata"
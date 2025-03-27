import tkinter as tk
from tkinter import messagebox
from auth_sha256 import register_user

def registra_utente_gui():
    """Funzione per registrare un utente tramite GUI."""
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

# Creazione della finestra principale
root = tk.Tk()
root.title("Registrazione Utente")

# Creazione dei widget
label_username = tk.Label(root, text="Nome utente:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

button_register = tk.Button(root, text="Registra", command=registra_utente_gui)
button_register.pack()

# Avvio del loop principale della GUI
root.mainloop()
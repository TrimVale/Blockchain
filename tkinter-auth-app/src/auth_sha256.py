import os
import json
import hashlib

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user with a hashed password."""
    hashed_password = hash_password(password)
    user = {"username": username, "password": hashed_password}

    # Load existing users or initialize an empty list
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            users = json.load(file)
    else:
        users = []

    # Add the new user
    users.append(user)

    # Save the updated users list
    with open("data.json", "w") as file:
        json.dump(users, file, indent=4)

    print(f"Utente {username} registrato con successo!")

def authenticate_user():
    """Authenticate a user by username and password."""
    username = input("Inserisci il tuo username: ")
    password = input("Inserisci la tua password: ")
    hashed_password = hash_password(password)

    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            users = json.load(file)
        
        for user in users: 
            if user.get('username') == username and user.get('password') == hashed_password:
                print(f"Benvenuto {username}")
                return True
        print("Nome utente o password errati!")
    else:
        print("Nessun utente registrato.")
    
    return False
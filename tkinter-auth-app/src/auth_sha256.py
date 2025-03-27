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
            try:
                users = json.load(file)
                # Verifica che ogni elemento sia un dizionario valido
                if not isinstance(users, list) or not all(
                    isinstance(u, dict) and "username" in u and "password" in u for u in users
                ):
                    raise ValueError("Dati non validi in data.json")
            except (json.JSONDecodeError, ValueError):
                users = []  # Se i dati sono corrotti, inizializza una lista vuota
    else:
        users = []

    print("Users caricati:", users)

    # Check if the username already exists
    for existing_user in users:
        if existing_user["username"] == username:
            return "Utente già esistente"

    # Add the new user
    users.append(user)

    print("Nuovo utente:", user)

    # Save the updated users list
    with open("data.json", "w") as file:
        json.dump(users, file, indent=4)

    return "Registrazione completata"

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
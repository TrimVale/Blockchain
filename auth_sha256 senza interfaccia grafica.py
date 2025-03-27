import hashlib
import json
import os

def hash_password(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

def register_user():
    username = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")
    
    hashed_password = hash_password(password)

    user_data = {
        'username': username,
        'password': hashed_password
    }
    
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            users = json.load(file)
    else:
        users = []

    users.append(user_data)
    
    with open("data.json", "w") as file:
        json.dump(users, file, indent=4)

    print(f"Utente {username} registrato con successo!")

def authenticate_user():
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

def main():
    while True:
        action = input("Scegli un'azione (1: Registrati, 2: Accedi, 3: Esci): ")
        
        if action == '1':
            register_user()
        elif action == '2':
            if authenticate_user():
                print("Accesso effettuato con successo!")
                break
            else:
                print("Autenticazione fallita, riprova.")
        elif action == '3':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida, riprova.")

if __name__ == "__main__":
    main()

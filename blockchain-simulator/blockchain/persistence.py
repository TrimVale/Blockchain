def salva_blockchain_su_file(blockchain, nome_file):
    import json
    with open(nome_file, 'w') as file:
        json.dump(blockchain, file)  # Salva la blockchain nel file

def carica_blockchain_da_file(nome_file):
    import json
    with open(nome_file, 'r') as file:
        return json.load(file)  # Carica la blockchain dal file
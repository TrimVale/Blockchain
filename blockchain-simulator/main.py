import json
from blockchain.blockchain import Blockchain

# Funzione per salvare la blockchain su un file JSON
def salva_blockchain(blockchain, filename="blockchain.json"):
    with open(filename, "w") as file:
        json.dump(blockchain.chain, file, indent=4)
    print("Blockchain salvata su file.")

# Funzione per caricare la blockchain da un file JSON
def carica_blockchain(filename="blockchain.json"):
    try:
        with open(filename, "r") as file:
            chain = json.load(file)
            print("Blockchain caricata da file.")
            return chain
    except FileNotFoundError:
        print("Nessun file trovato. Creazione di una nuova blockchain.")
        return []

def main():
    blockchain = Blockchain()
    
    # Carica la blockchain da file, se esiste
    blockchain.chain = carica_blockchain()
    if not blockchain.chain:
        blockchain.crea_blocco_iniziale()  # Crea un blocco iniziale se la blockchain è vuota

    while True:
        print("\nBlockchain Simulator")
        print("1. Crea nuovo blocco")
        print("2. Visualizza blockchain")
        print("3. Esci")
        
        choice = input("Scegli un opzione: ")
        
        if choice == '1':
            nome_transazione = input("Inserisci nome di transazione: ")
            dettagli_transazione = input("Inserisci i dettagli della transazione: ")
            blockchain.aggiungi_transazione(nome_transazione, dettagli_transazione)
            print("Blocco aggiunto!")
            
            # Salva la blockchain su file dopo aver aggiunto un nuovo blocco
            salva_blockchain(blockchain)
        
        elif choice == '2':
            print("\n--- Blockchain ---")
            for blocco in blockchain.chain:
                print(f"\nBlocco #{blocco.get('indice', 'N/A')}")
                print(f"  Timestamp: {blocco.get('timestamp', 'N/A')}")
                print(f"  Hash Precedente: {blocco.get('hash_precedente', 'N/A')}")
                print(f"  Hash Corrente: {blocco.get('hash_corrente', 'N/A')}")
                
                transazioni = blocco.get('transazione', [])
                if transazioni:
                    print("  Transazioni:")
                    for i, transazione in enumerate(transazioni, start=1):
                        print(f"    {i}. Nome: {transazione.get('nome_transazione', 'N/A')}")
                        print(f"       Dettagli: {transazione.get('dettagli_transazione', 'N/A')}")
                else:
                    print("  Nessuna transazione in questo blocco.")
            print("\n--- Fine Blockchain ---")
        
        elif choice == '3':
            print("Uscita in corso...")
            break
        
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
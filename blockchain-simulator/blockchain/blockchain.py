import time
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.crea_blocco_iniziale()

    def crea_blocco_iniziale(self):
        # Crea il blocco iniziale (genesis block)
        blocco_iniziale = {
            'indice': 0,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'transazione': [],
            'hash_precedente': '0',
            'hash_corrente': self.calcola_hash(0, '0', [])
        }
        self.chain.append(blocco_iniziale)

    def calcola_hash(self, indice, hash_precedente, transazione):
        # Calcola l'hash per un blocco
        blocco_stringa = f"{indice}{hash_precedente}{transazione}{time.time()}"
        return hashlib.sha256(blocco_stringa.encode()).hexdigest()

    def aggiungi_transazione(self, nome_transazione, dettagli_transazione):
        # Aggiunge una nuova transazione creando un nuovo blocco
        ultimo_blocco = self.chain[-1]
        nuovo_indice = ultimo_blocco['indice'] + 1
        hash_precedente = ultimo_blocco['hash_corrente']
        transazione = [{'nome_transazione': nome_transazione, 'dettagli_transazione': dettagli_transazione}]
        
        nuovo_blocco = {
            'indice': nuovo_indice,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'transazione': transazione,
            'hash_precedente': hash_precedente,
            'hash_corrente': self.calcola_hash(nuovo_indice, hash_precedente, transazione)
        }
        self.chain.append(nuovo_blocco)

    def get_chain(self):
        return self.chain

    def __repr__(self):
        # Rappresentazione leggibile della blockchain
        return f"Blockchain({self.chain})"
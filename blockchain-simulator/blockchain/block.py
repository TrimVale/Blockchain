class Blocco:
    def __init__(self, indice, timestamp, nome_transazione, dettagli_transazione, hash_precedente):
        self.indice = indice
        self.timestamp = timestamp
        self.nome_transazione = nome_transazione
        self.dettagli_transazione = dettagli_transazione
        self.hash_precedente = hash_precedente
        self.hash_corrente = self.calcola_hash()

    def calcola_hash(self):
        import hashlib
        stringa_blocco = f"{self.indice}{self.timestamp}{self.nome_transazione}{self.dettagli_transazione}{self.hash_precedente}"
        return hashlib.sha256(stringa_blocco.encode()).hexdigest()
import uuid
from typing import Dict
from storages import SQLite

DB = "helpdesk_manager.db"
CREATE_TABLE = """
            CREATE TABLE IF NOT EXISTS ordens (
                id TEXT PRIMARY KEY,
                cliente TEXT,
                problema TEXT,
                solucao TEXT,
                valor REAL,
                servico_realizado TEXT
            )
        """
TIKET = """INSERT INTO ordens VALUES (?, ?, ?, ?, ?, ?)"""
SELECT_ORDER = """SELECT * FROM ordens WHERE id = ?"""
        
        
class Tiket:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.db = SQLite(self.db_path)
        self.conn = self.db.connect()
        self.cursor = self.db.cursor(self.conn)
        
    def create_table(self, query):
        self.conn.execute(query)
        return
    
    def criate_tiket(self, cliente: Dict, problema: str, solucao: str, valor: float, servico_realizado: str):
        id = str(uuid.uuid4())
        self.cursor.execute(TIKET, (id, str(cliente), problema, solucao, valor, servico_realizado))
        self.conn.commit()
        return id

    def compartilhar(self, id: str, metodo: str):
        self.db.execute(SELECT_ORDER, (id,))
        ordem = self.db.fetchone()
        if not ordem:
            print("Ordem de serviço não encontrada")
            return

        if metodo.lower() == 'whatsapp':
            # Adicione aqui o código para compartilhar via WhatsApp
            pass
        elif metodo.lower() == 'email':
            # Adicione aqui o código para compartilhar via Email
            pass
        else:
            print("Método de compartilhamento não suportado")

    def imprimir(self, id: str):
        self.cursor.execute(SELECT_ORDER, (id,))
        ordem = self.db.fetchone()
        if not ordem:
            print("Ordem de serviço não encontrada")
            return

        # Adicione aqui o código para imprimir a ordem de serviço
        pass

# Exemplo de uso
tiket = Tiket(DB)
client = {
    "nome": "Nome do Cliente",
    "endereco": "Endereço do Cliente",
    "telefone": "Telefone do Cliente",
    "whatsapp": "WhatsApp do Cliente",
    "foto_do_equipamento": "Foto do Equipamento"
}


def main():
    create_tables = tiket.create_table(CREATE_TABLE)
    id = tiket.criate_tiket(client, "Problema Informado", "Solução", 100.0, "Serviço Realizado")
    print(id)  # Imprime o ID único da ordem de serviço


if __name__ == '__main__': # permite a execução deste módulo como script
    main()
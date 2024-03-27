import uuid
import sqlite3
from typing import Dict

class OrdemDeServico:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS ordens (
                id TEXT PRIMARY KEY,
                cliente TEXT,
                problema TEXT,
                solucao TEXT,
                valor REAL,
                servico_realizado TEXT
            )
        """)

    def criar_ordem(self, cliente: Dict, problema: str, solucao: str, valor: float, servico_realizado: str):
        id = str(uuid.uuid4())
        self.cursor.execute("""
            INSERT INTO ordens VALUES (?, ?, ?, ?, ?, ?)
        """, (id, str(cliente), problema, solucao, valor, servico_realizado))
        self.conn.commit()
        return id

    def compartilhar(self, id: str, metodo: str):
        self.cursor.execute("SELECT * FROM ordens WHERE id = ?", (id,))
        ordem = self.cursor.fetchone()
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
        self.cursor.execute("SELECT * FROM ordens WHERE id = ?", (id,))
        ordem = self.cursor.fetchone()
        if not ordem:
            print("Ordem de serviço não encontrada")
            return

        # Adicione aqui o código para imprimir a ordem de serviço
        pass

# Exemplo de uso
ordem = OrdemDeServico(":memory:")
cliente = {
    "nome": "Nome do Cliente",
    "endereco": "Endereço do Cliente",
    "telefone": "Telefone do Cliente",
    "whatsapp": "WhatsApp do Cliente",
    "foto_do_equipamento": "Foto do Equipamento"
}
id = ordem.criar_ordem(cliente, "Problema Informado", "Solução", 100.0, "Serviço Realizado")
print(id)  # Imprime o ID único da ordem de serviço
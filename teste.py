import sqlite3

banco = sqlite3.connect('banco_cadastro.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, senha text)")
cursor.execute("INSERT INTO cadastro VALUES ('teste', 'testando')")

banco.commit()
banco.close()
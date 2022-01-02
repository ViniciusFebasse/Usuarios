import sys
import sqlite3
from PyQt6 import uic, QtWidgets

banco = sqlite3.connect('banco_cadastro.db')
cursor = banco.cursor()

def logando():

    nome = primeira_tela.login_input_usuario.text()
    senha = primeira_tela.login_input_senha.text()
    print(nome, senha)

    try:
        cursor.execute("SELECT senha FROM cadastro WHERE nome = '" + nome + "'")
        senha_bd = cursor.fetchall()[0][0]
        print(senha_bd)
        if senha == senha_bd:
            primeira_tela.login_label_acesso.setText("Acesso liberado! Vá para a página Sistema!")
            primeira_tela.sistema.setEnabled(True)

        else:
            primeira_tela.login_label_acesso.setText("Acesso Negado. Dados incorretos!")

    except:
        primeira_tela.login_label_acesso.setText("Acesso Negado. Dados incorretos!")

def cadastrando():
    nome = primeira_tela.login_input_usuario.text()
    senha = primeira_tela.login_input_senha.text()

    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, senha text)")
    cursor.execute("INSERT INTO cadastro VALUES ('" + nome + "', '" + senha + "')")

    banco.commit()
    banco.close()
    primeira_tela.login_label_acesso.setText("Usuário cadastrado com sucesso!")

def bloquear():
    primeira_tela.sistema.setEnabled(False)
    primeira_tela.login_label_acesso.setText("")


# Execução do aplicativo
app = QtWidgets.QApplication([])

# Definição das telas
primeira_tela = uic.loadUi("template.ui")

# Definição do relacionamento de botões e funções
primeira_tela.login_btn_entrar.clicked.connect(logando)
primeira_tela.sistema_btn_bloquear.clicked.connect(bloquear)
primeira_tela.login_btn_cadastrar.clicked.connect(cadastrando)

primeira_tela.show()
app.exec()
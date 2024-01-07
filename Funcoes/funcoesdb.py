import sqlite3

def adicionar_cliente(nome, senha, email, cep, cpf, telefone, data, endereco):
    farmacia = sqlite3.connect('farmacia_dados.db')

    cursor = farmacia.cursor()

    cursor.execute("CREATE TABLE cliente (cli_nome text, cli_senha text, cli_email text, cli_cep text, cli_cpf text, cli_telefone text, cli_data text, cli_endereco text)")
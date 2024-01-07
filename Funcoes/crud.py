import sqlite3

farmacia = sqlite3.connect('farmacia_dados.db')

cursor = farmacia.cursor()

"""

cursor.execute("CREATE TABLE cliente (cli_nome text, cli_senha text, cli_email text, cli_cep text, cli_cpf text, cli_telefone text, cli_data text, cli_endereco text)")





cursor.execute("CREATE TABLE remedio (rem_nome text, rem_empresa text, rem_lote text, rem_tipo text, rem_preco real, rem_marca text)") 

"""

cursor.execute("INSERT INTO empresa (emp_nome, emp_senha, emp_email, emp_cnpj) VALUES ('Admin', '123123', 'Admin@gmail.com', '0')")

farmacia.commit()
import sqlite3

farmacia = sqlite3.connect('farmacia_dados.db')

cursor = farmacia.cursor()

"""

cursor.execute("CREATE TABLE cliente (cli_nome text, cli_senha text, cli_email text, cli_cep text, cli_cpf text, cli_telefone text, cli_data text, cli_endereco text)")

cursor.execute("CREATE TABLE empresa (emp_nome text, emp_senha text, emp_email text, emp_cnpj)")

cursor.execute("CREATE TABLE vendedor (ven_nome text, ven_senha text, ven_empresa text, ven_cpf text, ven_email text, ven_cep text, ven_telefone text, ven_data text, ven_endereco text)")

cursor.execute("CREATE TABLE remedio (rem_nome text, rem_empresa text, rem_lote text, rem_tipo text, rem_preco real, rem_marca text)") 

"""

cursor.execute("INSERT INTO empresa (emp_nome, emp_senha, emp_email, emp_cnpj) VALUES ('Admin', '123123', 'Admin@gmail.com', '0')")

farmacia.commit()
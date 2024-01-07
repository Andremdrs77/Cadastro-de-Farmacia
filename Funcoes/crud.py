import sqlite3


def adicionar_cliente(nome, senha, email, cep, cpf, telefone, data, endereco):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
                            cli_nome text,
                            cli_senha text,
                            cli_email text,
                            cli_cep text,
                            cli_cpf text,
                            cli_telefone text,
                            cli_data text,
                            cli_endereco text
                         )''')

        cursor.execute('INSERT INTO cliente (cli_nome, cli_senha, cli_email, cli_cep, cli_cpf, cli_telefone, cli_data, cli_endereco) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (nome, senha, email, cep, cpf, telefone, data, endereco))

        farmacia.commit()

    except sqlite3.Error as e:
        print(f"Erro ao adicionar cliente: {e}")
    finally:
        cursor.close()
        farmacia.close()


def criarEmpresa(nome, senha, cnpj, email):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS empresa (
                            emp_nome TEXT,
                            emp_senha TEXT,
                            emp_email TEXT,
                            emp_cnpj TEXT
                         )''')

        cursor.execute('INSERT INTO empresa (emp_nome, emp_senha, emp_email, emp_cnpj) VALUES (?, ?, ?, ?)', (nome, senha, email, cnpj))

        farmacia.commit()
        print("Empresa criada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar empresa: {e}")
    finally:
        cursor.close()
        farmacia.close()


def criarRemedio(nome, empresa, lote, tipo, preco, marca):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS remedio (
                            rem_nome TEXT,
                            rem_empresa TEXT,
                            rem_lote TEXT,
                            rem_tipo TEXT,
                            rem_preco REAL,
                            rem_marca TEXT
                         )''')

        cursor.execute('INSERT INTO remedio (rem_nome, rem_empresa, rem_lote, rem_tipo, rem_preco, rem_marca) VALUES (?, ?, ?, ?, ?, ?)', (nome, empresa, lote, tipo, preco, marca))

        farmacia.commit()
        print("Remédio adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar remédio: {e}")
    finally:
        cursor.close()
        farmacia.close()


def criarVendedor(nome, senha, empresa, cpf, email, cep, telefone, data, endereco):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS vendedor (
                            ven_nome TEXT,
                            ven_senha TEXT,
                            ven_empresa TEXT,
                            ven_cpf TEXT,
                            ven_email TEXT,
                            ven_cep TEXT,
                            ven_telefone TEXT,
                            ven_data TEXT,
                            ven_endereco TEXT
                         )''')

        cursor.execute('INSERT INTO vendedor (ven_nome, ven_senha, ven_empresa, ven_cpf, ven_email, ven_cep, ven_telefone, ven_data, ven_endereco) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (nome, senha, empresa, cpf, email, cep, telefone, data, endereco))

        farmacia.commit()
        print("Vendedor adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar vendedor: {e}")
    finally:
        cursor.close()
        farmacia.close()


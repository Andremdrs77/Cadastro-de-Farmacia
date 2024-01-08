import sqlite3
import pickle

def criarCliente(nome, senha, email, cep, cpf, telefone, data, endereco, cnpj):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
                            cli_nome TEXT,
                            cli_senha TEXT,
                            cli_email TEXT,
                            cli_cep TEXT,
                            cli_cpf TEXT,
                            cli_telefone TEXT,
                            cli_data TEXT,
                            cli_endereco TEXT,
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


def criarVendedor(nome, senha, empresa, cpf, email, cep, telefone, data, endereco, cnpj):
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
                            ven_endereco TEXT,
                         )''')

        cursor.execute('INSERT INTO vendedor (ven_nome, ven_senha, ven_empresa, ven_cpf, ven_email, ven_cep, ven_telefone, ven_data, ven_endereco) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (nome, senha, empresa, cpf, email, cep, telefone, data, endereco, cnpj))

        farmacia.commit()
        print("Vendedor adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar vendedor: {e}")
    finally:
        cursor.close()
        farmacia.close()

def deletarCliente(cpf):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''DELETE FROM cliente WHERE cli_cpf = ?''', (cpf,))

        farmacia.commit()

    except sqlite3.Error as e:
        print(f"Erro ao remover cliente: {e}")
    finally:
        cursor.close()
        farmacia.close()

def deletarVendedor(cpf):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''DELETE FROM vendedor WHERE ven_cpf = ?''', (cpf,))

        farmacia.commit()

    except sqlite3.Error as e:
        print(f"Erro ao remover vendedor: {e}")
    finally:
        cursor.close()
        farmacia.close()

def deletarRemedio(lote):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''DELETE FROM remedio WHERE rem_lote = ?''', (lote,))

        farmacia.commit()

    except sqlite3.Error as e:
        print(f"Erro ao remover remédio: {e}")
    finally:
        cursor.close()
        farmacia.close()

def mostrarVendedores():
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''SELECT ven_nome FROM vendedor''')

        vendedores = [row[0] for row in cursor.fetchall()]

        print('Nomes dos Vendedores:')
        for nome in vendedores:
            print(nome)

        print(vendedores)

    except sqlite3.Error as e:
        print(f"Erro ao mostrar vendedores: {e}")
    finally:
        cursor.close()
        farmacia.close()

def mostrarPrecos():
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''SELECT rem_nome, rem_preco FROM remedio''')

        dados_remedios = {row[0]: row[1] for row in cursor.fetchall()}

        print('Dicionário de Preços dos Medicamentos:')
        nomes = list(dados_remedios.keys())
        precos = list(dados_remedios.values())

        i = 0
        while i < len(nomes):
            print(f"{nomes[i]}: {precos[i]}")
            i += 1

    except sqlite3.Error as e:
        print(f"Erro ao mostrar preços: {e}")
    finally:
        cursor.close()
        farmacia.close()

def fazerBackup(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(dados, arquivo)
        print(f"Backup dos dados realizado com sucesso no arquivo: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao fazer backup dos dados: {str(e)}")

def restaurarBackup(nome_arquivo):
    try:
        with open(nome_arquivo, 'rb') as arquivo:
            dados_restaurados = pickle.load(arquivo)
        print(f"Dados restaurados com sucesso do arquivo: {nome_arquivo}")
        return dados_restaurados
    except FileNotFoundError:
        print(f"Arquivo de backup não encontrado: {nome_arquivo}")
        return None
    except Exception as e:
        print(f"Erro ao restaurar dados do backup: {str(e)}")
        return None

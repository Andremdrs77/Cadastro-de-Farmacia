import sqlite3
import pickle

def criarCliente(nome, senha, email, cep, cpf, telefone, data, endereco):
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
                            cli_endereco TEXT
                         )''')

        cursor.execute('INSERT INTO cliente (cli_nome, cli_senha, cli_email, cli_cep, cli_cpf, cli_telefone, cli_data, cli_endereco) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (nome, senha, email, cep, cpf, telefone, data, endereco))

        farmacia.commit()

    except sqlite3.Error as e:
        print(f"Erro ao adicionar cliente: {e}")
    finally:
        cursor.close()
        farmacia.close()
    

def criarEmpresa(nome, senha, cnpj, email, cep):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS empresa (
                            emp_nome TEXT,
                            emp_senha TEXT,
                            emp_email TEXT,
                            emp_cnpj TEXT,
                            emp_cep TEXT
                         )''')

        cursor.execute('INSERT INTO empresa (emp_nome, emp_senha, emp_email, emp_cnpj, emp_cep) VALUES (?, ?, ?, ?, ?)', (nome, senha, email, cnpj, cep))

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
        mostrarPrecos()


def criarVendedor(nome, senha, empresa, cpf, email, cep):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS vendedor (
                            ven_nome TEXT,
                            ven_senha TEXT,
                            ven_empresa TEXT,
                            ven_cpf TEXT,
                            ven_email TEXT,
                            ven_cep TEXT
                         )''')

        cursor.execute('INSERT INTO vendedor (ven_nome, ven_senha, ven_empresa, ven_cpf, ven_email, ven_cep) VALUES (?, ?, ?, ?, ?, ?)', (nome, senha, empresa, cpf, email, cep))

        farmacia.commit()
        print("Vendedor adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar vendedor: {e}")
    finally:
        cursor.close()
        farmacia.close()
        mostrarVendedores()


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

def mostrarInformacoesVendedor(cpf):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''SELECT * FROM vendedor WHERE ven_cpf = ?''', (cpf,))
        vendedor = cursor.fetchone()

        if not vendedor:
            print(f"Nenhum vendedor encontrado com o CPF {cpf}.")
            return

        return [vendedor[0],vendedor[1],vendedor[2],vendedor[3],vendedor[4],vendedor[5]]
        # print("Nome:", vendedor[0])
        # print("Senha:", vendedor[1])
        # print("Empresa:", vendedor[2])
        # print("CPF:", vendedor[3])
        # print("Email:", vendedor[4])
        # print("CEP:", vendedor[5])

    except sqlite3.Error as e:
        print(f"Erro ao mostrar informações do vendedor: {e}")
    finally:
        cursor.close()
        farmacia.close()

def mostrarInformacoesCliente(cpf):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''SELECT * FROM cliente WHERE cli_cpf = ?''', (cpf,))
        cliente = cursor.fetchone()

        if not cliente:
            print(f"Nenhum cliente encontrado com o CPF {cpf}.")
            return

        return [cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], cliente[7]]
        # print("Nome:", cliente[0])
        # print("Senha:", cliente[1])
        # print("Email:", cliente[2])
        # print("CEP:", cliente[3])
        # print("CPF:", cliente[4])
        # print("Telefone:", cliente[5])
        # print("Data:", cliente[6])
        # print("Endereço:", cliente[7])

    except sqlite3.Error as e:
        print(f"Erro ao mostrar informações do cliente: {e}")
    finally:
        cursor.close()
        farmacia.close()

def mostrarInformacoesRemedio(lote):
    try:
        farmacia = sqlite3.connect('farmacia_dados.db')
        cursor = farmacia.cursor()

        cursor.execute('''SELECT * FROM remedio WHERE rem_lote = ?''', (lote,))
        remedio = cursor.fetchone()

        if not remedio:
            print(f"Nenhum remédio encontrado com o lote {lote}.")
            return

        return [remedio[0], remedio[1], remedio[2], remedio[3], remedio[4], remedio[5]]
        # print("Nome:", remedio[0])
        # print("Empresa:", remedio[1])
        # print("Lote:", remedio[2])
        # print("Tipo:", remedio[3])
        # print("Preço:", remedio[4])
        # print("Marca:", remedio[5])

    except sqlite3.Error as e:
        print(f"Erro ao mostrar informações do remédio: {e}")
    finally:
        cursor.close()
        farmacia.close()

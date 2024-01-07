from sqlite3 import *
from Telas .Login .login import *
from Telas .Menu .menu import *
from Telas .DadosVendedor .dados_vendedor import *
from Telas .DadosRemedio .dados_remedio import *
from Telas .DadosEmpresa .dados_empresa import *
from Telas .DadosCliente .dados_cliente import *
from Telas .Login .login import *
from Telas .CriarConta .criar_conta import *
from Telas .CadastroVendedor .cadastrar_vendedor import *
from Telas .CadastroRemedio .cadastrar_remedio import *
from Telas .CadastroCliente . cadastrar_cliente import *
from Funcoes .funcoesdb import *

try:
    farmacia = sqlite3.connect('farmacia_dados.db')
    cursor = farmacia.cursor()
    cursor.execute('INSERT INTO empresa (emp_nome, emp_senha, emp_email, emp_cnpj) VALUES (?, ?, ?, ?)', ('admin', '123123', 'admin@gmail.com', '0'))
except:
    print('Admin já existe.')
finally:
    farmacia.close()
    cursor.close()

class App:
    def __init__(self):


aplicacao = App()
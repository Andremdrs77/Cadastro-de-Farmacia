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
from Funcoes .crud import *

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
        self.tela = TelaLogin()
        self.cnpj = None
        self.nomeEmpresa = ""

        self.tela.button_1.configure(command=lambda: self.infoTelas(tela="", cnpj=self.tela.entry_1.get()))


    def infoTelas(self, tela, cnpj):
        if tela == TelaMenu():
            self.Tela.nomeEmpresa() = ""
aplicacao = App()
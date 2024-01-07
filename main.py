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



class App:
    def __init__(self):
        self.tela = TelaLogin()
        self.cnpj = None
        self.nomeEmpresa = ""

        self.tela.button_1.configure(command=lambda: self.infoTelas(tela="Menu", cnpj=self.tela.entry_1.get()))
        self.tela.button_2.configure(command=lambda: self.infoTelas(tela="criarConta"))

    def infoTelas(self, tela, cnpj):
        if tela == "Menu":
            self.tela = TelaMenu(cnpj)
            nome_empresa = self.GetNomeEmpresa(cnpj)
            self.tela.nomeEmpresa = nome_empresa

        elif tela == "":
            pass
        


    def GetNomeEmpresa(self, cnpj):
        try:
            farmacia = sqlite3.connect('farmacia_dados.db')
            cursor = farmacia.cursor()
            cursor.execute('SELECT emp_nome FROM empresa WHERE emp_cnpj = ?', (cnpj,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return "Empresa não encontrada"
        except Exception as e:
            print(f"Erro ao obter nome da empresa: {e}")
        finally:
            cursor.close()
            farmacia.close()


    def login(self):
        self.tela.window.destroy()
        
        self.tela = TelaLogin()
        self.cnpj = None
        self.nomeEmpresa = ""

        self.tela.button_1.configure(command=lambda: self.infoTelas(tela="Menu", cnpj=self.tela.entry_1.get()))


    def menu(self, cnpj):
        self.tela.window.destroy()


    def criarConta(self):
        self.tela.window.destroy()


    def cadastrarVendedor(self):
        self.tela.window.destroy()


    def cadastrarCliente(self):
        self.tela.window.destroy()


    def cadastrarRemedio(self):
        self.tela.window.destroy()


    def dadosEmpresa(self):
        self.tela.window.destroy()


    def dadosCliente(self):
        self.tela.window.destroy()


    def dadosVendedor(self):
        self.tela.window.destroy()


    def dadosRemedio(self):
        self.tela.window.destroy()
aplicacao = App()
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

        self.tela.button_1.configure(command=lambda: self.infoTelas(tela="Menu", cnpj=self.tela.entry_1.get()))
        self.tela.button_2.configure(command=lambda: self.infoTelas(tela="criarConta"))

        self.tela.window.mainloop()

    def infoTelas(self, tela, cnpj):
        if tela == "Menu":
            self.tela = self.menu(cnpj)
            nome_empresa = self.GetNomeEmpresa(cnpj)
            self.tela.nomeEmpresa = nome_empresa

        elif tela == "":
            pass

        


    def GetNomeEmpresa(self, cnpj):
        try:
            with sqlite3.connect('farmacia_dados.db') as farmacia:
                cursor = farmacia.cursor()
                cursor.execute('SELECT emp_nome FROM empresa WHERE emp_cnpj = ?', (cnpj,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return "Empresa não encontrada"
        except Exception as e:
            print(f"Erro ao obter nome da empresa: {e}")


    def login(self):
        self.tela.window.destroy()
        
        self.tela = TelaLogin()
        self.cnpj = None

        self.tela.button_1.configure(command=lambda: self.infoTelas(tela="Menu", cnpj=self.tela.entry_1.get()))


    def menu(self, cnpj):
        self.tela.window.destroy()

        self.tela = TelaMenu()

    def criarConta(self):
        self.tela.window.destroy()


    def cadastrarVendedor(self, cnpj):
        self.tela.window.destroy()


    def cadastrarCliente(self, cnpj):
        self.tela.window.destroy()


    def cadastrarRemedio(self, cnpj):
        self.tela.window.destroy()


    def dadosEmpresa(self, cnpj):
        self.tela.window.destroy()


    def dadosCliente(self, cnpj):
        self.tela.window.destroy()


    def dadosVendedor(self, cnpj):
        self.tela.window.destroy()


    def dadosRemedio(self, cnpj):
        self.tela.window.destroy()

aplicacao = App()
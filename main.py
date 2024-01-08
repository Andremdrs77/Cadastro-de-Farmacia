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
        self.janela = TelaLogin()
        self.cnpj = None

        self.janela.button_1.configure(command=lambda: self.infoTelas(tela="Menu", cnpj=self.janela.entry_1.get()))
        self.janela.button_2.configure(command=lambda: self.infoTelas(tela="criarConta"))

        self.janela.window.mainloop()
        

    def infoTelas(self, tela, cnpj):
        if tela == "Menu":
            self.janela = self.menu(cnpj)
            nome_empresa = self.GetNomeEmpresa(cnpj)
            self.janela.nomeEmpresa = nome_empresa

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
        self.janela.window.destroy()
        
        self.janela = TelaLogin()
        self.cnpj = None

        self.janela.button_1.configure(command=lambda: self.infoTelas(tela="Menu", cnpj=self.janela.entry_1.get()))


    def menu(self, cnpj):
        self.janela.window.destroy()

        self.janela = TelaMenu()


    def criarConta(self):
        self.janela.window.destroy()


    def cadastrarVendedor(self, cnpj):
        self.janela.window.destroy()


    def cadastrarCliente(self, cnpj):
        self.janela.window.destroy()


    def cadastrarRemedio(self, cnpj):
        self.janela.window.destroy()


    def dadosEmpresa(self, cnpj):
        self.janela.window.destroy()


    def dadosCliente(self, cnpj):
        self.janela.window.destroy()


    def dadosVendedor(self, cnpj):
        self.janela.window.destroy()


    def dadosRemedio(self, cnpj):
        self.janela.window.destroy()

aplicacao = App()
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
        self.janela.button_2.configure(command=lambda: self.infoTelas(tela="CriarConta", cnpj=''))

        self.janela.window.mainloop()
        

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


    def infoTelas(self, tela, cnpj):
        self.cnpj = cnpj

        if tela == "Login":
            self.janela = self.login()

        elif tela == "Menu":
            nome_empresa = self.GetNomeEmpresa(cnpj)
            self.janela = self.menu(nome_empresa)

        elif tela == "CriarConta":
            self.janela = self.criarConta()



    def login(self):
        self.janela.window.destroy()
        
        self.janela = TelaLogin()
        self.cnpj = None

        self.janela.button_1.configure(command=lambda: self.infoTelas(tela="Menu", cnpj=self.janela.entry_1.get()))


    def menu(self, nome_empresa):
        self.janela.window.destroy()

        self.janela = TelaMenu()
        self.janela.button_1['command'] = lambda: self.infoTelas(tela="CadastrarVendedor", cnpj=self.cnpj)
        self.janela.button_2['command'] = lambda: self.infoTelas(tela="ConsultarVendedores", cnpj=self.cnpj)
        self.janela.button_3['command'] = lambda: self.infoTelas(tela="CadastrarCliente", cnpj=self.cnpj)
        self.janela.button_4['command'] = lambda: self.infoTelas(tela="ConsultarClientes", cnpj=self.cnpj)
        self.janela.button_5['command'] = lambda: self.infoTelas(tela="CadastrarRemedio", cnpj=self.cnpj)
        self.janela.button_6['command'] = lambda: self.infoTelas(tela="ConsultarRemedios", cnpj=self.cnpj)
        self.janela.button_7['command'] = lambda: self.infoTelas(tela="Login", cnpj=self.cnpj)
        self.textoEmpresa.configure(text = nome_empresa)

    def criarConta(self):
        self.janela.window.destroy()

        self.janela = TelaCriarConta()


    def cadastrarVendedor(self, cnpj):
        self.janela.window.destroy()

        self.janela = TelaCadastrarVendedor


    def cadastrarCliente(self, cnpj):
        self.janela.window.destroy()

        self.janela = TelaCadastrarCliente()


    def cadastrarRemedio(self, cnpj):
        self.janela.window.destroy()

        self.janela = TelaCadastrarRemedio()


    def dadosEmpresa(self, cnpj):
        self.janela.window.destroy()

        self.janela = TelaDadosEmpresa()


    def dadosCliente(self):
        self.janela.window.destroy()

        self.janela = TelaDadosCliente()


    def dadosVendedor(self):
        self.janela.window.destroy()

        self.janela = TelaDadosVendedor()


    def dadosRemedio(self):
        self.janela.window.destroy()

        self.janela = TelaDadosRemedio()


aplicacao = App()
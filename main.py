from sqlite3 import *

from Telas .Login .login import *
from Telas .Menu .menu import *
from Telas .DadosVendedor .dados_vendedor import *
from Telas .DadosRemedio .dados_remedio import *
# from Telas .DadosEmpresa .dados_empresa import *
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

        self.janela.button_1.configure(command=lambda: self.menu(cnpj=self.janela.entry_1.get(), nome_empresa=''))
        self.janela.button_2.configure(command=lambda: self.criarConta())

        self.janela.window.mainloop()
        

    def GetNomeEmpresa(self, cnpj):
        print(cnpj)
        # try:
        #     with sqlite3.connect('farmacia_dados.db') as farmacia:
        #         cursor = farmacia.cursor()
        #         cursor.execute('SELECT emp_nome FROM empresa WHERE emp_cnpj = ?', (cnpj,))
        #         result = cursor.fetchone()
        #         if result:
        #             return result[0]
        #         else:
        #             return "Empresa não encontrada"
        # except Exception as e:
        #     print(f"Erro ao obter nome da empresa: {e}")

    def login(self):
        self.janela.window.destroy()
        
        self.janela = TelaLogin()
        self.cnpj = None

        self.janela.button_1.configure(command=lambda: self.menu(cnpj=self.janela.entry_1.get(), nome_empresa=''))


    def menu(self, cnpj, nome_empresa):
        nome_empresa = self.GetNomeEmpresa(cnpj)
        if isinstance(self.janela, TelaMenu):
            self.janela.button_1['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_2['command'] = lambda: self.dadosVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarCliente()
            self.janela.button_4['command'] = lambda: self.dadosCliente()
            self.janela.button_5['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_6['command'] = lambda: self.dadosRemedio()
            self.janela.button_7['command'] = lambda: self.login()
        else:
            self.janela.window.destroy()
            self.janela = TelaMenu()
            self.janela.button_1['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_2['command'] = lambda: self.dadosVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarCliente()
            self.janela.button_4['command'] = lambda: self.dadosCliente()
            self.janela.button_5['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_6['command'] = lambda: self.dadosRemedio()
            self.janela.button_7['command'] = lambda: self.login()

        self.janela.window.mainloop()


    def criarConta(self):
        self.janela.window.destroy()

        self.janela = TelaCriarConta()


    def cadastrarVendedor(self):
        self.janela.window.destroy()

        self.janela = TelaCadastrarVendedor()


    def cadastrarCliente(self):
        self.janela.window.destroy()

        self.janela = TelaCadastrarCliente()


    def cadastrarRemedio(self):
        self.janela.window.destroy()

        self.janela = TelaCadastrarRemedio()


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
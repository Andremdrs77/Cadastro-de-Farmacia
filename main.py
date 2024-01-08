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
        self.cnpj_conta = None

        self.janela.button_1['command'] = lambda: self.menu(cnpj=self.janela.entry_1.get(), nome_empresa='')
        self.janela.button_2['command'] = lambda: self.criarConta()

        self.janela.window.mainloop()
        

    def GetNomeEmpresa(self, cnpj):
        print(cnpj)
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
        if isinstance(self.login, TelaLogin):
            self.janela.button_1['command'] = lambda: self.menu(cnpj=self.janela.entry_1.get(), nome_empresa='')
            self.janela.button_2['command'] = lambda: self.criarConta()
        else:
            self.janela.window.destroy()
            self.janela = TelaLogin()
            self.janela.button_1['command'] = lambda: self.menu(cnpj=self.janela.entry_1.get(), nome_empresa='')
            self.janela.button_2['command'] = lambda: self.criarConta()


    def menu(self, cnpj, nome_empresa):
        self.cnpj = cnpj
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


    def criarConta(self):
        if isinstance(self.janela, TelaCriarConta):
            self.janela.button_1['command'] = lambda: self.login()
            self.janela.button_2['command'] = lambda: self.menu(cnpj='', nome_empresa='')
        else:
            self.janela.window.destroy()
            self.janela = TelaCriarConta()
            self.janela.button_1['command'] = lambda: self.login()
            self.janela.button_2['command'] = lambda: self.menu(cnpj='', nome_empresa='')



    def cadastrarVendedor(self):
        if isinstance(self.janela, TelaCadastrarVendedor):
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: self.dadosVendedor()
            self.janela.button_5['command'] = lambda: self.menu(cnpj='', nome_empresa='')
        else:
            self.janela.window.destroy()
            self.janela = TelaCadastrarVendedor()
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: self.dadosVendedor()
            self.janela.button_5['command'] = lambda: self.menu(cnpj='', nome_empresa='')


    def cadastrarCliente(self):
        if isinstance(self.janela, TelaCadastrarCliente):
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: self.ciarCliente(nome=self.janela.entry_1.get(),
                                                                        cpf=self.janela.entry_2.get(),
                                                                        cep=self.janela.entry_3.get(),
                                                                        email=self.janela.entry_4.get(),
                                                                        telefone=self.janela.entry_5.get(),
                                                                        data=self.janela.entry_6.get(),
                                                                        endereco=self.janela.entry_7.get(),
                                                                        senha=self.janela.entry_8.get(),
                                                                        cnpj=self.cnpj())
            self.janela.button_5['command'] = lambda: self.menu(cnpj='', nome_empresa='')
        else:
            self.janela.window.destroy()
            self.janela = TelaCadastrarCliente()
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: self.criarCliente(nome=self.janela.entry_1.get(),
                                                                        cpf=self.janela.entry_2.get(),
                                                                        cep=self.janela.entry_3.get(),
                                                                        email=self.janela.entry_4.get(),
                                                                        telefone=self.janela.entry_5.get(),
                                                                        data=self.janela.entry_6.get(),
                                                                        endereco=self.janela.entry_7.get(),
                                                                        senha=self.janela.entry_8.get(),
                                                                        cnpj=self.cnpj())
            self.janela.button_5['command'] = lambda: self.menu(cnpj='', nome_empresa='')


    def cadastrarRemedio(self):
        if isinstance(self.janela, TelaCadastrarRemedio):
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: self.dadosRemedio()
            self.janela.button_5['command'] = lambda: self.menu(cnpj='', nome_empresa='')
        else:
            self.janela.window.destroy()
            self.janela = TelaCadastrarRemedio()
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: self.dadosRemedio()
            self.janela.button_5['command'] = lambda: self.menu(cnpj='', nome_empresa='')


    def dadosCliente(self):
        if isinstance(self.janela, TelaDadosCliente):
            self.janela.button_1['command'] = lambda: self.menu(cnpj='', nome_empresa='')
        else:
            self.janela.window.destroy()
            self.janela = TelaDadosCliente()
            self.janela.button_1['command'] = lambda: self.menu(cnpj='', nome_empresa='')


    def dadosVendedor(self):
        if isinstance(self.janela, TelaDadosVendedor):
            self.janela.button_2['command'] = lambda: self.menu(cnpj='', nome_empresa='')
        else:
            self.janela.window.destroy()
            self.janela = TelaDadosVendedor()
            self.janela.button_2['command'] = lambda: self.menu(cnpj='', nome_empresa='')


    def dadosRemedio(self):
        if isinstance(self.janela, TelaDadosRemedio):
            self.janela.button_2['command'] = lambda: self.menu(cnpj='', nome_empresa='')
        else:
            self.janela.window.destroy()
            self.janela = TelaDadosRemedio()
            self.janela.button_2['command'] = lambda: self.menu(cnpj='', nome_empresa='')

aplicacao = App()
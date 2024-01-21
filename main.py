from sqlite3 import *

from Telas .Login .login import *
from Telas .Menu .menu import *
from Telas .DadosVendedor .dados_vendedor import *
from Telas .DadosRemedio .dados_remedio import *
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

        def Logar():
            cnpj = self.janela.entry_1.get()
            senha = self.janela.entry_2.get()
            verificarEmpresa = verificarEmpresaSenha(cnpj, senha)
            if verificarEmpresa:
                self.cnpj_conta = cnpj
                self.menu(cnpj=cnpj, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))

        self.janela.button_1['command'] = lambda: Logar()
        self.janela.button_2['command'] = lambda: self.criarConta()

        self.janela.window.mainloop()
        

    def GetNomeEmpresa(self, cnpj):
        try:
            with sqlite3.connect('farmacia_dados.db') as farmacia:
                cursor = farmacia.cursor()
                cursor.execute('SELECT emp_nome FROM empresa WHERE emp_cnpj = ?', (cnpj,))
                result = cursor.fetchone()
                if result:
                    return str(result[0])
                else:
                    return "Empresa não encontrada"
        except Exception as e:
            print(f"Erro ao obter nome da empresa: {e}")


    def login(self):
        def Logar():
            cnpj = self.janela.entry_1.get()
            senha = self.janela.entry_2.get()
            verificarEmpresa = verificarEmpresaSenha(cnpj, senha)
            if verificarEmpresa:
                self.cnpj_conta = cnpj
                self.menu(cnpj=cnpj, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))

        if isinstance(self.janela, TelaLogin):
            self.janela.button_1['command'] = Logar
            self.janela.button_2['command'] = self.criarConta
        else:
            self.janela.window.destroy()
            self.janela = TelaLogin()
            self.janela.button_1['command'] = Logar
            self.janela.button_2['command'] = self.criarConta


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
            self.janela.canvas.itemconfig(self.janela.textoEmpresa, text=f'Bem-vindo(a),\n{nome_empresa}!')
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
            self.janela.canvas.itemconfig(self.janela.textoEmpresa, text=f'Bem-vindo(a),\n{nome_empresa}!')

    def criarConta(self):
        if isinstance(self.janela, TelaCriarConta):
            self.janela.button_1['command'] = lambda: self.login()
            self.janela.button_2['command'] = lambda: criarEmpresa(email=self.janela.entry_2.get(),
                                                                        senha=self.janela.entry_3.get(),
                                                                        cnpj=self.janela.entry_4.get(),
                                                                        cep=self.janela.entry_5.get(),
                                                                        nome=self.janela.entry_6.get())
        else:
            self.janela.window.destroy()
            self.janela = TelaCriarConta()
            self.janela.button_1['command'] = lambda: self.login()
            self.janela.button_2['command'] = lambda: criarEmpresa(email=self.janela.entry_2.get(),
                                                                        senha=self.janela.entry_3.get(),
                                                                        cnpj=self.janela.entry_4.get(),
                                                                        cep=self.janela.entry_5.get(),
                                                                        nome=self.janela.entry_6.get())


    def cadastrarVendedor(self):
        if isinstance(self.janela, TelaCadastrarVendedor):
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: criarVendedor(nome=self.janela.entry_2.get(),
                                                                        cpf=self.janela.entry_3.get(),
                                                                        cep=self.janela.entry_4.get(),
                                                                        email=self.janela.entry_5.get(),
                                                                        senha=self.janela.entry_1.get(),
                                                                        empresa=self.GetNomeEmpresa(self.cnpj_conta))
            self.janela.button_5['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
        else:
            self.janela.window.destroy()
            self.janela = TelaCadastrarVendedor()
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: criarVendedor(nome=self.janela.entry_2.get(),
                                                                        cpf=self.janela.entry_3.get(),
                                                                        cep=self.janela.entry_4.get(),
                                                                        email=self.janela.entry_5.get(),
                                                                        senha=self.janela.entry_1.get(),
                                                                        empresa=self.GetNomeEmpresa(self.cnpj_conta))
            self.janela.button_5['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))


    def cadastrarCliente(self):
        if isinstance(self.janela, TelaCadastrarCliente):
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: criarCliente(nome=self.janela.entry_1.get(),
                                                                        cpf=self.janela.entry_2.get(),
                                                                        cep=self.janela.entry_5.get(),
                                                                        email=self.janela.entry_7.get(),
                                                                        telefone=self.janela.entry_3.get(),
                                                                        data=self.janela.entry_4.get(),
                                                                        endereco=self.janela.entry_6.get(),
                                                                        senha=self.janela.entry_8.get())
            self.janela.button_5['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
        else:
            self.janela.window.destroy()
            self.janela = TelaCadastrarCliente()
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_3['command'] = lambda: self.cadastrarRemedio()
            self.janela.button_4['command'] = lambda: criarCliente(nome=self.janela.entry_1.get(),
                                                                        cpf=self.janela.entry_2.get(),
                                                                        cep=self.janela.entry_5.get(),
                                                                        email=self.janela.entry_7.get(),
                                                                        telefone=self.janela.entry_3.get(),
                                                                        data=self.janela.entry_4.get(),
                                                                        endereco=self.janela.entry_6.get(),
                                                                        senha=self.janela.entry_8.get())
            self.janela.button_5['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))


    def cadastrarRemedio(self):
        if isinstance(self.janela, TelaCadastrarRemedio):
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_4['command'] = lambda: criarRemedio(empresa=self.janela.entry_1.get(),
                                                                        nome=self.janela.entry_2.get(),
                                                                        lote=self.janela.entry_3.get(),
                                                                        preco=self.janela.entry_4.get(),
                                                                        marca=self.janela.entry_5.get(),
                                                                        tipo=self.janela.entry_6.get())
            self.janela.button_3['command'] = lambda: self.dadosRemedio()
            self.janela.button_5['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
        else:
            self.janela.window.destroy()
            self.janela = TelaCadastrarRemedio()
            self.janela.button_1['command'] = lambda: self.cadastrarCliente()
            self.janela.button_2['command'] = lambda: self.cadastrarVendedor()
            self.janela.button_4['command'] = lambda: criarRemedio(empresa=self.janela.entry_1.get(),
                                                                        nome=self.janela.entry_2.get(),
                                                                        lote=self.janela.entry_3.get(),
                                                                        preco=self.janela.entry_4.get(),
                                                                        marca=self.janela.entry_5.get(),
                                                                        tipo=self.janela.entry_6.get())
            self.janela.button_3['command'] = lambda: self.dadosRemedio()
            self.janela.button_5['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))


    def dadosCliente(self):
        def MudarInfo():
            try:
                InfoCliente = mostrarInformacoesCliente(cpf=self.janela.entry_1.get())
                if InfoCliente:
                    self.janela.canvas.itemconfig(self.janela.nomeTxt, text=f"Nome: {InfoCliente[0]}")
                    self.janela.canvas.itemconfig(self.janela.senhaTxt, text=f"Senha: {InfoCliente[1]}")
                    self.janela.canvas.itemconfig(self.janela.emailTxt, text=f"Email: {InfoCliente[2]}")
                    self.janela.canvas.itemconfig(self.janela.cepTXT, text=f"CEP: {InfoCliente[3]}")
                    self.janela.canvas.itemconfig(self.janela.telefoneTxt, text=f"Telefone: {InfoCliente[5]}")
                    self.janela.canvas.itemconfig(self.janela.datanascimentoTxt, text=f"Data de nascimento: {InfoCliente[6]}")
                    self.janela.canvas.itemconfig(self.janela.enderecoTxt, text=f"Endereço: {InfoCliente[7]}")
                else:
                    self.janela.canvas.itemconfig(self.janela.nomeTxt, text="Nome: ")
                    self.janela.canvas.itemconfig(self.janela.senhaTxt, text="Senha: ")
                    self.janela.canvas.itemconfig(self.janela.emailTxt, text="Email: ")
                    self.janela.canvas.itemconfig(self.janela.cepTXT, text="CEP: ")
                    self.janela.canvas.itemconfig(self.janela.telefoneTxt, text="Telefone: ")
                    self.janela.canvas.itemconfig(self.janela.datanascimentoTxt, text="Data de nascimento: ")
                    self.janela.canvas.itemconfig(self.janela.enderecoTxt, text="Endereço: ")
            except Exception as e:
                print(f"Erro ao obter informações do cliente: {e}")

        if isinstance(self.janela, TelaDadosCliente):
            self.janela.button_1['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
            self.janela.button_3['command'] = lambda: deletarCliente(cpf=self.janela.entry_1.get())
            self.janela.button_2['command'] = lambda: MudarInfo()
        else: #Vascasjfhasfuoasgfiasufasyifasfasifhasfu
            self.janela.window.destroy()
            self.janela = TelaDadosCliente()
            self.janela.button_1['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
            self.janela.button_3['command'] = lambda: deletarCliente(cpf=self.janela.entry_1.get())
            self.janela.button_2['command'] = lambda: MudarInfo()


    def dadosVendedor(self):
        def MudarInfo():
            try:
                InfoVendedor = mostrarInformacoesVendedor(cpf=self.janela.entry_1.get())
                if InfoVendedor:
                    self.janela.canvas.itemconfig(self.janela.nomeTxt, text=f"Nome: {InfoVendedor[0]}")
                    self.janela.canvas.itemconfig(self.janela.senhaTxt, text=f"Senha: {InfoVendedor[1]}")
                    self.janela.canvas.itemconfig(self.janela.empresaTxt, text=f"Empresa: {InfoVendedor[2]}")
                    self.janela.canvas.itemconfig(self.janela.emailTxt, text=f"Email: {InfoVendedor[4]}")
                else:
                    self.janela.canvas.itemconfig(self.janela.nomeTxt, text="Nome: ")
                    self.janela.canvas.itemconfig(self.janela.senhaTxt, text="Senha: ")
                    self.janela.canvas.itemconfig(self.janela.empresaTxt, text="Empresa: ")
                    self.janela.canvas.itemconfig(self.janela.emailTxt, text="Email: ")
            except Exception as e:
                print(f"Erro ao obter informações do vendedor: {e}")

        if isinstance(self.janela, TelaDadosVendedor):
            self.janela.button_1['command'] = lambda: deletarVendedor(cpf=self.janela.entry_1.get())
            self.janela.button_2['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
            self.janela.button_3['command'] = lambda: MudarInfo()
        else:
            self.janela.window.destroy()
            self.janela = TelaDadosVendedor()
            self.janela.button_2['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
            self.janela.button_1['command'] = lambda: deletarVendedor(cpf=self.janela.entry_1.get())
            self.janela.button_3['command'] = lambda: MudarInfo()


    def dadosRemedio(self):
        def MudarInfo():
            try:
                InfoRemedio = mostrarInformacoesRemedio(lote=self.janela.entry_1.get())
                if InfoRemedio:
                    self.janela.canvas.itemconfig(self.janela.nomeTxt, text=f"Nome: {InfoRemedio[0]}")
                    self.janela.canvas.itemconfig(self.janela.empresaTxt, text=f"Empresa: {InfoRemedio[1]}")
                    self.janela.canvas.itemconfig(self.janela.tipoTxt, text=f"Tipo: {InfoRemedio[3]}")
                    self.janela.canvas.itemconfig(self.janela.precoTxt, text=f"Preço: R$ {str(InfoRemedio[4]).replace('.',',')}" + '0')
                    self.janela.canvas.itemconfig(self.janela.marcaTxt, text=f"Marca: {InfoRemedio[5]}")
                else:
                    self.janela.canvas.itemconfig(self.janela.nomeTxt, text="Nome: ")
                    self.janela.canvas.itemconfig(self.janela.empresaTxt, text="Empresa: ")
                    self.janela.canvas.itemconfig(self.janela.tipoTxt, text="Tipo: ")
                    self.janela.canvas.itemconfig(self.janela.precoTxt, text="Preço: ")
                    self.janela.canvas.itemconfig(self.janela.marcaTxt, text="Marca: ")
            except Exception as e:
                print(f"Erro ao obter informações do remédio: {e}")

        if isinstance(self.janela, TelaDadosRemedio):
            self.janela.button_1['command'] = lambda: deletarRemedio(lote=self.janela.entry_1.get())
            self.janela.button_2['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
            self.janela.button_3['command'] = lambda: MudarInfo()
        else:
            self.janela.window.destroy()
            self.janela = TelaDadosRemedio()
            self.janela.button_2['command'] = lambda: self.menu(cnpj=self.cnpj_conta, nome_empresa=self.GetNomeEmpresa(self.cnpj_conta))
            self.janela.button_1['command'] = lambda: deletarRemedio(lote=self.janela.entry_1.get())
            self.janela.button_3['command'] = lambda: MudarInfo()

aplicacao = App()
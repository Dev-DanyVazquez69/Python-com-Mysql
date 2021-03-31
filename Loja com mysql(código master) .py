import mysql.connector
import PySimpleGUI as sg

class jogos_ps2():
    def __init__(self):
        '''self.banco = mysql.connector.connect(
        host ="localhost",
        username = "root",
        passwd="",
        database = "ps2")'''
        self.lista = []
        sg.theme("tealmono")
        self.layout = [
            [sg.Text("Código do produto"),sg.Input(key = "codigo")],
            [sg.Text("Nome do produto  "),sg.Input(key = "nome")],
            [sg.Text("Valor do produto  "),sg.Input(key = "valor")],
            [sg.Checkbox("Eletronico",key = "Eletronico"),sg.Checkbox("Eletrodoméstico",key = "Eletrodoméstico"),sg.Checkbox("Informatica",key = "Informatica")],
            [sg.Button("Inserir no banco de dados"),sg.Button("Registrar produto em txt"),sg.Button("Listar do txt"),sg.Button("Excluir"),sg.Button("Sair")],
            [sg.Output(key = "output",size = (70,10),background_color = "black",text_color = "red")]
        ]
        self.janela = sg.Window("dany vazquez",layout = self.layout)
    def iniciar(self):
        while True:
            self.eventos,self.valores = self.janela.read()
            if self.eventos == "Sair" :
                break
            elif self.eventos == "Registrar produto em txt":
                if self.valores["codigo"] and self.valores["nome"] and self.valores["valor"]:
                    self.listar_produtos()
                    sg.popup(f'Registro feito com sucesso\nCodigo:{self.codigo}\nNome:{self.nome}\nValor:R${self.valor}\nTipo:{self.tipo}')
                else:
                    sg.popup("Por favor preencha todos os campos")
            elif self.eventos == "Listar do txt":
                with open("produtos.txt","r") as arquivo:
                   txt = arquivo.read()
                if txt:
                    self.janela["output"].update("")
                    self.listar()
                else:
                    print("não há nenhum produto cadastrado")
            elif self.eventos == "Inserir no banco de dados":
                try:
                    self.banco_de_dados()
                    sg.popup(f'Registro feito com sucesso\nCodigo:{self.codigo}\nNome:{self.nome}\nValor:R${self.valor}\nTipo:{self.tipo}')
                except:
                    sg.popup("Erro:\nBanco de dados não conectado")
            elif self.eventos == "Excluir":
                try:
                    self.excluir()
                except:
                    sg.popup("Erro:\n-Comando invalido\n-Banco de dados não conectado")
            self.limpar_campos()
    def limpar_campos(self):
        self.janela["codigo"].update("")
        self.janela["nome"].update("")
        self.janela["valor"].update("")
        self.janela["Eletronico"].update("")
        self.janela["Eletrodoméstico"].update("")
        self.janela["Informatica"].update("")
    #esperando ver o video de commo adicionar uma nova janela
    def listar_produtos(self):
        if self.valores["Eletronico"]:
            self.tipo = "Eletronico"
        elif self.valores["Eletrodoméstico"]:
            self.tipo = "Eletrodoméstico"
        elif self.valores["Informatica"]:
            self.tipo = "Informatica"
        else:
            self.tipo = "Não definido"
        self.codigo = int(self.valores["codigo"])
        self.nome = self.valores["nome"]
        self.valor = float(self.valores["valor"])
        self.lista.append([f'codigo:{self.codigo},nome:{self.nome},valor:{self.valor},tipo:{self.tipo}'])
        with open("produtos.txt","a",newline = "",encoding = "utf-8") as arquivo:
                    arquivo.write(f'\nCodigo:{self.codigo}\nNome:{self.nome}\nValor:R${self.valor}\nTipo:{self.tipo}\n')
    def banco_de_dados(self):
        if self.valores["Eletronico"]:
            self.tipo = "Eletronico"
        elif self.valores["Eletrodoméstico"]:
            self.tipo = "Eletrodoméstico"
        elif self.valores["Informatica"]:
            self.tipo = "Informatica"
        else:
            self.tipo = "Não definido"
        self.codigo = int(self.valores["codigo"])
        self.nome = self.valores["nome"]
        self.valor = float(self.valores["valor"])
        cursor = self.banco.cursor()
        #comandos que serão inseridos dentro do metodo execute
        comando_sql = "INSERT INTO produtos (Codigo,Nome,Valor,Tipo) VALUES(%s,%s,%s,%s)"
        #dados que completarão as linhas com %s
        dados = (self.codigo,self.nome,self.valor,self.tipo)
        cursor.execute(comando_sql,dados)
        #metodo para inserção de dados na tabela
        self.banco.commit()
    def listar(self):
        with open("produtos.txt","r") as arquivo:
            print(arquivo.read())
    def excluir(self):
        cursor = self.banco.cursor()
        #comandos que serão inseridos dentro do metodo execute
        a_ser_excluido =str(input("Codigo do produto a ser excluido__")) #Vou ter que criar um input onde irá pedir uma indentificação ao produto que sera excluso
        comando = f"DELETE FROM produtos where codigo ={a_ser_excluido}"
        comando_sql = comando
        cursor.execute(comando_sql)
        

dany = jogos_ps2()
dany.iniciar()
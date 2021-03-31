import mysql.connector

banco = mysql.connector.connect(
    host ="localhost",
    username = "root",
    passwd="",

    database = "PYTHON_TESTE_MY_SQL")

cursor = banco.cursor()
#comandos que serão inseridos dentro do metodo execute
comando_sql = "INSERT INTO agenda (nome,idade,telefone) VALUES(%s,%s,%s)"
#dados que completarão as linhas com %s
dados = ("geylson","15","geylson..@gmail.com")
cursor.execute(comando_sql,dados)
#metodo para inserção de dados na tabela
banco.commit()
#algoritmo para verificar se o arquivo txt está vazio
'''with open("produtos.txt","r") as arquivo:
    txt= arquivo.read()
if txt:
    print("oi")
else: 
    print("n oi")'''

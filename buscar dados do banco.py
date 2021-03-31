import mysql.connector
'''#A = adicionar
#w = criar e sobreescrever
#r = apenas ler
with open("criar aki.txt","w+",encoding= "utf-8") as arquivo:
    arquivo.write("Olá pessoas eu sou o léo e eu sou o miguel")
    arquivo.seek(0,0)
    print(arquivo.read())'''

banco = mysql.connector.connect(
    host ="localhost",
    username = "root",
    passwd="",
    database = "ps2")
cursor = banco.cursor()
#comandos que serão inseridos dentro do metodo execute
comando_sql = "select * from produtos"
#dados que completarão as linhas com %s
#dados = (codigo,nome,valor,tipo)
cursor.execute(comando_sql)
x = cursor.fetchall()
for l in range(0,len(x)):
    print("")
    for c in range(4):
        print(x[l][c]) 
#metodo para inserção de dados na tabela
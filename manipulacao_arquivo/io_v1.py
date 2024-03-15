# Leitura básica
arquivo = open('pessoas.csv') #abre o arquivo
dados = arquivo.read() #armazena os dados (leitura) na memoria
arquivo.close() #fecha o arquivo


for registro in dados.splitlines():
  print('Nome: {}, Idade: {}'.format(*registro.split(','))) #* pega os argumentos presentes

# Leitura Stream usando strip()
arquivo = open('pessoas.csv')

for registro in arquivo:
  print('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) #strip remove os espaços nas bordas

arquivo.close()

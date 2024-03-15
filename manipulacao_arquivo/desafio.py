import csv
# from urllib import request


# Pegando os dados no site
""" def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o csv...')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/cirso-python/desafio-ibge.csv')
 """


# Lendo o arquivo
def read(arquivo):
    with open(arquivo, encoding='latin1') as entrada:
        print('Lendo o csv...')
        dados = csv.reader(entrada)
        print('Leitura completa!')
        for cidade in dados:
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read('desafio-ibge.csv')

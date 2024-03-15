# Função (def) sem retorno
from math import pi


def circulo(raio):
  print(f'Área do círculo: {pi * raio ** 2}')


if __name__ == '__main__':
  raio = float(input('Informe o raio: '))
  circulo(raio)

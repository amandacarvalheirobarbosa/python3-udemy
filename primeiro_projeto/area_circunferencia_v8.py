# Função (def) com retorno
from math import pi


def circulo(raio):
  return pi * raio ** 2


if __name__ == '__main__':
  raio = float(input('Informe o raio: '))
  area = circulo(raio)
  print(f'Área do circulo: {area}')

from math import pi
import sys


def circulo(raio):
  return pi * float(raio) ** 2


if __name__ == '__main__':
  raio = sys.argv[1] #entrada é passada no terminal, junto com a chamada do arquivo
  area = circulo(raio)
  print(f'Área do circulo: {area}')

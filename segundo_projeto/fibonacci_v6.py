# Fibonacci
def fibonacci(quantidade):
  resultado = [0, 1]
  # for i in range(quantidade - 2): #dá certo tb
  for _ in range(2, quantidade): #_ variavel que não é usada
    resultado.append(sum(resultado[-2:]))
  return resultado


if __name__ == '__main__':
  #Listar os 20 primeiros numeros da sequencia
  for fib in fibonacci(20):
    print(fib, end=',')

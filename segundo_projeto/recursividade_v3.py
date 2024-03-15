# Fibonacci com recursividade com operador ternario
def fibonacci(quantidade, sequencia=(0, 1)):
  # Importante: Condição de parada
  return sequencia if len(sequencia) == quantidade else \
    fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),)) #soma de tupla


if __name__ == '__main__':
  for fib in fibonacci(20):
    print(fib, end=',')

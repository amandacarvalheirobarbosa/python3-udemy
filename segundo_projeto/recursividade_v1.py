# Recursividade é quando a função chama ela mesmo.
# Sempre se atentar a condição de parada.


def imprimir(maximo, atual):
  if atual < maximo: #condição de parada!
    print(atual)
    imprimir(maximo, atual + 1)


imprimir(100, 1)

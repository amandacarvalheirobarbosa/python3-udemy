# Tuplas (array nao pode ser modificada)
dir(tuple)
#help(tuple)

tupla = tuple()
tupla = () #cria uma tupla
type(tupla)
tupla = ('um') #erro: cria uma string
type(tupla)

#para criar uma tupla com 1 elemento
tupla = ('um',)
type(tupla)

tupla[0]
#tupla[0] = 'novo' #erro: tupla nao muda.

cores = ('verde', 'amarelo', 'azul', 'azul', 'branco')
cores[0]
cores[-1]
cores[1:]
cores.index('amarelo')
cores.count('azul')
len(cores)

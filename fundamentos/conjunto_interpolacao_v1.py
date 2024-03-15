# Conjuntos

a = {1, 2, 3}
type(a)
#a[0] #não aceita indice
a = set('codddd3r')
print(a)
print('3' in a, 4 not in a)

{1, 2, 3} == {3, 2, 1, 3} #True: pois tem os mesmos numeros e nao importa a ordem

# Operações
c1 = {1, 2}
c2 = {2, 3}
c1.union(c2)
c1.intersection(c2)
c1.update(c2)
c1

c2 <= c1 #subconjunto
c1 >= c2 #superconjunto

{1, 2, 3} - {2}
c1 - c2
c1 -= {2}
c1
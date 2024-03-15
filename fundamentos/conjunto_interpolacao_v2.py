# Interpolação
from string import Template

nome, idade = 'Amanda', 26

#versão mais antiga e menos recomendada:
print('Nome: %s Idade: %d %r %r' % (nome, idade, True, False)) #%d para int, %.2f para float. Se usar %d para true ou false, converte pra 1 e 0

#mais recomendado para python < 3.6
print('Nome: {0} Idade: {1}'.format(nome, idade))

#mais utilizado e recomendado: python > 3.6
print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome: $n Idade: $idade')
print(s.substitute(n=nome, idade=idade))
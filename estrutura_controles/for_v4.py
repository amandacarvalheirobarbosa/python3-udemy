# For 4
from random import randint


# for i in range(1, 11):
#   if i == 6:
#     break
#   print(i)
# else:
#   print('Fim!')


def sortear_numeros():
  return randint(1, 6)


for x in range(1, 7):
  if x % 2 == 1:
    continue

  if x == sortear_numeros():
    print('ACERTOU!!', x)
    break
else:
  print('NÃO ACERTOU!!')

def get_tipo_dia(dia):
  dias = {
      1: 'Fim de semana',
      2: 'Semana',
      3: 'Semana',
      4: 'Semana',
      5: 'Semana',
      6: 'Semana',
      7: 'Fim de semana',
  }
  return dias.get(dia, '** INVÁLIDO **')


if __name__ == '__main__':
  for dia in range(0, 9):
    print(f'{dia}: {get_tipo_dia(dia)}')


# A partir do python 3.10 surgiu o match que seria o switch
def get_tipo_dia(dia):
  match dia:
    case 2 | 3 | 4 | 5 | 6 :
      return 'Dia de semana'
    case 1 | 7:
      return 'Fim de semana'
    case _:
      return '** inválido **'


if __name__ == '__main__':
  for dia in range(0, 9):
    print(f'{dia}: {get_tipo_dia(dia)}')

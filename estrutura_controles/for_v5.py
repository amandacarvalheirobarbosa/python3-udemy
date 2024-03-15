# For 5

#variavel com letras maiusculas, por convenção para variaveis constantes
PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida',
]


for texto in textos:
  found = False
  for palavra in texto.lower().split():
    if palavra in PALAVRAS_PROIBIDAS:
      print('Texto possui pelo menos uma palavra proibida: ', palavra)
      found = True
      break

    if not found:
      print('Texto autorizado: ', texto)

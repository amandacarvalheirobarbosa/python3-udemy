# Dicionários 2
pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
pessoa
pessoa.pop('idade') #acessa e exclui valor
pessoa
pessoa.update({'idade': 40, 'Sexo': 'M'})
pessoa
del pessoa['cursos']
pessoa
pessoa.clear()
pessoa
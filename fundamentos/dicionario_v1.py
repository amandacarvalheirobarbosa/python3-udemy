# Dicionários (chave e valor obrigatório)
dir(dict)

pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
type(pessoa)
len(pessoa)
pessoa
pessoa['nome']
pessoa['idade']
pessoa['cursos']
pessoa['cursos'][1]
#pessoa['tags'] #dá erro pois nao existe
pessoa.keys()
pessoa.values()
pessoa.items()
pessoa.get('idade')

pessoa.get('tags') #nao dá erro
pessoa.get('tags', []) #se não tiver, retorna vazio
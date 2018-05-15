# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 9	Questão: É Quadrado Mágico?

def eh_quadrado_magico(quadrado):
	lista = []
	for i in quadrado:
		for j in i:
			if j not in lista:
				lista.append(j)
	
	aux = []
	for i in quadrado:
		for j in i:
			aux.append(j)
	
	if lista == aux and len(quadrado) != 0:
		# Somando Linhas:
		soma_linha = 0
		lista_linhas = []
		linha = 0
		while linha <= len(quadrado)-1:
			for i in range(len(quadrado[linha])):
				soma_linha += quadrado[linha][i]
			lista_linhas.append(soma_linha)
			soma_linha = 0
			linha += 1
		
		# Somando Colunas:
		soma_coluna = 0
		lista_colunas = []
		coluna = 0
		while coluna <= len(quadrado)-1:
			for j in range(len(quadrado)):
				soma_coluna += quadrado[j][coluna]
			lista_colunas.append(soma_coluna)
			soma_coluna = 0
			coluna += 1
		
		lista_final = lista_linhas + lista_colunas
		
		# Somando Diagonal:
		soma_diagonal = 0
		for d in range(len(quadrado)):
			soma_diagonal += quadrado[d][d]
		lista_final.append(soma_diagonal)
		
		# Somando Diagonal Secundária:
		soma_diagonal_sec = 0
		for ds in range(len(quadrado)):
			soma_diagonal_sec += quadrado[ds][(len(quadrado)-1) - ds]
		lista_final.append(soma_diagonal_sec)
		
		teste = lista_final[0]
		for i in lista_final:
			if i != teste:
				return False
		return True
	else:
		return False

quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
quadrado2 = [[1,2,3],[4,5,6]]
quadrado3 = []
assert eh_quadrado_magico(quadrado1)
assert not eh_quadrado_magico(quadrado2)
assert not eh_quadrado_magico(quadrado3)

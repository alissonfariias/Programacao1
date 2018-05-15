# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Meu Insert

def meu_insert(posicao, elemento, lista):
	lista.append(elemento)
	for i in range(len(lista)-1,-1,-1):
		if lista[i] == elemento:
			if i != posicao:
				lista[i], lista[i-1] = lista[i-1], lista[i]
	
	return lista

lista = ['joel', 'gil', 'santana', 'marcos', 'pedro', 'abel', 'julio']
print meu_insert(1, 'alisson', lista)

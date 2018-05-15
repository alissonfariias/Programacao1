# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Universidade Federal de Campina Grande
# Período: 2017.2
# Unidade: 7	Questão: Lista Presença

def cria_lista_presenca(turmas, nomes, num):
	lista = []
	for i in range(len(turmas)):
		if turmas[i] == num:
			lista.append(nomes[i])
	
	return lista
	
turmas = [1, 2, 2, 4, 5, 3, 5]
nomes = ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
assert cria_lista_presenca(turmas, nomes, 5) == ["Carla", "Jose"]

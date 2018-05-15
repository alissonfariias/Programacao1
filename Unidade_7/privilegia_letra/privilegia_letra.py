# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Privilegia Letra

def letra_magica(fila, letra):

	indice = 0
	for i in range(len(fila)):
		if fila[i][0] == letra:
			j = i
			while j > indice:
				fila[j], fila[j-1] = fila[j-1], fila[j]
				j -= 1
			indice += 1
			
fila = ["carlos", "bruno", "andre", "daniel", "ana", "carla"]
assert letra_magica(fila, "a") is None
assert fila == ["andre", "ana", "carlos", "bruno", "daniel", "carla"]

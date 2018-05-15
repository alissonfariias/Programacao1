# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 6, Questão: Mais Velhos Primeiro

def idosos_inicio(fila):
	
	indice = 0
	for i in range(len(fila)):
		if fila[i] >= 60:
			fila[i], fila[indice] = fila[indice], fila[i]
			indice += 1
	
	print fila

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]

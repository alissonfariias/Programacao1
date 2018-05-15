# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 9	Questão: Toppl

def filtra_alunos(alunos, inscritos, media):
	cont = 0
	for i in range(len(alunos)-1,-1,-1):
		if alunos[i][0] not in inscritos or alunos[i][1] < media:
			cont += 1
			alunos.pop(i)
	return cont

inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]

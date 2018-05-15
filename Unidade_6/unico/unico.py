# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 6	Questão: Único

def unico(string):

	nova_string = ''
	for i in range(len(string)):
		if string[i] not in nova_string:
			nova_string += string[i]
	return nova_string
	
assert unico("aa***xxxzzb+++") == "a*xzb+"
assert unico("") == ""

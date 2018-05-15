# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 8	Questão: Verificando se uma String é Substring de Outra String

def is_substring(str1, str2):
	for i in range(len(str1) - len(str2) +1):
		atual = ''
		for j in range(i, len(str2)+i):
			atual += str1[j]
		if atual == str2:
			return True
	return False

assert is_substring('boiada','oi')
assert not is_substring('casorio', 'casa')

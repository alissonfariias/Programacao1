# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Ciência da Computação - Programação I
# Aluno: Walisson Nascimento de Farias	Matrícula: 117210716
# Unidade: 6	Questão: Minha Implementação para o Método join

def meu_join(delimitador, sequencia_de_string):
	nova_sequencia = ''
	if len(sequencia_de_string) == 1:
		return sequencia_de_string[0]
	for i in range(len(sequencia_de_string)):
		if i == (len(sequencia_de_string)-1):
			nova_sequencia += sequencia_de_string[i]
		else:
			nova_sequencia += sequencia_de_string[i] + delimitador
	return nova_sequencia

assert meu_join("*", "a") == "a"
assert meu_join("*", "abc") == "a*b*c"
assert meu_join("*", ["a", "b", "c"]) == "a*b*c"
assert meu_join('*', ["a"]) == "a"
assert meu_join('', "abc") == 'abc'
assert meu_join('*', ["a", "b", "a"]) == 'a*b*a'

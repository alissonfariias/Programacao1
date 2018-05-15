# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 9	Questão: Square Code

def square_code(mensagem):

	def meu_join(delimitador, sequencia_de_string):
		nova_sequencia = ''
		if len(sequencia_de_string) == 1:
			nova_sequencia += sequencia_de_string[0]
		else:
			for i in range(len(sequencia_de_string)):
				if i == (len(sequencia_de_string)-1):
					nova_sequencia += sequencia_de_string[i]
				else:
					nova_sequencia += sequencia_de_string[i] + delimitador
		return nova_sequencia
	
	import math
	
	string = ''
	for i in range(len(mensagem)):
		if mensagem[i].isalpha():
			string += mensagem[i]
	
	numero_linhas = len(string) ** 0.5
	numero_colunas = int(math.ceil(len(string) / numero_linhas))
	numero_linhas = int(math.floor(numero_linhas))
	
	palavra = ''
	lista = []
	for j in range(len(string)):
		palavra += string[j]
		if (j+ 1) % numero_colunas == 0:
			lista.append(palavra)
			palavra = ''
	if len(palavra) != 0:
		lista.append(palavra)
	
	final = [''] * numero_colunas
	
	for i in lista:
		for j in range(len(i)):
			final[j] += i[j]
	
	return meu_join(' ', final)

m = "O tatu virou uma bola!!!"
assert square_code(m) == "Ovul tima ara tob uuo"

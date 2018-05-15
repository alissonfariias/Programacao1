# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Programação I - Período: 2017.2
# Unidade: 7, Questão: Cria Senha

def criaSenhaFraca(palavra):
	senha = '((%s))' % palavra
	return senha

def criaSenhaForte(palavra):
	senha = ''
	for i in palavra:
		if i == 'o' or i == 'O':
			senha += '0'
		elif i == 'i' or i == 'I' or i == 'L' or i == 'l':
			senha += '1'
		elif i == 'e' or i == 'E':
			senha += '3'
		elif i == 'a' or i == 'A':
			senha += '4'
		elif i == 'b' or i == 'B':
			senha += '6'
		elif i == 't' or i == 'T':
			senha += '7'
		else:
			senha += i
	senha = '((%s))' % senha
	return senha

lista = []
while True:
	dados = raw_input().split()
	if dados[0] == '*' or dados[0] == '***':
		break
	palavra = dados[0]
	seguranca = dados[1]
	if seguranca == 'fraco':
		lista.append(criaSenhaFraca(palavra))
	elif seguranca == 'forte':
		lista.append(criaSenhaForte(palavra))

for i in lista:
	print i

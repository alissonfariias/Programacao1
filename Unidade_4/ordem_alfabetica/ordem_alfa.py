# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 4	Questão: Ordem Alfabética

quantidade_palavras = int(raw_input())

lista = []
for i in range(quantidade_palavras):
	palavra = raw_input()
	lista.append(palavra)

print '---'

palavra_ref = raw_input()

antes = 0
depois = 0
for palavra in lista:
	if palavra < palavra_ref:
		antes += 1
	elif palavra > palavra_ref:
		depois += 1

print '%i antes' % antes
print '%i depois' % depois

# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5 	-	Questão: Aprovados no ENEM

lista_nomes = []
lista_notas = []
while True:
	dados = raw_input().split()
	if dados[0] == "fim":
		break
	nomes = dados[0]
	notas = int(dados[1])
	lista_nomes.append(nomes)
	lista_notas.append(notas)

nota_de_corte = int(raw_input())

cont = 0
for i in range(len(lista_notas)):
	if lista_notas[i] >= nota_de_corte:
		print '%s, %d' % (lista_nomes[i], lista_notas[i])
		cont += 1
if cont == 0:
	print 'Nenhum candidato aprovado.'

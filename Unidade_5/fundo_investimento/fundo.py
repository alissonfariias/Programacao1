# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 5	Questão: Fundo de Investimento

soma = 0.0
cont = 0
lista = []
while True:
	cont += 1
	sequencia = float(raw_input())
	lista.append(sequencia)
	soma += sequencia
	media = soma / cont
	if media > sequencia:
		soma = 0.0
		for e in range(len(lista)):
			if e != (len(lista)-1):
				soma += lista[e]
		nova_media = soma / (len(lista)-1)
		print 'Saldo total do FIS: R$%.2f.' % soma 
		print 'Média das contribuições: R$%.2f.' % nova_media
		break

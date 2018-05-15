# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

nota_escrita1 = float(raw_input())
nota_didatica1 = float(raw_input())
nota_titulacao1 = float(raw_input())
idade1 = int(raw_input())
nota_escrita2 = float(raw_input())
nota_didatica2 = float(raw_input())
nota_titulacao2 = float(raw_input())
idade2 = int(raw_input())

peso_notaescrita1 = nota_escrita1 * 0.3
peso_notadidatica1 = nota_didatica1 * 0.4
peso_notatitulacao1 = nota_titulacao1 * 0.3
peso_notaescrita2 = nota_escrita2 * 0.3
peso_notadidatica2 = nota_didatica2 * 0.4
peso_notatitulacao2 = nota_titulacao2 * 0.3
media1 = peso_notaescrita1 + peso_notadidatica1 + peso_notatitulacao1
media2 = peso_notaescrita2 + peso_notadidatica2 + peso_notatitulacao2

if media1 > media2:
	print 'O primeiro candidato foi aprovado com média %.1f.' % media1
elif media1 < media2:
	print 'O segundo candidato foi aprovado com média %.1f.' % media2
elif media1 == media2:
	if idade1 > idade2:
		print 'O primeiro candidato foi aprovado com média %.1f.' % media1
	elif idade1 < idade2:
		print 'O segundo candidato foi aprovado com média %.1f.' % media2
	elif idade1 == idade2:
		print 'Empate.'

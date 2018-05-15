# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())
faltas_disciplina = float(raw_input())
media = (nota1 + nota2 + nota3) / 3.0
if faltas_disciplina <= 22 and media >= 7.0:
	print 'aprovado por media'
elif faltas_disciplina >= 23:
	print 'reprovado por faltas'
elif faltas_disciplina <= 22:
	if media < 4.0:
		print 'reprovado por nota'
	elif media >= 4.0 and media < 7.0:
		print 'prova final'


# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

cre = float(raw_input())
experiencia = int(raw_input())
nota_entrevista = int(raw_input())

if cre < 7.0:
	if experiencia < 6:
		print 'Candidato eliminado. CRE e experiência abaixo do limite.'
	elif experiencia >= 6:
		print 'Candidato eliminado. CRE abaixo do limite.'
elif cre >= 7.0:
	if experiencia < 6:
		print 'Candidato eliminado. Experiência abaixo do limite.'
	elif experiencia >= 6:
		if nota_entrevista >= 1 and nota_entrevista <= 3:
			print 'Candidato classificado.'
		elif nota_entrevista > 3 and nota_entrevista <= 5:
			print 'Candidato aprovado.'

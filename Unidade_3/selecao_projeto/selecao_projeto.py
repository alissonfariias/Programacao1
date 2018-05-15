# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
cre = float(raw_input())
experiencia = int(raw_input())
nota_entrevista = float(raw_input())
if cre < 7 and experiencia < 6:
	print 'Candidato eliminado. CRE e experiência abaixo do limite.'
elif cre < 7 and experiencia >= 6:
	print 'Candidato eliminado. CRE abaixo do limite.'
elif cre >= 7 and experiencia < 6:
	print 'Candidato eliminado. Experiência abaixo do limite.'
elif cre >= 7 and experiencia > 6:
	if nota_entrevista <= 3:
		print 'Candidato classificado.'
	elif nota_entrevista > 3:
		print 'Candidato aprovado.'

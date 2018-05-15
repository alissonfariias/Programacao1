# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
n_semestres = int(raw_input())
ensino = int(raw_input())
prod_intelectual = int(raw_input())
orientacao = int(raw_input())
ativ_administrativa = int(raw_input())
if n_semestres < 4:
	print "Promoção indeferida. Número de semestres insuficiente."
elif n_semestres >= 4:
	if ensino >= 320 and prod_intelectual >= 100 and orientacao >= 20:
		media = (ensino + prod_intelectual + orientacao + ativ_administrativa) / 4
		if media < 140:
			print "Promoção indeferida. Média insuficiente."
		elif media >= 140:
			print "Promoção deferida. Parabéns!"
	else:
		print "Promoção indeferida. Pontuação mínima não alcançada."

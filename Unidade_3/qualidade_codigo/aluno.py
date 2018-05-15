# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Ciclo Trigonométrico

angulo = float(raw_input())	
if angulo <= 360:
	if angulo >= 1 and angulo <= 89:
		print 'Quadrante 1' 
	elif angulo > 90 and angulo < 180:
		print 'Quadrante 2'
	elif angulo > 180 and angulo < 270:
		print 'Quadrante 3'
	elif angulo > 270 and angulo < 360:
		print 'Quadrante 4'
	else:
		print 'Sobre eixos'
if angulo > 360:
	num2 = angulo % 360	
	if num2 >= 1 and num2 <= 89:
		print 'Quadrante 1'
	elif num2 > 90 and num2 < 180:
		print 'Quadrante 2'
	elif num2 > 180 and num2 < 270:
		print 'Quadrante 3'
	elif num2 > 270 and num2 < 360:
		print 'Quadrante 4'
	else:
		print 'Sobre eixos'

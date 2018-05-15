# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

import math

delta = b ** 2 - 4 * a * c
if delta < 0:
	print 'sem raizes reais'
elif delta == 0:
	raiz_de_delta = math.sqrt(delta)	
	x1 = ((-1*b) + raiz_de_delta) / (2 * a)
	x2 = ((-1*b) - raiz_de_delta) / (2 * a)
	print 'x = %.2f' % (x1 or x2)
else:
	raiz_de_delta = math.sqrt(delta)	
	x1 = ((-1*b) + raiz_de_delta) / (2 * a)
	x2 = ((-1*b) - raiz_de_delta) / (2 * a)
	print 'x1 = %.2f\nx2 = %.2f' % (x1,x2)

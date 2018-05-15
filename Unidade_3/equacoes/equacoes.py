# coding: utf-8
# Nome: Walisson Nascimento de Farias
# Ciências da Computação UFCG - 2017.2
# Matrícula: 117210716

a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

import math
delta = (b**2)-4*a*c

x1 = (-b+raizdelta)/(2*a)
x2 = (-b-raizdelta)/(2*a)

if delta < 0:
	print "sem raizes reais"
elif delta == 0:
	print x1 or x2
elif delta > 0:
	print "x1 = %.2f\nx2 = %.2f" % (x1,x2)

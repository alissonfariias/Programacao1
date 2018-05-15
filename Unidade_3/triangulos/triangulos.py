# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

l_a = int(raw_input())
l_b = int(raw_input())
l_c = int(raw_input())
perimetro = (l_a + l_b + l_c)

if l_a < l_b + l_c and l_a > l_b - l_c:
	print 'triangulo valido. %i' % perimetro
elif l_b < l_a + l_c and l_b > l_a - l_c:
	print 'triangulo valido. %i' % perimetro
elif l_c < l_a + l_b and l_c > l_a - l_b:
	print 'triangulo valido. %i' % perimetro
else:
	print 'triangulo invalido.'

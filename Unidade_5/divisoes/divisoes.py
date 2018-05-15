# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5 	-	Questão: Divisão por Subtrações

D, d = raw_input().split()
quociente = 0
d_maior = True
while d_maior:
	D = int(D)
	d = int(d)
	if D >= d:
		print '%i - %i = %i' % (D, d, D-d)
		D = D - d
		quociente += 1
	else:
		print '%i - %i < 0' % (D, d)
		d_maior = False
	
print '==='
print 'quociente = %i' % quociente 
print 'resto = %i' % D

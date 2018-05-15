# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Herão

a = int(raw_input())
l = []

for i in range(a):
	a,b,c = raw_input().split()
	a,b,c = float(a), float(b), float(c)
	soma = (a+b+c) / 2.0
	area = (soma * (soma -a) * (soma - b) * (soma - c)) ** 0.5
	l.append(area)
	
cont = 0
m = 0

for i in range(len(l)):
	print 'Área {}: {:.2f}'.format(i + 1, l[i])
	if l[i] > 100:
		cont += 1
		m += l[i]

if cont > 0:
	m = float(m) / cont
	print 'Número maiores: {:.0f}, área média: {:.2f}'.format(cont, float(m))

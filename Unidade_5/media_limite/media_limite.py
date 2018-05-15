# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5, Questão: Média Atinge Limite

medias = [] 
cont = 0
soma = 0
while True:
	numero = raw_input()
	if numero == '-':
		break
	cont += 1
	soma += float(numero)
	medias.append(soma/cont)

alcancado = False
valor_limite = float(raw_input())
for i in range(len(medias)):
	if medias[i] > valor_limite:
		print 'media = %.1f' % medias[i]
		print 'num = %i' % (i+1)
		alcancado = True
		break

if alcancado == False:
	print 'limite não alcançado'

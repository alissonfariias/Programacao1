# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: SAMU

dias = []
soma = 0
for i in range(1,13):
	meses = raw_input()
	dias.append(meses)
	soma += int(meses)

media = soma/12.0
print 'Média mensal de atendimentos: %.2f' % media
print '----'

for j in range(len(dias)):
	if int(dias[j]) > media:
		print 'Mês %i: %i' % (int(j+1),int(dias[j]))
	else:
		pass

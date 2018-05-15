# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5, Questão: Operações Bancárias

dados = raw_input().split()

cliente = dados[0]
saldo_atual = float(dados[1])
while True:
	dados = raw_input().split()
	if dados[0] == '3':
		break
	if dados[0] == '1':
		saldo_atual -= float(dados[1])
	if dados[0] == '2':
		saldo_atual += float(dados[1])

print 'Saldo de R$ %.2f na conta de %s' % (saldo_atual,cliente)

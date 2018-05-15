# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 5
# QUESTÃO: Premiação Cliente

compras_joao = 0
compras_julio = 0
while compras_joao <= 2 or compras_julio <= 2 or quanto_gastou < 2000:
	dados = raw_input().split()
	if dados[0] == 'fim':
		print 'Não houve vencedor.'
		break
	nome_cliente = dados[0]
	quanto_gastou = float(dados[1])
	if nome_cliente == 'joao' and quanto_gastou >= 2000.0:
		print 'joao foi o vencedor. Comprou mais R$ 2000.00 no período.'
		break
	if nome_cliente == 'julio' and quanto_gastou >= 2000.0:
		print 'julio foi o vencedor. Comprou mais R$ 2000.00 no período.'
		break
	if nome_cliente == 'joao' and quanto_gastou < 2000.0:
		compras_joao += 1
		if compras_joao > 2:
			print 'joao foi o vencedor. Comprou mais de duas vezes no período.'
			break
	if nome_cliente == 'julio' and quanto_gastou < 2000.0:
		compras_julio += 1
		if compras_julio > 2:
			print 'julio foi o vencedor. Comprou mais de duas vezes no período.'
			break

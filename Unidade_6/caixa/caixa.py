# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 6, Questão: Caixa Registradora

def caixa_registradora(lista_valores, meta):
	
	soma_vendas = 0
	soma_comissao = 0
	for i in range(len(lista_valores)):
		soma_vendas += lista_valores[i]
		if lista_valores[i] < 1000:
			comissao = lista_valores[i] / 100 * 5
			soma_comissao += comissao
		elif lista_valores[i] >= 1000 and lista_valores[i] < 5000:
			comissao = lista_valores[i] / 100 * 10
			soma_comissao += comissao
		elif lista_valores[i] >= 5000:
			comissao = lista_valores[i] / 100 * 15
			soma_comissao += comissao
	
	if (soma_vendas - comissao) >= meta:
		situacao = 'Lucro'
	elif (soma_vendas - comissao) < meta:
		situacao = 'Prejuizo'
	
	resultado = []
	resultado.append(soma_vendas)
	resultado.append(soma_comissao)
	resultado.append(situacao)
	return resultado

assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']

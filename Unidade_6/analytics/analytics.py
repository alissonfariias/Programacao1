# coding: utf-8

votacao = []
votacao.append('greve geral,sim,543,joao,servidor')
votacao.append('greve geral,nao,543,marina,servidor')
votacao.append('indicativo de greve,sim,5,joao,professor')
votacao.append('paralisação,nao,543,julio,professor')
votacao.append('paralisação,sim,543,carlos,professor')
votacao.append('paralisação,sim,543,juliana,professor')
votacao.append('lei 1329,sim,99,joao,servidor')

def conta_votos(votacao,id_votacao):

	cont_sim = 0
	cont_nao = 0
	for i in range(len(votacao)):
		categorias = votacao[i].split(',')
		if id_votacao == int(categorias[2]):
			if categorias[1] == 'sim':
				cont_sim += 1
			elif categorias[1] == 'nao':
				cont_nao += 1
	
	lista = []
	lista.append(cont_sim)
	lista.append(cont_nao)
	
	return lista

assert conta_votos(votacao, 543) == [3,2]

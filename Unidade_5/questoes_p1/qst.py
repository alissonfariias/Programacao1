# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 5	Questão: Questões para P1

lista_nomes = []
pontuacao = []
while True:
	colaborador = raw_input()
	if colaborador == '**':
		break
	lista_nomes.append(colaborador)
	soma = 0
	while True:
		num_questoes = raw_input()
		if num_questoes == '*':
			break
		soma += int(num_questoes)
	pontuacao.append(soma)
	soma = 0

total = 0
for num in pontuacao:
	total += num

print 'Relatório de novas questões:\n'

for i in range(len(lista_nomes)):
	print '%s: %i' % (lista_nomes[i], pontuacao[i])

print '---'
print 'Total de novas questões: %i' % total

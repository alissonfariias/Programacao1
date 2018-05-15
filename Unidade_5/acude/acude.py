# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 5	Questão: Limite açude

limite_superior = float(raw_input())
nivel_atual = int(raw_input())

if nivel_atual >= limite_superior:
	print 'Açude passou a liberar água.'
	print 'Nível: %.2f' % nivel_atual
else:
	ultrapassou = False
	while ultrapassou == False:
		evento = raw_input().split()
		if evento[0] == 'chuva' or evento[0] == 'afluente':
			nivel_atual += int(evento[1])
			if nivel_atual >= limite_superior:
				ultrapassou = True
		if evento[0] == 'demanda':
			nivel_atual -= int(evento[1])
			if nivel_atual < 0:
				nivel_atual = 0
	
	print 'Açude passou a liberar água.'
	print 'Nível: %.2f' % nivel_atual
	

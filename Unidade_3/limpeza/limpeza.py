# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
servico = int(raw_input())
if servico == 1:
	tamanho_tanque = int(raw_input())
	preco = 80 * tamanho_tanque
	if preco >= 200:
		print 'R$ %2.f,00\nBrinde!' % preco
	if preco < 200:
		print 'R$ %2.f,00' % preco
elif servico == 2:
	tamanho_tanque = int(raw_input())
	preco = 50 * tamanho_tanque
	if preco >= 200:
		print 'R$ %2.f,00\nBrinde!' % preco
	if preco < 200:
		print 'R$ %2.f,00' % preco
elif servico == 3:
	print 'R$ 50,00'

# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

gols_campinense = int(raw_input())
gols_treze = int(raw_input())

if gols_campinense > gols_treze:
	print 'Campinense'
elif gols_treze > gols_campinense:
	print 'Treze'
elif gols_campinense == gols_treze:
	print 'Empate'

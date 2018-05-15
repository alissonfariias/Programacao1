# coding: utf-8
# Nome: Walisson Nascimento de Farias
# Ciências da Computação UFCG - 2017.2
# Matrícula: 117210

quantidade_pessoas = int(raw_input())
dinheiro = float(raw_input())

custo_tav = 100 * quantidade_pessoas
custo_onibus = 22 * quantidade_pessoas
if quantidade_pessoas % 4 == 0:
	custo_taxi = 200 * (quantidade_pessoas / 4)
if quantidade_pessoas % 4 != 0:
	custo_taxi = 200 * (quantidade_pessoas / 4) + 200

if custo_tav <= dinheiro:
	print "TAV. R$ %.2f" % custo_tav
elif custo_taxi <= dinheiro:
	print "Táxi. R$ %.2f" % custo_taxi
elif custo_onibus <= dinheiro:
	print "Ônibus. R$ %.2f" % custo_onibus
else:
	print "Não é possível realizar a viagem."

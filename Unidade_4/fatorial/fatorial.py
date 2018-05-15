# coding: utf-8
# Nome: Walisson Nascimento de Farias
# Ciências da Computação UFCG - 2017.2
# Matrícula: 117210716
# Unidade: 4
# Fatorial

n = int(raw_input())

n_fat = 1
for i in range(2,n+1):
	n_fat = n_fat * i

print n_fat

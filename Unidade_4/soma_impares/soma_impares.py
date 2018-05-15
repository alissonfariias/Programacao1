# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Soma Últimos Ímpares

quantidade = int(raw_input())
limite = int(raw_input())
lista = []

for c in range(quantidade):
	numero = int(raw_input())
	if numero % 2 != 0:
		lista.append(numero)

soma = 0
for i in range(-1, -len(lista) -1, -1):
	if lista[i] + soma < limite:
		soma += lista[i]
	else:
		break

print soma

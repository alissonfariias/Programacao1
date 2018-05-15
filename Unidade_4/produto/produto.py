# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Produto de Dois Somatórios

numero = raw_input()

soma_dos_pares = 0
soma_dos_impares = 0
for i in range(len(numero)):
	if i % 2 == 0:
		soma_dos_pares += int(numero[i])
	elif i % 2 != 0:
		soma_dos_impares += int(numero[i])

resultado = soma_dos_pares * soma_dos_impares
print '%05.i' % resultado

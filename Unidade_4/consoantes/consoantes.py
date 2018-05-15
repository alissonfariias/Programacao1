# coding: utf-8
# Nome: Walisson Nascimento de Farias
# Ciências da Computação UFCG - 2017.2
# Matrícula: 117210716
# Unidade: 4
# Início Consoantes

num = raw_input()

lista = []
for i in range(int(num)):
	palavra = raw_input()
	lista.append(palavra)

vogais = ['a','e','i','o','u','A','E','I','O','U']
consoantes = 0
for e in lista:
	if e[0] in vogais:
		pass
	else:
		consoantes += 1
		
porcentagem = consoantes * 100.0 / float(num)

print "total de palavras: %s" % int(num)
print "iniciadas por consoantes: %i (%.2f%%)" % (consoantes,porcentagem) 

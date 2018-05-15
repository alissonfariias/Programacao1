# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Universidade Federal de Campina Grande
# Período: 2017.2
# Letras Coincidentes

primeira_palavra = raw_input()
segunda_palavra = raw_input()

coincidentes = []
quant_coincidentes = 0
letra = []
for i in range(len(primeira_palavra)):
	if primeira_palavra[i] == segunda_palavra[i]:
		coincidentes.append(i+1)
		quant_coincidentes += 1
		letra.append(primeira_palavra[i])

print 'Letras coincidentes'
for i in range(len(letra)):
	print "'%s' na posição %s" % (letra[i],coincidentes[i])

quant_caracteres = len(primeira_palavra) + len(segunda_palavra)
porcentagem = quant_coincidentes * 100 / quant_caracteres
print 'Total de letras coincidentes: %i (%i%%)' % (quant_coincidentes,porcentagem)

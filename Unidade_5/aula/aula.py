# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 5 	-	Questão: Aula de médias

soma = 0
quant = 0
lista_notas = []
while True:
	numero = float(raw_input())
	soma += int(numero)
	quant += 1.0
	lista_notas.append(numero)
	if soma >= 100:
		break

media = soma / quant

print 'Quantidade de números lidos: %i' % quant
print 'Soma dos números lidos: %.2f' % soma
print 'Média = %.2f' % media
print ''
print 'Abaixo da média'
for i in range(len(lista_notas)):
	if lista_notas[i] < media:
		print '%.2f (%io)' % (lista_notas[i], i+1)
print ''
print 'Acima da média'
for i in range(len(lista_notas)):
	if lista_notas[i] > media:
		print '%.2f (%io)' % (lista_notas[i], i+1)

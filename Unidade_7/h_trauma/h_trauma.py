# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação I - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 7	Questão: Hospital de Trauma

pacien = []
urgen = []
vermelho = []
laranja = []
amarelo = []
verde = []
azul = []
lista = []

while True:
	pacientes = raw_input()
	if pacientes == 'fim':
		break
	pacientes = pacientes.split()
		
	pacien.append(pacientes[0])
	urgen.append(pacientes[1])

for i in range(len(urgen)):
	if urgen[i] == 'vermelho':
		vermelho.append(pacien[i])
	if urgen[i] == 'laranja':
		laranja.append(pacien[i])
	if urgen[i] == 'amarelo':
		amarelo.append(pacien[i])
	if urgen[i] == 'verde':
		verde.append(pacien[i])
	if urgen[i] == 'azul':
		azul.append(pacien[i])
		

lista = vermelho + laranja + amarelo + verde + azul

for j in range(len(lista)):
	print lista[j]
print '---'
print 'vermelho: %i' % len(vermelho)
print 'laranja: %i' % len(laranja)
print 'amarelo: %i' % len(amarelo)
print 'verde: %i' % len(verde)
print 'azul: %i' % len(azul)
print '---'

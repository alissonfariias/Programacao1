# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Aprovados e Reprovados

quant_alunos = raw_input()

soma_notas_maiores = 0
soma_notas_menores = 0
quant_aprovados = 0
quant_reprovados = 0
for i in range(int(quant_alunos)):
	nota = float(raw_input())
	if nota < 7.0:
		soma_notas_menores += nota
		quant_reprovados += 1
		media_reprovados = soma_notas_menores / quant_reprovados
	elif nota >= 7.0:
		soma_notas_maiores += nota
		quant_aprovados += 1
		media_aprovados = soma_notas_maiores / quant_aprovados

print 'Reprovados: %i' % quant_reprovados
if quant_reprovados > 0:
	print 'Média: %.1f' % media_reprovados
else:
	pass
print ''
print 'Aprovados: %i' % quant_aprovados
if quant_aprovados > 0:
	print 'Média: %.1f' % media_aprovados
else:
	pass

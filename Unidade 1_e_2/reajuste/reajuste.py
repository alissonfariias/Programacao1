# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Percentual de Reajuste

salario_minimo_atual = float(raw_input('Valor atual? '))
salario_minimo_novo = float(raw_input('Novo valor? '))

reajuste = salario_minimo_novo - salario_minimo_atual
porcentagem = reajuste * 100 / salario_minimo_atual
print 'Reajuste de %.1f%%' % porcentagem

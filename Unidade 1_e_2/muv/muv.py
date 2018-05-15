# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Movimento Uniformemente Variado

posicao_inicial = float(raw_input('Posição inicial? '))
velocidade_inicial = float(raw_input('Velocidade inicial? '))
tempo_deslocamento = float(raw_input('Tempo? '))
aceleracao = float(raw_input('Aceleração? '))

velocidade_final = velocidade_inicial + aceleracao * tempo_deslocamento
funcao_horaria = (posicao_inicial + (velocidade_inicial * tempo_deslocamento) + (aceleracao * (tempo_deslocamento ** 2)) / 2)
velocidade_media = (velocidade_inicial + velocidade_final) / 2

print ''
print 'Dados da questão'
print '================'
print '   Posição inicial: %.2f m' % posicao_inicial
print 'Velocidade inicial: %.2f m/s' % velocidade_inicial
print '        Aceleração: %.2f m/s2' % aceleracao
print '             Tempo: %.2f s' % tempo_deslocamento
print '  Velocidade final: %.2f m/s' % velocidade_final
print '  Velocidade média: %.2f m/s' % velocidade_media
print '     Posição final: %.2f m' % funcao_horaria

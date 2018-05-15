# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Espaço em Disco Simplificado

login1 = str(raw_input())
espaco1 = float(raw_input())
login2 = str(raw_input())
espaco2 = float(raw_input())
login3 = str(raw_input())
espaco3 = float(raw_input())

espaco1_mb = espaco1 / 1024 / 1024
espaco2_mb = espaco2 / 1024 / 1024
espaco3_mb = espaco3 / 1024 / 1024
espaco_total = espaco1_mb + espaco2_mb + espaco3_mb
espaco_medio = espaco_total / 3

print 'SPLab - Espaço utilizado pelos usuários'
print '---------------------------------------------'
print 'Nr., Usuário, Espaço Utilizado\n'
print '1, %s, %.2f MB' % (login1,espaco1_mb)
print '2, %s, %.2f MB' % (login2,espaco2_mb)
print '3, %s, %.2f MB\n' % (login3,espaco3_mb)
print 'Espaço total ocupado: %.2f MB' % espaco_total
print 'Espaço médio ocupado: %.2f MB' % espaco_medio

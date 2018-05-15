# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# IPTU

area_casa = float(raw_input('Área construída? '))
aliquota = float(raw_input('Alíquota? '))

iptu = area_casa * aliquota + 35.00
quota_unica = iptu * 0.75
seis_parcelas_total = iptu * 0.95
seis_parcelas_valor = seis_parcelas_total / 6
dez_parcelas_total = iptu
dez_parcelas_valor = iptu / 10

print 'IPTU: R$ %.2f' % iptu
print ''
print 'Pagamento:'
print '1. Quota única. R$ %.2f' % quota_unica
print '2. Em 6 parcelas. Total: R$ %.2f' % seis_parcelas_total
print '   6 x R$ %.2f' % seis_parcelas_valor
print '3. Em 10 parcelas. Total: R$ %.2f' % dez_parcelas_total
print '   10 x R$ %.2f' % dez_parcelas_valor

# coding: utf-8

print '== Estágio 1 =='
peso1 = float(raw_input('Peso? '))
nota1 = float(raw_input('Nota? '))
print '== Estágio 2 =='
peso2 = float(raw_input('Peso? '))
nota2 = float(raw_input('Nota? '))
print '== Estágio 3 =='
peso3 = float(raw_input('Peso? '))
nota3 = float(raw_input('Nota? '))
print '== Resultados =='
mediaparcial = peso1*nota1 + peso2*nota2 + peso3*nota3
notaminimafinal = mediaparcial * 0.6
notaminimafinal1 = (5.0 - notaminimafinal) / 0.4
notaminimafinal2 = (7.0 - notaminimafinal) / 0.4
print 'Média parcial: %.1f' % mediaparcial
print 'Nota na final, pra média 5.0 = %.1f' % notaminimafinal1
print 'Nota na final, pra média 7.0 = %.1f' % notaminimafinal2

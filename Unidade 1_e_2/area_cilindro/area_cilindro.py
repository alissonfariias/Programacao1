# coding: utf-8

print 'Cálculo da Superfície de um Cilindro\n---'
diametro = float(raw_input('Medida do diâmetro? '))
altura = float(raw_input('Medida da altura? '))
raio = diametro / 2.0
import math
a_base1 = math.pi * (raio ** 2.0)
a_base2 = math.pi * (raio ** 2.0)
perimetro = (math.pi * 2.0) * raio
a_lateral = altura * perimetro
a_cilindro = a_base1 + a_base2 + a_lateral
print '---\nÁrea calculada: %.2f' % a_cilindro

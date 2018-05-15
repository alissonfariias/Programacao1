# coding: utf-8

raio = float(raw_input())
diagonal = raio * 2
import math
lado = diagonal / math.sqrt(2)
area_quadrado = lado ** 2
area_circulo = math.pi * (raio ** 2)
area_nao_comum = area_circulo - area_quadrado
print 'Área não comum: %5.5f' % area_nao_comum

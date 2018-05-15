# coding: utf-8

import math
diametro = float(raw_input())
raio = diametro / 2
area = math.pi * (raio ** 2)
perimetro = (2 * math.pi) * raio
print "A: %.5f" % area
print "P: %.5f" % perimetro

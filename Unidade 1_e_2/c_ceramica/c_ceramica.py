# coding: utf-8

capacidade = float(raw_input('Capacidade de revestimento? '))
print '\n== Dados do vão a revestir =='
comprimento = float(raw_input('Comprimento? '))
largura = float(raw_input('Largura? '))
altura = float(raw_input('Altura? '))
area_chao =  comprimento * largura
perimetro = comprimento + largura + comprimento + largura
area_parede = perimetro * altura
area_total = area_chao + area_parede
n_caixas = area_total / capacidade
print '\n== Resultados =='
print 'Área total a revestir: %4.1f m2' % area_total
print 'Número de caixas: %1.f' % n_caixas

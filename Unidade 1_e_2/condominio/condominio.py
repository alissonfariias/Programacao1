# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Construção do Condomínio

lado1_terreno = float(raw_input())
lado2_terreno = float(raw_input())
area_casas = float(raw_input())

quantidade = float(lado1_terreno * lado2_terreno)
quantidade2 = quantidade / area_casas

print "%f casa(s) pode(m) ser construída(s) no terreno." % quantidade2

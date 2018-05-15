# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade: 7, Questão: Bubblesort

def bubble_sort(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1-i):
                if lista[j] > lista[j+1]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [0, 9, 1, 5, 1, 2, 3, 4, 5, 7, 6]

print bubble_sort(lista)

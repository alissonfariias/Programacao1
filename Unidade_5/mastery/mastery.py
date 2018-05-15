# coding: utf-8
# Matrícula: 117210716
# Aluno: Walisson Nascimento de Farias
# Atividade: Mastery Learning
# Disciplina : Programação 1
# Período : 2017.2
# Universidade Federal de Campina Grande

print "Mastery Learning"
print "Cálculo da nota na unidade\n"

nota1 = float(raw_input("Nota? "))
nota2 = float(raw_input("Nota? "))

maior_nota1 = nota1
maior_nota2 = nota2

if nota2 > nota1:
	maior_nota1= nota2
	maior_nota2 = nota1

media = (maior_nota1 + maior_nota2) / 2

cont_nota = 2
situacao = 'cursando'
if nota1 >= 7 or nota2 >= 7:
		situacao = 'aprovado'
penalizacao = 0
print 'Média: %.1f (%s)' % (media,situacao)
print 'Penalização: %.1f\n' % (penalizacao)

while True:
	if nota1 >= 7 or nota2 >= 7:
		break
	nota = float(raw_input("Nota? "))
	cont_nota += 1
	if nota > maior_nota1:
		maior_nota2 = maior_nota1
		maior_nota1 = nota

	if cont_nota > 2:
		penalizacao += 0.5
	
	if nota > 2 and nota < 7:
		media = (maior_nota1 + maior_nota2) / 2
		print 'Média: %.1f (%s)' % (media,situacao)
		print 'Penalização: %.1f\n' % (penalizacao)
		
	if nota >= 7:
		situacao = 'aprovado'
		media = (maior_nota1 + maior_nota2) / 2
		print 'Média: %.1f (%s)' % (media,situacao)
		print 'Penalização: %.1f\n' % (penalizacao)

	if nota >= 7:
		break

print "==="
print "Notas válidas: %.1f e %.1f" % (maior_nota1,maior_nota2)
print "Média parcial na unidade: %.1f" % (media)
print "Penalizações: %.1f" % (penalizacao)
print "Média final na unidade: %.1f" % (media - penalizacao)

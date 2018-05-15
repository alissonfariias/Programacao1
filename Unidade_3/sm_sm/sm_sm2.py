# coding: utf-8

numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
numero4 = int(raw_input())

segundo_menor = segundo_maior = 0

if numero1 <= numero2 and numero1 >= numero3 and numero1 >= numero4:
	segundo_maior = numero1
elif numero1 <= numero3 and numero1 >= numero4 and numero1 >= numero2:
	segundo_maior = numero1
elif numero1 <= numero4 and numero1 >= numero2 and numero1 >= numero3:
	segundo_maior = numero1
	
elif numero2 <= numero1 and numero2 >= numero3 and numero2 >= numero4:
	segundo_maior = numero2
elif numero2 <= numero3 and numero2 >= numero4 and numero2 >= numero1:
	segundo_maior = numero2
elif numero2 <= numero4 and numero2 >= numero1 and numero2 >= numero3:
	segundo_maior = numero2

elif numero3 <= numero2 and numero3 >= numero1 and numero3 >= numero4:
	segundo_maior = numero3
elif numero3 <= numero1 and numero3 >= numero4 and numero3 >= numero2:
	segundo_maior = numero3
elif numero3 <= numero4 and numero3 >= numero2 and numero3 >= numero1:
	segundo_maior = numero3

else:
	segundo_maior = numero4
	
# segundo menor

if numero1 >= numero2 and numero1 <= numero3 and numero1 <= numero4:
	segundo_menor = numero1
elif numero1 >= numero3 and numero1 <= numero4 and numero1 <= numero2:
	segundo_menor = numero1
elif numero1 >= numero4 and numero1 <= numero2 and numero1 <= numero3:
	segundo_menor = numero1

elif numero2 >= numero1 and numero2 <= numero3 and numero2 <= numero4:
	segundo_menor = numero2
elif numero2 >= numero3 and numero2 <= numero4 and numero2 <= numero1:
	segundo_menor = numero2
elif numero2 >= numero4 and numero2 <= numero1 and numero2 <= numero3:
	segundo_menor = numero2

elif numero3 >= numero2 and numero3 <= numero1 and numero3 <= numero4:
	segundo_menor = numero3
elif numero3 >= numero1 and numero3 <= numero4 and numero3 <= numero2:
	segundo_menor = numero3
elif numero3 >= numero4 and numero3 <= numero2 and numero3 <= numero1:
	segundo_menor = numero3

else:
	segundo_menor = numero4

print "Considerando os números %i, %i, %i e %i" % (numero1,numero2,numero3,numero4)
print "O segundo menor número é %i" % segundo_menor
print "O segundo maior número é %i" % segundo_maior

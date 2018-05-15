# coding: utf-8
numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
numero4 = int(raw_input())

if numero1 < numero2 and numero3 and numero4:
	if numero2 < numero3 and numero4:
		segundomenor = numero2
	elif numero3 < numero2 and numero4:
		segundomenor = numero3
	elif numero4 < numero2 and numero3:
		segundomenor = numero4
elif numero2 < numero1 and numero3 and numero4:
	if numero1 < numero3 and numero4:
		segundomenor = numero1
	elif numero3 < numero1 and numero4:
		segundomenor = numero3
	elif numero4 < numero1 and numero3:
		segundomenor = numero3
elif numero3 < numero1 and numero2 and numero4:
	if numero1 < numero2 and numero4:
		segundomenor = numero1
	elif numero2 < numero1 and numero4:
		segundomenor = numero2
	elif numero4 < numero1 and numero2:
		segundomenor = numero4
elif numero4 < numero1 and numero2 and numero3:
	if numero1 < numero2 and numero3:
		segundomenor = numero1
	elif numero2 < numero1 and numero3:
		segundomenor = numero2
	elif numero3 < numero1 and numero2:
		segundomenor = numero3

if numero1 > numero2 and numero3 and numero4:
	if numero2 > numero3 and numero4:
		segundomaior = numero2
	elif numero3 > numero2 and numero4:
		segundomaior = numero3
	elif numero4 > numero2 and numero3:
		segundomaior = numero4
elif numero2 > numero1 and numero3 and numero4:
	if numero1 > numero3 and numero4:
		segundomaior = numero1
	elif numero3 > numero1 and numero4:
		segundomaior = numero3
	elif numero4 > numero1 and numero3:
		segundomaior = numero3
elif numero3 > numero1 and numero2 and numero4:
	if numero1 > numero2 and numero4:
		segundomaior = numero1
	elif numero2 > numero1 and numero4:
		segundomaior = numero2
	elif numero4 > numero1 and numero2:
		segundomaior = numero4
elif numero4 > numero1 and numero2 and numero3:
	if numero1 > numero2 and numero3:
		segundomaior = numero1
	elif numero2 > numero1 and numero3:
		segundomaior = numero2
	elif numero3 > numero1 and numero2:
		segundomaior = numero3

print 'Considerando os números %i, %i, %i e %i' % (numero1, numero2, numero3, numero4)
print 'O segundo menor número é %i' % segundomenor
print 'O segundo maior número é %i' % segundomaior

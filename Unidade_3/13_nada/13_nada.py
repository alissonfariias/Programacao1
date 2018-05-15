# coding: utf-8

numero1 = int(raw_input())
numero2 = int(raw_input())
numero3 = int(raw_input())
if numero1 == 13:
	soma = 0
	print soma
elif numero2 == 13:
	soma = numero1
	print soma
elif numero3 == 13:
	if numero1 + numero2 == 13:
		print 0
	else:
		soma = numero1 + numero2
		print soma
elif numero1 + numero2 + numero3 == 13:
	soma = 0
	print soma
else:
	soma = numero1 + numero2 + numero3
	print soma

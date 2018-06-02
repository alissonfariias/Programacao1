razao = float(raw_input())

criancas = 0
adultos = 0
peso_total = 0.0
while True:
	sequencia = raw_input().split()
	if sequencia[0] == "a":
		adultos += 1
		peso_total += float(sequencia[1])
	if sequencia[0] == "c":
		criancas += 1
		peso_total += float(sequencia[1])
	if criancas == 1 and adultos == 0 and razao >= 1:
		criancas -= 1
		peso_total -= float(sequencia[1])
		break
	if (criancas/adultos) >= razao:
		criancas -= 1
		peso_total -= float(sequencia[1])
		break
	if peso_total > 700:
		criancas -= 1
		peso_total -= float(sequencia[1])
		break

print 'Limite atingido'
print 'Elevador saiu com %i pessoas e %.2f kg.' % (criancas+adultos,peso_total)

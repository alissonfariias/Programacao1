# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 6	Questão: Cálculo de Seguro

def calcula_seguro(valor_veiculo,lista):
	
	idade = lista[0]
	status = lista[1]
	possui_cartao = lista[2]
	area_de_risco = lista[3]
	casa_ou_ap = lista[4]
	propria_ou_alugada = lista[5]
	uso_do_carro = lista[6]
	
	pontos = 0
	
	if idade <= 21:
		pontos += 20
	elif idade >= 22 and idade <= 30:
		pontos += 15
	elif idade >= 31 and idade <= 40:
		pontos += 12
	elif idade >= 41 and idade <= 60:
		pontos += 10
	elif idade > 60:
		pontos += 20
		
	if status == True:
		pontos += 10
	elif status == False:
		pontos += 20
	
	if possui_cartao == True:
		pontos += 20
	elif possui_cartao == False:
		pontos += 10
		
	if area_de_risco == True:
		pontos += 20
	elif area_de_risco == False:
		pontos += 10
	
	if casa_ou_ap == True:
		pontos += 20
	elif casa_ou_ap == False:
		pontos += 10
	
	if propria_ou_alugada == True:
		pontos += 10
	elif propria_ou_alugada == False:
		pontos += 20
	
	if uso_do_carro == 'Lazer':
		pontos += 20
	elif uso_do_carro == 'Trabalho':
		pontos += 10
	elif uso_do_carro == 'Misto':
		pontos += 20
	
	if pontos <= 80:
		risco = 'Risco Baixo'
	elif pontos > 80 and pontos <= 100:
		risco = 'Risco Medio'
	elif pontos > 100:
		risco = 'Risco Alto'
	
	if risco == 'Risco Baixo':
		valor_a_pagar = valor_veiculo / 100 * 10
	elif risco == 'Risco Medio':
		valor_a_pagar = valor_veiculo / 100 * 20
	elif risco == 'Risco Alto':
		valor_a_pagar = valor_veiculo / 100 * 30
	
	resultado = []
	resultado.append(pontos)
	resultado.append(risco)
	resultado.append(valor_a_pagar)
	return resultado

print calcula_seguro(2000.0, [21, True, True, True, True, True, 'Misto'])

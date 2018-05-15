# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2

veiculo = str(raw_input())
if veiculo == 'Automóvel utilitário':
	print 'Valor a pagar: R$ 11.40.'
elif veiculo == 'Ônibus':
	quant_eixos_onibus = float(raw_input())
	valor_onibus = quant_eixos_onibus * 11.40
	print 'Valor a pagar: R$ %.2f.' % valor_onibus
elif veiculo == 'Caminhão':
	quant_eixos_caminhao = float(raw_input())
	valor_caminhao = quant_eixos_caminhao * 9.60
	print 'Valor a pagar: R$ %.2f.' % valor_caminhao
elif veiculo == 'Motocicleta':
	print 'Valor a pagar: R$ 5.70.'
else:
	print 'Veículo não cadastrado.'

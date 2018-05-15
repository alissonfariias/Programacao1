# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Período: 2017.2
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# Unidade: 6	Questão: Diferença entre Dois Horários no Dia

def quanto_tempo(horario1, horario2):

	hora1 = int(horario1[0] + horario1[1])
	minuto1 = int(horario1[3] + horario1[4])
	hora2 = int(horario2[0] + horario2[1])
	minuto2 = int(horario2[3] + horario2[4])
	
	horas = hora2 - hora1
	minutos = minuto2 - minuto1
	
	if minutos < 0:
		minutos += 60
		horas -= 1
	
	return "%i hora(s) e %i minuto(s)" % (horas,minutos)

assert quanto_tempo("07:15", "09:18") == "2 hora(s) e 3 minuto(s)"

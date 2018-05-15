# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Unidade 4
# QUESTÃO: Campanha

gols_pro = 0
gols_contra = 0
vitorias = 0
empates = 0
derrotas = 0
vitorias_em_casa = 0
empates_em_casa = 0
derrotas_em_casa = 0
vitorias_fora = 0
empates_fora = 0
derrotas_fora = 0
for i in range(10):
	n = raw_input()
	if n[5] == 'c':
		gols = n[0]
		contra = n[2]
		gols_pro += int(gols)
		gols_contra += int(contra)
		if gols > contra:
			vitorias += 1
			vitorias_em_casa += 1
		elif gols < contra:
			derrotas += 1
			derrotas_em_casa += 1
		elif gols == contra:
			empates += 1
			empates_em_casa += 1		
	elif n[5] == 'f':
		gols = n[2]
		contra = n[0]
		gols_pro += int(gols)
		gols_contra += int(contra)
		if gols > contra:
			vitorias += 1
			vitorias_fora += 1
		elif gols < contra:
			derrotas += 1
			derrotas_fora += 1
		elif gols == contra:
			empates += 1
			empates_fora += 1

pontos = (vitorias * 3) + (empates * 1) + (derrotas * 0)
pontos_em_casa = (vitorias_em_casa * 3) + (empates_em_casa * 1) + (derrotas_em_casa * 0)
pontos_fora = (vitorias_fora * 3) + (empates_fora * 1) + (derrotas_fora * 0)


print '%iv, %ie, %id' % (vitorias,empates,derrotas)
print 'pontos: %i' % pontos
print 'saldo: %i (%i pro, %i contra)' % (gols_pro-gols_contra,gols_pro,gols_contra)
print 'pontos em casa: %i' % pontos_em_casa
print 'pontos fora: %i' % pontos_fora

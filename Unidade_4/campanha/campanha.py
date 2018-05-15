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
for i in range(10):
	n = raw_input()
	if n[5] == 'c':
		gols = n[0]
		contra = n[2]
		gols_pro += int(gols)
		gols_contra += int(contra)
		if gols > contra:
			vitorias += 1
		elif gols < contra:
			derrotas += 1
		elif gols == contra:
			empates += 1
	elif n[5] == 'f':
		gols = n[2]
		contra = n[0]
		gols_pro += int(gols)
		gols_contra += int(contra)
		if gols > contra:
			vitorias += 1
		elif gols < contra:
			derrotas += 1
		elif gols == contra:
			empates += 1

vitorias_em_casa = (vitorias * 3) + (empates * 1) + (derrota * 0)


print '%iv, %ie, %id' % (vitorias,empates,derrotas)
print 'pontos: %i' % gols_pro
print 'saldo: %i (%i pro, %i contra)' % (gols_pro-gols_contra,gols_pro,gols_contra)
print 'pontos em casa: %i' % vitorias_em_casa
print 'pontos fora: %i' % vitorias_fora

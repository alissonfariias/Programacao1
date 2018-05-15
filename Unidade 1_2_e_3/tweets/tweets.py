# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Tweets por Página
# Unidade: 2

quantidade_tweets = int(raw_input())

quantidade_paginas = quantidade_tweets / 400
tweets_perdidos = ((quantidade_tweets % 400) * 100) / 400

print 'Serão necessárias %d página(s) para visualizar os tweets.' % quantidade_paginas
print '%.1f%% dos tweets serão perdidos.' % tweets_perdidos

# coding: utf-8
# Aluno: Walisson Nascimento de Farias
# Matrícula: 117210716
# UFCG - Período: 2017.2
# Tweets por pagina

quantidade_tweets = int(raw_input())

quantidade_paginas = quantidade_tweets / 400
tweets_perdidos = quantidade_tweets % 400.0
porcentagem_tweets_perdidos = tweets_perdidos * 100.0 / quantidade_tweets

print "Serão necessárias %i página(s) para visualizar os tweets." % quantidade_paginas
print "%.1f%% dos tweets serão perdidos." % porcentagem_tweets_perdidos

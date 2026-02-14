def mediaGolsTime(time):
  totalGols = 0
  totalJogos = 0

  for jogador in time.jogadores:
      totalGols += jogador.gols
      totalJogos += jogador.jogos
  if totalJogos > 0:
    media = totalGols / totalJogos
  else:
     media = 0
  return(media)

def TotalGolsTimes(time):
  totalGols = 0
  for jogador in time.jogadores:
      totalGols += jogador.gols
  return(totalGols)

def TotalAssistTime(time):
  totalAssist = 0
  for jogador in time.jogadores:
      totalAssist += jogador.assistencias
  return(totalAssist)

def defineArtilheiro(time):
  gols = 0
  artilheiro = None
  for jogador in time.jogadores:
    if jogador.gols > gols:
      artilheiro = jogador
      gols = jogador.gols
  return(artilheiro)

def defineAssistente(time):
  assist = 0
  assistente = None
  for jogador in time.jogadores:
    if jogador.assistencias > assist:
      assistente = jogador
      assist = jogador.assistencias
  return(assistente)

def criterioRankingGeral(time):
   mediaGols = mediaGolsTime(time)
   totalAssist = TotalAssistTime(time)
   totalGols = TotalGolsTimes(time)

   pontuacao = (mediaGols * 100) + (totalAssist * 0.7) + (totalGols)

   return(pontuacao)

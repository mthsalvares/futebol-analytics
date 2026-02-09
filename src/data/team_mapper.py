from data.team import adicionaJogador

def associaJogadorTime(times,jogadores):
  countTime = 0
  countJogador = 0

  for time in times:
    for jogador in jogadores:
        if time.nome == jogador.time:
            adicionaJogador(times[countTime], jogadores[countJogador])
        countJogador += 1
    countTime += 1
    countJogador = 0
  return(times)
def mediaGolsJogos(Jogador):
  media = Jogador.gols / Jogador.jogos
  return(f'Média de gols/jogos: {media:.2f}')

def mediaAssistJogos(Jogador):
  media = Jogador.assistencias / Jogador.jogos
  return(f'Média de assist/jogos: {media:.2f}')
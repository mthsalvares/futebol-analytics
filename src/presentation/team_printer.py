from statistic.player_stats import *
from statistic.team_stats import *

def exibicaoTimes(times):
  for time in times:
    print(f'Time: {time.nome}') 
    print(f'Pais: {time.pais}') 
    print("") 
    print(f'Total de gols do {time.nome}: {TotalGolsTimes(time)}')
    print(f'Total de assistencias do {time.nome}: {TotalAssistTime(time)}')
    print(f'Média de gols por jogo: {mediaGolsTime(time):.2f}')
    print("") 
    artilheiro = defineArtilheiro(time)
    assistente = defineAssistente(time)

    if artilheiro is not None:
      print(f'Artilheiro: {artilheiro.nome} ({artilheiro.gols} gols)')
    if assistente is not None:
      print(f'Lider assistências: {assistente.nome} ({assistente.assistencias} assistencias)')
    print("---------------------------------")
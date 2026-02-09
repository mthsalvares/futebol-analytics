from statistic.player_stats import *

def exibicaoTimes(times):
  for time in times:
    print(f'Time: {time.nome}') 
    print(f'Pais: {time.pais}') 
    print("") 
    for jogador in time.jogadores: 
        print(f'Jogador: {jogador.nome}\n' 
              f'Gols: {jogador.gols}\n' 
              f'Assistências: {jogador.assistencias}') 
        print(mediaGolsJogos(jogador)) 
        print(mediaAssistJogos(jogador)) 
        print('\n')
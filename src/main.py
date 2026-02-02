from data.player import Jogador
from data.players_loader import *
from statistic.player_stats import *

def main():
    print("Sistema de Análise de Futebol iniciado ⚽")

if __name__ == "__main__":
    main()

'''jogador = Jogador('Luciano',579,166,45,4)

print(f'Jogador: {jogador.nome}\n'
      f'Gols: {jogador.gols}\n'
      f'Assistências: {jogador.assistencias}')

print(mediaGolsJogos(jogador))
print(mediaAssistJogos(jogador))'''

jogadores = []
jogadores = criaJogador()

for jogador in jogadores:
    print(f'Jogador: {jogador.nome}\n'
      f'Gols: {jogador.gols}\n'
      f'Assistências: {jogador.assistencias}')

    print(mediaGolsJogos(jogador))
    print(mediaAssistJogos(jogador))

    print('\n')


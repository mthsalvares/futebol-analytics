from data.player import Jogador
from data.players_loader import *
from statistic.player_stats import *
from data.team_loader import *
from data.team_mapper import *
from presentation.team_printer import *

def main():
    print("Sistema de Análise de Futebol iniciado ⚽")

if __name__ == "__main__":
    main()

times = criaTime()
jogadores = criaJogador()

times = associaJogadorTime(times, jogadores)

exibicaoTimes(times)


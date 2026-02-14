from data.player import Jogador
from data.players_loader import *
from statistic.player_stats import *
from data.team_loader import *
from data.team_mapper import *
from presentation.team_printer import *
from statistic.team_stats import *
from statistic.ranking_stats import *
from presentation.ranking_printer import *

def main():
    print("Sistema de Análise de Futebol iniciado ⚽")

if __name__ == "__main__":
    main()

times = criaTime()
jogadores = criaJogador()

times = associaJogadorTime(times, jogadores)

exibicaoTimes(times)
exibicaoRanking(rankingTime(times,TotalGolsTimes),'Total de Gols')
exibicaoRanking(rankingTime(times,mediaGolsTime), 'Media de Gols do Time')
exibicaoRanking(rankingTime(times,TotalAssistTime),'Total de Assistências')
exibicaoRanking(rankingTime(times,criterioRankingGeral), 'Score Geral')



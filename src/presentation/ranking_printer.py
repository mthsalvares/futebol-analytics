from statistic.ranking_stats import *

def exibicaoRanking(ranking, string):
  print(f'Ranking por {string}')
  for i,item in enumerate(ranking, start=1):
    print(f'{i} - {item["time"]} - {item["valor"]:.2f}')
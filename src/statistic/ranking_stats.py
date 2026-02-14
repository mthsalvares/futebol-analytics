from statistic.team_stats import *

def rankingTime(times,criterio):
  lista = []
  for time in times:
    valor = criterio(time)
    item = {"time":time.nome,"valor":valor}

    lista.append(item)
  
  lista.sort(key=lambda x: x['valor'], reverse=True)
  return(lista)
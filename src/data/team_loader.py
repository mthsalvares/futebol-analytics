import json
from data.team import *

def criaTime():

  with open('data/teams.json', 'r', encoding='utf-8') as teams_json:
    dados = json.load(teams_json)
    times = []

    for d in dados:
      times.append(Time(d['nome'],d['pais']))
    
    return(times)
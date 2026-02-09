import json
from data.player import Jogador

def criaJogador():
  with open('data/players.json', 'r', encoding='utf-8') as players_json:
    dados = json.load(players_json)

    jogadores = []
    for item in dados:
      jogadores.append(Jogador(item['nome'],item['time'],item['jogos'],item['gols'],item['assistencias'], item['titulos']))
    return(jogadores)

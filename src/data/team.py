class Time:
  def __init__(self, nome, pais):
    self.nome = nome
    self.pais = pais
    self.jogadores = []

def adicionaJogador(time,jogador):
  time = time.jogadores.append(jogador)
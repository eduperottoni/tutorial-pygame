from pygame.sprite import groupcollide

class LeitorColisao():
  def __init__(self, grupo_jogador, grupo_inimigo, grupo_arma):
    self.__grupo_jogador = grupo_jogador
    self.__grupo_arma = grupo_arma
    self.__grupo_inimigo = grupo_inimigo
    self.__mortes = 0

  def checar_colisao(self):
    if groupcollide(self.__grupo_arma, self.__grupo_inimigo, True, True):
      self.__mortes += 1
    return self.__mortes
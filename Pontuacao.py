from pygame import font

class Pontuacao():
  def __init__(self):
    self.__fonte = font.SysFont('comicsans', 50)
    self.__pontuacao = None

  def atualizar_pontuacao(self, qtd_mortes, superficie):
    self.__pontuacao = self.__fonte.render(
      f'Mortes: {qtd_mortes}',
      True,
      (255,255,255)
    )

    superficie.blit(self.__pontuacao, (20,20))
  
    
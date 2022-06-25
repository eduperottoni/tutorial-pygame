from Desenhavel import Desenhavel
from SpriteImage import SpriteImage

class Dunofausto(Desenhavel):
  def __init__(self, group_torradas):
    super().__init__('Images/dunofausto_small.png', 400, 100)
    self.__torradas = group_torradas
    self.__velocidade = 2

  def tacar_torradas(self):
    print(len(self.__torradas))
    if len(self.__torradas) < 15:
      self.__torradas.add(
        SpriteImage('Images/toast_small.png',*self.get_sprite().rect.center)
      )

  def mover_dir(self):
    self.get_sprite().rect.x += self.__velocidade

  def mover_esq(self):
    self.get_sprite().rect.x -= self.__velocidade

  def mover_cim(self):
    self.get_sprite().rect.y -= self.__velocidade
  
  def mover_bai(self):
    self.get_sprite().rect.y += self.__velocidade

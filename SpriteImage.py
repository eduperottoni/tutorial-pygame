
from pygame.sprite import Sprite
from pygame.image import load

class SpriteImage(Sprite):
  def __init__(self, image_path: str = 'Images/dunofausto_small.jpg', x_position: int = 0, y_position: int = 0):
    super().__init__()

    self.__image = load(image_path)
    self.__rect = self.__image.get_rect(
      center=(x_position, y_position)
    )
  
  def update(self):
    # self.kill() #Destroi o sprite
    self.mover_x(-0.1)
  
  @property
  def image(self) -> str:
    return self.__image
  
  @property
  def rect(self) -> object:
    return self.__rect
  
  def mover_x(self, value) -> None:
    self.__rect.x -= 0.1

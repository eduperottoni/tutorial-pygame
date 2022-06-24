from SpriteImage import SpriteImage

class Desenhavel:
  def __init__(self, image_path, x_position: int = 0, y_position: int = 0):
    self.__sprite = SpriteImage(image_path, x_position, y_position)

  def get_sprite(self):
    return self.__sprite
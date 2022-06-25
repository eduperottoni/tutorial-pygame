from Desenhavel import Desenhavel
from random import randint

class Inimigo(Desenhavel):
  def __init__(self):
    super().__init__('Images/inimigo_1.png', 800, randint(20,580))
  


  

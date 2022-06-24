import pygame
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE

class LeitorEventos():
  def __init__(self):
    pass
  
  def ler_evento(self):
    for evento in event.get(): #Retorna uma lista de events
      if evento.type ==  QUIT:
        pygame.quit()

      if evento.type == KEYUP:
        if evento.key == K_SPACE:
          dunofausto.tacar_torradas()

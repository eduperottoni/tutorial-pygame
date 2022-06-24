import pygame
from pygame import display

from pygame.image import load, save
from pygame.transform import scale

from pygame.sprite import Group, GroupSingle

from Desenhavel import Desenhavel
from Torrada import Torrada
from Inimigo import Inimigo
from LeitorEventos import LeitorEventos

pygame.init()

tamanho_tela = (800, 600)

superficie = display.set_mode(
  size=tamanho_tela,
  flags=0,
  depth=0,
  display=0,
  vsync=0 #tira sincronização do tipo raster
)
display.set_caption(
  'Testando o title da tela'
)

fundo = scale(
  load('Images/space.jpg'),
  tamanho_tela
)



dunofausto = Desenhavel('Images/dunofausto_small.png')
torrada = Torrada()
inimigo = Inimigo()

grupo_inimigos = GroupSingle(inimigo.get_sprite())
grupo_torradas = Group()
grupo_duno = GroupSingle(dunofausto.get_sprite())


leitorevento = LeitorEventos()

while True:
  superficie.blit(
    fundo, #Imagem
    (0,0) #Posição
  )

  leitorevento.ler_evento()

  grupo_duno.draw(superficie)
  grupo_inimigos.draw(superficie)
  grupo_torradas.draw(superficie)

  grupo_duno.update()
  grupo_inimigos.update()
  grupo_torradas.update()

  display.update()
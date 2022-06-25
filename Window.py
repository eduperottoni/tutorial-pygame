import pygame
from pygame import display
from pygame.time import Clock

from pygame.image import load, save
from pygame.transform import scale

from pygame.sprite import Group, GroupSingle

from Desenhavel import Desenhavel
from Pontuacao import Pontuacao
from Torrada import Torrada
from Inimigo import Inimigo
from LeitorEventos import LeitorEventos
from Dunofausto import Dunofausto
from LeitorColisao import LeitorColisao

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


grupo_inimigos = Group(Inimigo().get_sprite())
grupo_torradas = Group()

clock = Clock()

dunofausto = Dunofausto(grupo_torradas)
grupo_duno = GroupSingle(dunofausto.get_sprite())

leitoreventos = LeitorEventos()
leitorcolisao = LeitorColisao(grupo_duno, grupo_inimigos, grupo_torradas)
pontuacao = Pontuacao()

round = 0
mortes = 0
while True:

  clock.tick(120)

  round += 1
  if round % 120 == 0:
    if mortes < 20:
      grupo_inimigos.add(Inimigo().get_sprite()) 
    for _ in range(int(mortes/20)):
      grupo_inimigos.add(Inimigo().get_sprite())

  superficie.blit(
    fundo, #Imagem
    (0,0) #Posição
  )
  pontuacao.atualizar_pontuacao(mortes, superficie)

  evento = leitoreventos.ler_evento()
  mortes = leitorcolisao.checar_colisao()

  if evento == "fechar":
    pygame.quit()
  elif evento == "atacar":
    dunofausto.tacar_torradas()
  elif evento == "mover-dir":
    dunofausto.mover_dir()
  elif evento == "mover-esq":
    dunofausto.mover_esq()
  elif evento == "mover-up":
    dunofausto.mover_cim()
  elif evento == 'mover-down':
    dunofausto.mover_bai()    

  

  grupo_duno.draw(superficie)
  grupo_inimigos.draw(superficie)
  grupo_torradas.draw(superficie)

  grupo_duno.update()
  grupo_inimigos.update(0.1, "esq")
  grupo_torradas.update(1, "dir")

  display.update()
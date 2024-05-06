# Constantes
WIDTH = 800
HEIGHT = 600

class Nave:
  def __init__(self,vida,poder,posição_nave,posição_tiro,imagem_nave,imagem_tiro):
    self.vida = vida
    self.poder = poder
    self.posição_nave = posição_nave
    self.posição_tiro = posição_tiro
    self.imagem_nave = imagem_nave
    self.imagem_tiro = imagem_tiro

  def atacar(self):
    pass

  def mover(event):
    pass

  def limite(self):
    pass

  def show(self):
    pass


#CRIANDO O GATO

class gato():
  def __init__(self, cor):
    self.cor = cor

  def como(self):
    print(self.cor)

nao = gato(branco)
nao.como()

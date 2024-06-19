class Conta:
  
  def __init__(self)->None:

    self.nome = ""
    self.pontos = 0


  def set_nome(self,nome:str)->None:
    self.nome = nome

    
  def set_pontos(self,pontos:int)->None:
    self.pontos = pontos


class Cadastro:

  def __init__(self)->None:

    self.contas = []

  def registrar(self,conta)->None:

    if self.confirmar_conta(conta):
      self.contas.append(conta)
    else:
      pass
    
  def confirmar_conta(self,conta)->None:

    for conta_aux in self.contas:
      if conta.nome == conta_aux.nome:
        return False
    return True    

  def salvar_banco_dados(self)->None:

    with open("test.txt","w") as arq:
      for conta in self.contas:
        arq.write(f"{conta.nome} : {conta.pontos}\n")

  
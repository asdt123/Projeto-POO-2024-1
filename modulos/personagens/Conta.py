import sqlite3


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

    # Conectar ou criar banco de dados
    conn = sqlite3.connect('jogadores.db')
    cursor = conn.cursor()

        # Criar a tabela com as colunas de nome e pontuação
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        pontuacao INT
       )
    ''')

    # Confirmar as mudanças
    conn.commit()
    for conta in self.contas:
      print(conta.nome, conta.pontos)
      cursor.execute('''
      INSERT INTO jogadores (nome, pontuacao) VALUES (?, ?)
      ''', (conta.nome, conta.pontos))

  
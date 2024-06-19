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

      self.contas.append(conta)

  def salvar_banco_dados(self, num_players)->None:

    # Conectar ou criar banco de dados
    conn = sqlite3.connect('jogadores.db')
    cursor = conn.cursor()
        # Criar a tabela com as colunas de nome e pontuação
    if num_players == 1:
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS solo (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL,
          pontuacao INT
        )
      ''')
      conn.commit()
      for conta in self.contas:
        cursor.execute('''
        INSERT INTO solo (nome, pontuacao) VALUES (?, ?)
        ''', (conta.nome, conta.pontos))

    else:
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS dupla (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL,
          pontuacao INT
        )
      ''')
      conn.commit()
      for conta in self.contas:
        cursor.execute('''
        INSERT INTO dupla (nome, pontuacao) VALUES (?, ?)
        ''', (conta.nome, conta.pontos))

    # Confirmar as mudanças

    conn.commit()
    self.contas.clear()

    
  
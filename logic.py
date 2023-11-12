import random

class Board:
  def __init__(self):
    self._rows = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

  def __str__(self):
    s = '-------\n'
    for row in self._rows:
      for cell in row:
        s = s + '|'
        if cell == None:
          s=s+' '
        else:
          s=s+cell
      s = s + '|\n-------\n'
    return s

  def get(self, x, y):
    return self._rows[x][y]

  def set(self, x, y, value):
    self._rows[x][y] = value


class Game:
  def __init__(self, playerX, playerO):
    self._board = Board()
    self._playerX = playerX
    self._playerO = playerO
    self._current_player = playerX

  def other_player(self):
    if self._current_player == self._playerX:
      self._current_player = self._playerO
    else:
      self._current_player = self._playerX
  
  def game_ends(self):
    for i in range(0, 3):
      if self._board.get(i, 0) != None and self._board.get(i, 0) == self._board.get(i, 1) == self._board.get(i, 2):
        print(self._board.get(i, 0), ' Won')
        return True
        
    for i in range(0, 3):
      if self._board.get(0, i) != None and self._board.get(0, i) == self._board.get(1, i) == self._board.get(2, i):
        print(self._board.get(0, i), ' Won')
        return True
        
    if self._board.get(1, 1) != None and (self._board.get(0, 0) == self._board.get(1, 1) == self._board.get(2, 2) or self._board.get(2, 0) == self._board.get(1, 1) == self._board.get(0, 2)):
      print(self._board.get(1, 1), ' Won')
      return True
      
    for row in range(0, 3):
      for col in range(0, 3):
        if self._board.get(row, col) == None:
          return False
        
    print('Draw')
    return True

  def run(self):
    while not self.game_ends():
      if self._current_player == self._playerX:
        turn = 'X'
      else:
        turn = 'O'
      print(turn, ' turn')
      self._current_player.make_move(self._board, turn)
      print(self._board)
      self.other_player()

class Human:
  def make_move(self, board, turn):
    try:
        row = int(input("Input row index: "))
        col = int(input("Input col index: "))
    except:
        raise ValueError('Input invalid, must be an int.')
    else:
        if row < 0 or row > 2 or col < 0 or col > 2:
            raise ValueError('Input invalid, should >=0 and <=2.')
        if board.get(row, col) != None:
            raise ValueError('Input invalid, the place already has input.')
        board.set(row, col, turn)

class Bot:
  def make_move(self, board, turn):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while board.get(x, y) != None:
      x = random.randint(0, 2)
      y = random.randint(0, 2)
    board.set(x, y, turn)


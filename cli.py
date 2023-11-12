from logic import Human
from logic import Bot
from logic import Game


if __name__ == '__main__':
  playerX = Human()
  playerO = Bot()
  game = Game(playerX, playerO)
  game.run()

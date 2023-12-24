from Game import *

# Create game object and set debug
game = Game()
game.debug = False  # При дебаге выводиться поле врага и больше информации


if __name__ == '__main__':
    game.start()

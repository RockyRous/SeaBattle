from Game import *

# Create game object and set debug
game = Game()
game.debug = True

# используем при отладке @game.clear_screen

welcome_message()

if __name__ == '__main__':
    game.start()  # Выводим приветствие игры и производим настройку
    # Настраиваем противника (возможно настраиваем поле, корабли и др параметры)

    # Начинаем игровой цикл
    while True:
        game.print_ui()  # ввыводим весь интерфейс

        game.setup_ship()  # Раставляем своё поле с кораблями
        game.setup_ship(ai, auto)  # Раставляем поле противника

        game.print_ui()  # Обновляем юи

        player_step = True
        while player_step:
            player_step = game.step_player()  # Делаем выстрел на поле противника
            # Если попали - ходим еще, если ошибка - ходим еще.
            # Ход закончен = выходим из цикла

        game.is_win()  # Проверяем факт победы
        game.print_ui()  # Обновляем юи

        game.step_ai()  # Ход аи

        game.is_win()  # Проверяем факт победы
        game.print_ui()  # Обновляем юи





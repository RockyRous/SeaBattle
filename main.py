from Game import *

# Create game object and set debug
game = Game()
game.debug = True


welcome_message()

if __name__ == '__main__':
    game.start()  # Выводим приветствие игры и производим настройку
    # Определяем какие найстройки мне нужны
    # Настраиваем противника (возможно настраиваем поле, корабли и др параметры)


    # Начинаем цикл растановки поля кораблями
    game.setup_ship()

    game.print_ui()  # ввыводим весь интерфейс

    # # Имеем настроеную игру и раставленные доски для игры. т.е. полная подготовка завершена.
    # # Начинаем игровой цикл
    # while True:
    #
    #     game.step_player()  # Игрок делает ход
    #     game.print_ui()
    #     game.is_win()  # Проверяем факт победы
    #
    #     game.step_ai()  # Ход ИИ
    #     game.print_ui()
    #     game.is_win()





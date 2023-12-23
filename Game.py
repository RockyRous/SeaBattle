"""
В данном файле описана основная логика игры
"""
import random
from game_errors import *


def welcome_message():
    """ Print welcome message at startup """
    print('How to play Sea Battle... (soon)')


class Dot:
    def __init__(self, x: int, y: int, value='0'):
        self.x, self.y = x, y
        self.value = value
        self.free = True  # Used to install ships
    # Имеет одно из значений (Пусто\мимо\попал\корабль)

    # Использует маг методы сравнения
    # __eq__() – для равенства ==
    # __ne__() – для неравенства !=
    # Где вызывает определеные ошибки, которые будут отрабатываться


class Ship:
    """ Ship data """
    def __init__(self, size: int, pivot_dot: Dot, rotate: int = 0):
        self.size = size
        self.pivot_dot = pivot_dot
        # self.x, self.y = x, y  # pivot point
        self.rotate = rotate
        self.hp = size


class Field:
    def __init__(self, hide: bool, name: str) -> None:
        # Размер игрового поля
        self.x = self.y = 6
        # Его инициализация
        self.board = [[Dot(i, j) for i in range(self.x)] for j in range(self.y)]
        # board[y][x]!!!!

        self.name = name  # Кому принадлежит поле
        self.hide = hide  # Отображение поля (не используется :С )
        self.active_ships = 0  # Кол-во активных кораблей
        self.ships = []  # Обьекты принадлежащих кораблей

        # Плохое место хранения, но удобнее пока нет
        # list:[list[name: str, size: int]]
        self.ship_list = [['Фрегат (3)', 3], ['Корвет (2)', 2], ['Корвет (2)', 2], ['Лодка (1)', 1],
                          ['Лодка (1)', 1], ['Лодка (1)', 1], ['Лодка (1)', 1]]

    def out(self, x: int, y: int) -> bool:
        """
        Проверяет, выходит ли точка за пределы поля
        """
        if x in range(0, self.x) and y in range(0, self.y):
            return True
        return False

    def get_ship_dots(self, ship: Ship) -> list[Dot] or bool:
        """ return all dots in ship or False! """
        dots_list = []
        x = ship.pivot_dot.x
        y = ship.pivot_dot.y
        dots_list.append(self.board[y][x])

        if ship.rotate == 0:  # Длина = 1
            return dots_list

        elif ship.rotate == 1:  # Слева - направо
            for i in range(ship.size - 1):
                x += 1
                if x > 5:  # Можно было сделать через self.out, но выходит больше действий
                    er02()
                    return False
                dots_list.append(self.board[y][x])

        elif ship.rotate == 2:  # Сверху - вниз
            for i in range(ship.size - 1):
                y += 1
                if y > 5:
                    er02()
                    return False
                dots_list.append(self.board[y][x])

        elif ship.rotate == 3:  # Справа - влево
            for i in range(ship.size - 1):
                x -= 1
                if x < 0:
                    er02()
                    return False
                dots_list.append(self.board[y][x])

        elif ship.rotate == 4:  # Снизу - вверх
            for i in range(ship.size - 1):
                y -= 1
                if y < 0:
                    er02()
                    return False
                dots_list.append(self.board[y][x])
        else:
            raise GameError(f'Что-то пошло не так... get_ship_dots -> ship.rotate?? {ship.rotate} ')
        return dots_list

    def contour(self, dot: Dot) -> None:
        """ Change free status Dot + neighboring Dot """
        self.board[dot.y][dot.x].free = False
        if dot.x + 1 <= 5:
            self.board[dot.y][dot.x + 1].free = False
        if dot.x - 1 >= 0:
            self.board[dot.y][dot.x - 1].free = False
        if dot.y + 1 <= 5:
            self.board[dot.y + 1][dot.x].free = False
        if dot.y - 1 >= 0:
            self.board[dot.y - 1][dot.x].free = False

    def add_ship(self, ship: Ship):
        """ Перед вызовом проверить возможности размещения и создать обозначить класс """

        # Размещение
        dots_list = self.get_ship_dots(ship)
        for dot in dots_list:
            dot.value = 'T'
            self.contour(dot)

        # Добавление активного судна
        self.active_ships += 1
        self.ships.append(ship)

        print('Корабль успешно размещен')

    def may_add_ship(self, ship: Ship) -> bool:
        """ Check free Dot for ship """
        if not ship.pivot_dot.free:  # Дот заблокирован
            er01(ship.pivot_dot)
            return False
        if ship.size > 1:  # Корабль занимает больше 1 дота
            dots_list = self.get_ship_dots(ship)  # Получаем список всех дотов корабля
            if dots_list == False:
                return False
            for dot in dots_list:
                if not dot.free:
                    er03(dot)
                    return False
        return True

    # Функции деплой и автодеплой шипс можно обьеденить повторяющийся код
    def deploy_ships(self):
        """ Ручная реализация кораблей на поле """
        """
        Создаем шип и даем ему пивот и ротейт, потом юзаем этот шип
        
        Надо иметь список размещаемых кораблей и начинать с больших
        выводим инструкцию (print_help_deploy)
        Cпрашиваем куда пивот поинт и какую ротацию
        Как и адд_шип, надо определять свободность клеток и наличие их на поле (may add ship)
        Если всё ок - выполняем адд шип, затем работаем со следующим
        Если корабли кончились - заканчиваем
        """

        for current_ship in self.ship_list:
            input_x, input_y, input_rotate, new_ship = None, None, None, None

            for y in self.board:
                print([f'x={dot.x}|y={dot.y}|value={dot.value}|free={dot.free}' for dot in y])

            # Цикл валидации судна целиком
            no_valid_ship = True
            while no_valid_ship:

                # Вывод подсказки для ввода
                print(f'Нужно указать координаты начальной точки корабля: {current_ship[0]}\n'
                      f'Введите через пробел сначала координату Х, потом координату У')
                if current_ship != '4':  # Если корабль длинее чем 1, инфа по повороту
                    print(f'Потом поворот судна (в какую сторону будет распологаться его остальная часть от начала)'
                          f'1 - это направо, 2 - вниз, 3 - влево, 4 - вверх')

                # Цикл валидации инпута
                no_valid_input = True
                while no_valid_input:
                    info = input().split()
                    input_x = int(info[0])
                    input_y = int(info[1])
                    input_rotate = int(info[2])
                    print(f'x = {input_x} y = {input_y} rotate = {input_rotate}')
                    if self.out(input_x, input_y):  # Если ячейка в пределах доски
                        if self.board[input_y][input_x].free:  # Если ячейка свободна
                            if 1 <= input_rotate <= 4:
                                no_valid_input = False
                            else:
                                print('Поворот 1-4!')
                        else:
                            print(f'Ячейка x:{input_x} y:{input_y} занята')
                    else:
                        game_errors.er04()


                ship_pivot_dot = self.board[input_y][input_x]  # Вызываем Dot этих координат

                # Обьявляем судно с полученными данными
                if current_ship[1] != 1:  # Если корабль длиннее чем 1
                    new_ship = Ship(current_ship[1], ship_pivot_dot, input_rotate)
                else:
                    new_ship = Ship(current_ship[1], ship_pivot_dot)

                # Можем ли расположить всё судно?
                if self.may_add_ship(new_ship):  # Функция обрабатывает все ошибки
                    no_valid_ship = False
            self.add_ship(new_ship)

    # Функции деплой и автодеплой шипс можно обьеденить повторяющийся код
    def auto_deploy_ships(self):
        """ automatic deploy ship """
        for current_ship in self.ship_list:
            input_x, input_y, input_rotate, new_ship = None, None, None, None
            # Цикл валидации судна целиком
            no_valid_ship = True
            while no_valid_ship:

                # Цикл валидации инпута
                no_valid_input = True
                while no_valid_input:
                    # info = input().split()

                    input_x = random.randint(0, 5)
                    input_y = random.randint(0, 5)
                    input_rotate = random.randint(1, 4)
                    if self.board[input_y][input_x].free:  # Если ячейка свободна идём дальше
                        no_valid_input = False

                ship_pivot_dot = self.board[input_y][input_x]  # Вызываем Dot этих координат

                # Обьявляем судно с полученными данными
                if current_ship[1] != 1:  # Если корабль длиннее чем 1
                    new_ship = Ship(current_ship[1], ship_pivot_dot, input_rotate)
                else:
                    new_ship = Ship(current_ship[1], ship_pivot_dot)

                # Можем ли расположить всё судно?
                if self.may_add_ship(new_ship):  # Функция обрабатывает все ошибки
                    no_valid_ship = False

            self.add_ship(new_ship)

    def shot(self, x: int, y: int) -> str:
        return 'Выстрел произведен, вы попали'
        # return 'Выстрел произведен, вы не попали'


class Player:
    """
    Будущий родитель игрока и ИИ

    Имеет своё поле
    имеет доску противника

    ask - where to shoot (переопределяется в дочерках)
    move - стреляем и отрабатываем ошибки

    функция рандомного выбора дота в который не стреляли
    """


class User(Player):
    """
    переопределяем аск
    Возможность выбора рандомного выстрела
    """


class PlayerAI(Player):
    """
    Переопределяем аск
    рандом по полю

    Если попали и не убили -
    """


class Game:
    """
    Main game class.
    Здесь высокоуровневая логика ссылающаяся на низкоуровневую (и интерфейс)
    """

    def __init__(self, debug: bool = False) -> None:
        self.debug = debug  # При дебаге хочу выводить поле противника себе и мб еще что
        self.last_action = None  # Последнее событие для вывода в интерфейсе
        self.player_field = Field(hide=True, name='Player')  # Можно сделать ввод своего имени
        self.ai_field = Field(hide=True, name='AI')

    def start(self) -> None:
        """ Start the game. """
        a = f'Welcome to Sea Battle'
        print(a)
        # Определяем какие найстройки мне нужны
        # Напимер ии или что-то еще, пока просто привет

        self.setup_ship()  # Расставляем корабли
        self.print_ui()  # выводим весь интерфейс

        # Начинаем игровой цикл
        while True:
            self.step_player()  # Игрок делает ход
            self.print_ui()
            self.is_win(self.ai_field)  # Проверяем факт победы

            self.step_ai()  # Ход ИИ
            self.print_ui()
            self.is_win(self.player_field)

    def setup_ship(self) -> None:
        """
        Вывод описания
        Вопрос автодеплоя
            автодеплой
            Ручная реализация
        Автодеплой ии
        """

        query = (f'Вы можете расставить корабли на поле самостоятельно\n'
                 f'Или воспользоваться случайной растановкой.\n'
                 f'Введите:\n'
                 f'1 - для ручной установки.\n'
                 f'2 - для автоматической установки')
        print(query)

        input_start = True
        while input_start:
            try:
                c = input()
                if c == '1':
                    self.player_field.deploy_ships()
                    input_start = False
                elif c == '2':
                    self.player_field.auto_deploy_ships()
                    input_start = False
                else:
                    raise GameError('Ошибка 1/2 Введите только 1 или 2')
            except GameError as ge:
                print(ge)

        # Авторазмещение поля противника
        self.ai_field.auto_deploy_ships()

    def step_player(self) -> None:
        """
        Обращаемся к классу игрока
        1 - инпут хода игрока + описание что делать
        2 - валидация хода
        3 - выполнение хода (стрельба -> результат) (должен возвращаться бул + данные)
        4 - повтор в зависимости от результата
        """

    @staticmethod  # Если не будем использовать стату
    def is_win(field: Field) -> None:
        """ win or None """
        # Получаем поле проигравшего
        if field.active_ships == 0:
            if field.name == 'AI':
                print('Ура победа! Вы одолели эту консервную банку! Вы молодец!')
            else:
                print('О нет! Технологии вас одолели! :С')
        """
        Получаем боард, проверяем кол-во активных кораблей на доске
        Если 0 - то обьявляем победу 
        
        Отдельная тут логика - победа.
        Пишем кто выйграл и предлагаем начать новую игру или закрыть игру.
        """

    def step_ai(self) -> None:
        """
        Обращаемся к классу ИИ
        1 - Запуск рандома и его валидация
        2 - выполнение хода (должен возвращаться бул + данные)
        3 - при попадании отработка логики (продолжение хода)
        """

    # ================================================
    #                   Interface
    # ================================================

    def print_message(self, last_action: str) -> None:
        """ print last message """
        if last_action is not None:
            query = (f'****************************'
                     f'{last_action}'
                     f'****************************')
            print(query)

    def print_fields(self) -> None:
        if self.debug:
            for y in self.player_field.board:
                print([f'x={dot.x}|y={dot.y}|value={dot.value}|free={dot.free}' for dot in y])
            print('')
            for y in self.ai_field.board:
                print([f'x={dot.x}|y={dot.y}|value={dot.value}|free={dot.free}' for dot in y])
        else:
            for y in self.player_field.board:
                print([f'{dot.value}' for dot in y])
            print('')
            for y in self.ai_field.board:
                print([f'{dot.value}' for dot in y])
        # выводим поле врага форматируя символы

    def print_ui(self) -> None:
        """
        Выводим клевый интерфейс:
        1. Производим очистку интерфейса (если без дебага)
        2. Выводим ласт экшн
        3. Выводим доски
        """
        #
        self.print_fields()




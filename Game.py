"""
В данном файле описана основная логика игры
"""
import random
import game_errors


def welcome_message():
    """ Print welcome message at startup """
    print('Hello in SeaBattle')


# def step(fn, game):
#     """
#     Decorator
#     print ui
#     func
#     is win?
#     """
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         game.print_ui()  # ввыводим интерфейс
#         game.is_win()  # Проверяем факт победы
#         return result
#     return wrapper


class Dot:
    def __init__(self, x: int, y: int, value='0'):
        self.x, self.y = x, y
        self.value = value
        self.free = True
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

        # Имя корабля?
        # Можно сделать генератор дающий имя и поставить его в стандарт переменной


class Field:
    def __init__(self, hide: bool):
        # Размер игрового поля
        x = y = 6
        # Его инициализация
        self.board = [[Dot(i, j) for i in range(x)] for j in range(y)]
        # board[y][x]!!!!

        self.hide = hide  # Отображение поля
        self.active_ships = 0  # Кол-во активных кораблей
        self.ships = []  # Обьекты принадлежащих кораблей

        # list:[list[name: str, size: int], list[name: str, size: int]...] Надо сделать отдельно от класса
        self.ship_list = [['3', 3], ['2', 2], ['2', 2], ['1', 1], ['1', 1], ['1', 1], ['1', 1]]

    @staticmethod
    def out(x, y) -> bool:
        """
        Проверяет, выходит ли точка за пределы поля
        """
        if x in range(0, 6) and y in range(0, 6):
            return True
        return False

    def get_ship_dots(self, ship: Ship) -> list[Dot] or bool:
        """ return all dots in ship """
        dots_list = []
        x = ship.pivot_dot.x
        y = ship.pivot_dot.y
        dots_list.append(self.board[y][x])

        if ship.rotate == 0:  # Длина = 1
            return dots_list

        elif ship.rotate == 1:  # Слева - направо
            for i in range(ship.size - 1):
                x += 1
                if x > 5:
                    game_errors.er02()
                    return False
                dots_list.append(self.board[y][x])

        elif ship.rotate == 2:  # Сверху - вниз
            for i in range(ship.size - 1):
                y += 1
                if y > 5:
                    game_errors.er02()
                    return False
                dots_list.append(self.board[y][x])

        elif ship.rotate == 3:  # Справа - влево
            for i in range(ship.size - 1):
                x -= 1
                if x < 0:
                    game_errors.er02()
                    return False
                dots_list.append(self.board[y][x])

        elif ship.rotate == 4:  # Снизу - вверх
            for i in range(ship.size - 1):
                y -= 1
                if y < 0:
                    game_errors.er02()
                    return False
                dots_list.append(self.board[y][x])
        else:
            print('Что-то пошло не так... get_ship_dots -> ship.rotate??')
            print(ship.rotate)
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
            game_errors.er01(ship.pivot_dot)
            return False
        if ship.size > 1:  # Корабль занимает больше 1 дота
            dots_list = self.get_ship_dots(ship)  # Получаем список всех дотов корабля
            if dots_list == False:
                return False
            for dot in dots_list:
                # if not self.out(dot.x, dot.y):
                #     game_errors.er02(dot)
                #     return False
                if not dot.free:
                    game_errors.er03(dot)
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
    автодеплой кораблей
    ask - where to shoot (переопределяется в дочерках)
    move - стреляем и отрабатываем ошибки
    """


class User(Player):
    """
    переопределяем аск

    """





class Game:
    """
    Main game class.
    Здесь высокоуровневая логика ссылающаяся на низкоуровневую (на другие классы)
    """

    def __init__(self, debug: bool = False):
        self.debug = debug  # При дебаге хочу выводить поле противника себе и мб еще что
        self.last_action = None  # Последнее событие для вывода в интерфейсе
        self.player_field = Field(hide=True)
        self.ai_field = Field(hide=True)

    def start(self):
        """ Welcome and settings """
        a = f'Welcome to Sea Battle'
        print(a)
        # Определяем какие найстройки мне нужны
        # Напимер ии или что-то еще, пока просто привет

    def setup_ship(self):
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
                    print('Ошибка 1/2 Введите только 1 или 2')
            except:
                print('Ошибка try Введите только 1 или 2 (возможно проблема глубже)')

        # Авторазмещение поля противника
        self.ai_field.auto_deploy_ships()

    def step_player(self):
        """
        1 - инпут хода игрока + описание что делать
        2 - валидация хода
        3 - выполнение хода (стрельба -> результат) (должен возвращаться бул + данные)
        4 - повтор в зависимости от результата
        """

    def is_win(self):
        """ win or None """
        """
        Производим проверку отсутствия живых кораблей у досок
        Наверное передаем боард
        
        Если вин - то логика завершения игры
        """

    def step_ai(self):
        """
        1 - Запуск рандома и его валидация
        2 - выполнение хода (должен возвращаться бул + данные)
        3 - при попадании отработка логики (продолжение хода)
        """

    def print_message(self, last_action: str) -> None:
        """ print last message """
        if last_action is not None:
            query = (f'****************************'
                     f'{last_action}'
                     f'****************************')
            print(query)

    def print_fields(self, debug: bool, player_field: Field, ai_field: Field) -> None:
        if debug:
            for y in player_field.board:
                print([f'x={dot.x}|y={dot.y}|value={dot.value}|free={dot.free}' for dot in y])
            print('')
            for y in ai_field.board:
                print([f'x={dot.x}|y={dot.y}|value={dot.value}|free={dot.free}' for dot in y])
        else:
            for y in player_field.board:
                print([f'{dot.value}' for dot in y])
            print('')
            for y in ai_field.board:
                print([f'{dot.value}' for dot in y])
        # выводим поле врага форматируя символы

    def print_ui(self):
        """
        Используем местный класс интерфейс.
        Выводим клевый интерфейс:
        описание последнего события (в идеале окно с логом но кто мы такие делать это в консоли)
        своя доска и доска противника всё под форматированием
        """
        # При дебаге - выводим поле врага открытым
        self.print_fields(True, self.player_field, self.ai_field)


            # Функцию очистки кмд

    #
    # def clear_screen():  # будет декоратором

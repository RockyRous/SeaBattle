"""
В данном файле описана основная логика игры
"""
def welcome_message():
    """ Print welcome message at startup """
    print('Hello in SeaBattle')


class Ship:
    """ Ship data """
    def __init__(self, size: int, x: int, y: int, rotate: int):
        self.size = size
        self.x, self.y = x, y  # pivot point
        self.rotate = rotate
        self.hp = size
    """
    Принадлежит полю (или игроку?)
    """


class Dot:
    def __init__(self, value = 0):
        self.value = value
        self.free = True
    # Имеет одно из значений (Пусто\мимо\попал\корабль)


    # Использует маг методы сравнения
    # __eq__() – для равенства ==
    # __ne__() – для неравенства !=
    # Где вызывает определеные ошибки, которые будут отрабатываться


class Field:
    def __init__(self, hide: bool):
        # Размер игрового поля
        x = y = 6
        # Его инициализация
        self.board = [[Dot() for i in range(x)] for i in range(y)]

        self.hide = hide  # Отображение поля
        self.active_ships = 0  # Кол-во активных кораблей

    def contour(self, x,y) -> None:
        """ Change free status Dot + neighboring Dot """
        """ Думаю тут + add_ship, можно еще оптимизировать """
        self.board[x][y].free = False
        self.board[x+1][y].free = False
        self.board[x-1][y].free = False
        self.board[x][y+1].free = False
        self.board[x][y-1].free = False

    def add_ship(self, ship: Ship) -> str:
        """ Перед вызовом проверить возможности размещения и создать обозначить класс """

        # Размещение
        if ship.rotate == 1:  # Слева - направо
            for i in range(ship.size):
                x = ship.x + i
                self.board[x][ship.y].value = 'T'
                self.contour(x, ship.y)
        elif ship.rotate == 2:  # Сверху - вниз
            for i in range(ship.size):
                y = ship.y - i
                self.board[ship.x][y].value = 'T'
                self.contour(ship.x, y)
        elif ship.rotate == 3:  # Справа - влево
            for i in range(ship.size):
                x = ship.x - i
                self.board[ship.x - i][ship.y].value = 'T'
                self.contour(x, ship.y)
        elif ship.rotate == 4:  # Снизу - вверх
            for i in range(ship.size):
                y = ship.y + i
                self.board[ship.x][y].value = 'T'
                self.contour(ship.x, y)

        # Добавление активного судна
        self.active_ships += 1

        return 'Корабль успешно размещен'

    def may_add_ship(self) -> bool:
        """ Check free Dot for ship """

    def print_help_deploy:
        print('Так-вот-так, туда-сюда')

    def deploy_ships(self):
        """ Ручная реализация кораблей на поле """
        """
        Надо иметь список размещаемых кораблей и начинать с больших
        выводим инструкцию (print_help_deploy)
        Cпрашиваем куда пивот поинт и какую ротацию
        Как и адд_шип, надо определять свободность клеток и наличие их на поле (may add ship)
        Если всё ок - выполняем адд шип, затем работаем со следующим
        Если корабли кончились - заканчиваем
        """

    def auto_deploy_ships(self):
        """ automatic deploy ship """



    """
    ?????? Метод out, который для точки(объекта класса Dot) возвращает True, если
    точка выходит за пределы поля, и False, если не выходит.
    """

    def shot(self, x: int,y: int) -> str:
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


class Interface:
    def print_fields():

    # выводим своё поле
    # выводим поле врага форматируя символы
    def print_message():
    # use last_action


class Game:
    def __init__(self, debug=False):
        self.debug = debug  # При дебаге хочу выводить поле противника себе и мб еще что
        self.last_action = None  # Последнее событие для вывода в интерфейсе
    """
    Тут должны дергаться все ниточки в остальных классах

    Генерация случайной доски (рандом плейс шип)
    Принт инструкции
    определение проигравшего
    старт игры
    смена игрока
    """
    def start(self):
    def setup_ship(self):
        """
        Вопрос автодеплоя
        Ручная реализация
        (всё ссылается на класс Field)
        """

    def step_player(self):
    def is_win(self):
    def step_ai(self):


    def print_ui(self):
        # При дебаге - выводим поле врага открытым
        Interface.print_message(last_action):
        Interface.print_fields(self.debug):



    def clear_screen():  # будет декоратором





## Игра "Морской бой"
## Как играть:

1. Клонируйте репозиторий на свой локальный компьютер.
2. Запустите `main.py`, чтобы начать игру.
3. Следуйте инструкциям на экране, чтобы делать свои ходы и наслаждаться игрой!




## Общие принципы работы:

* Игра начинается с расстановки кораблей. Игроки могут расставлять корабли самостоятельно или автоматически.
* После расстановки кораблей начинается игровой процесс. Игроки по очереди делают по одному выстрелу.
* Если выстрел попадает в корабль, игрок делает ещё один ход.
* Если корабль уничтожен, он удаляется из поля.
* Побеждает игрок, первым потопив все корабли противника.

**Дополнительные возможности:**

* Для отладки игры можно включить вывод игрового поля противника. Для этого необходимо при инициализации игры передать аргумент `debug=True`.
* ИИ может использовать стратегию поиска следующей точки для выстрела. В текущей реализации ИИ сначала пытается найти ближайшую точку к последнему попаданию. Если такая точка не найдена, ИИ делает случайный выстрел.


## Структура проекта:

* `main.py` - главный файл, запускающий игру
* `game.py` - класс `Game`, реализующий игровой процесс

**Класс `Game`:**
* Имеет параметр debug: bool
* Хранит в себе экземпляры классов игрока и ИИ

* `start()` - запуск игрового процесса
  
* `setup_ship` - расстановка кораблей
* `step_player` - ход игрока
* `step_ai` - ход ИИ
* `is_win` - проверка победы
* `print_ui` - вывод интерфейса

**Класс `User`:**
* Наследуется от класса Player и хранит в себе экземпляр поля (Field)
* `ask` - запрос хода игрока
* `move` - выполнение хода игрока

**Класс `PlayerAI`:**
* Аналогично User
* `ask` - запрос хода ИИ
* `search_next_shot` - поиск следующей точки для выстрела
* `move` - выполнение хода ИИ

**Класс `Field`:**

* `out` - проверка выхода за пределы поля
* `deploy_ships` - расстановка кораблей
* `auto_deploy_ships` - автоматическая расстановка кораблей
* `add_ship` - добавление корабля на поле

**Класс `Dot`:**
* Элемент класса Field - ячейка.
* Хранит в себе координаты, статус занятости и значение.


SkillFactory homework 9.5.1 (HW-02)

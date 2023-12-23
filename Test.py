from game_errors import GameError


def gen_name():
    for i in range(100):
        yield i

gen = gen_name()

class Test:
    def __init__(self, size):
        self.size = size
        self.name = f'Ship_{size}_{next(gen)}'

Testing1 = Test(1)
Testing2 = Test(2)
Testing3 = Test(2)
Testing4 = Test(3)
print(Testing1.name)
print(Testing2.name)
print(Testing3.name)
print(Testing4.name)


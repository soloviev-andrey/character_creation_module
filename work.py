
from math import sqrt

message = """Добро пожаловать в самую лучшую программу\
    для вычисления квадратного корня из заданного числа"""


def сalculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Описывает функцию."""
    if your_number <= 0:
        return
    calc_square = сalculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень '
          f'из введённого вами числа. '
          f'Это будет:{calc_square}')


print(message)
calc(25.5)
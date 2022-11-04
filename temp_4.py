from math import sqrt

message = '''Добро пожаловать в самую лучшую программу для вычисления
             квадратного корня из заданного числа'''
print(message)


def calculatesquareroot(number):
    """ Вычисляет квадратный корень"""
    return sqrt(number)


def calc(number):
    if number <= 0:
        return
    root = calculatesquareroot(number)
    print(f'Мы вычислили квадратный корень '
          f'из введённого вами числа. Это будет: {root}')


print(message)
calc(25.5)

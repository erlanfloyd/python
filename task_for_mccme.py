"""
Дано действительное положительное число a и целоe число n.
Вычислите a**n. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степень пользоваться нельзя.
Входные данные
Вводится действительное положительное число a и целоe число n.
Выходные данные
Выведите ответ на задачу.
"""

a = int(input('a: '))
n = int(input('n: '))


def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)


print(power(a, n))
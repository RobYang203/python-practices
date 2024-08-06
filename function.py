def add(a, b):
    return a + b


def minus(a, b, /):
    return a - b


def multiplied(*, a, b):
    return a * b


def divide(*, a, b):
    return a / b


def divide_three(a, /, *, b, c):
    return a / b / c


def get_sum_tuple(*a):
    result = 0
    for i in a:
        result += i

    return result


def get_minus_dict(**a):
    result = 0
    for key in a:
        result -= a[key]

    return result


def abs_number(x): return x if x > 0 else x * -1


def call_number_generator(*numbers):
    for i in numbers:
        yield i


print('call add =', add(1, 2))
print('arg call add =', add(a=1, b=3))
print('call minus =', minus(1, 2))
print('call multiplied =', multiplied(a=2, b=2))
print('call divide =', divide(a=2, b=5))
print('call sum:', get_sum_tuple(1, 2, 3, 4, 5, 6, 7, 8))
print('call divide three numbers:', divide_three(1, b=2, c=5))
print('get minus = ', get_minus_dict(a=1, b=2, c=4, d=5))
print('cal abs_number = ', abs_number(-10))
print('call sum by call_number_generator=',
      sum(call_number_generator(1, 2, 3, 4, 0, 9, 8, 7, 6)))

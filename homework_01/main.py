"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i ** 2 for i in num]


# filter types


ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_numbers(nums, num_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if num_type == ODD:
        return list(filter(lambda x: x % 2 != 0, nums))
    elif num_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, nums))
    elif num_type == PRIME:
        return list(filter(lambda x: is_prime(x), nums))
#для проверки дз
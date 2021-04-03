"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*args):
    numbers = list(num ** 2 for num in args)
    return numbers
    
print(power_numbers(2, 3, 4, 56, 345, 0, 34))

"""
>>> power_numbers(1, 2, 5, 7)
<<< [1, 4, 25, 49]
"""


# filter types
EVEN = "even"
ODD = "odd"
PRIME = "prime"
ERR = "error"


def prime_check(lizt:list):
    res = []
    for num in lizt:
        flag = False
        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    # if factor is found, set flag to True
                    flag = True
                    # break out of loop
                    break

        # check if flag is True
        if not flag:
            res.append(num)
    return res



def filter_numbers(lict, type=EVEN):
    if type == EVEN:
        return [num for num in lict if num%2==0]
    elif type == ODD:
        return [num for num in lict if num%2==1]
    elif type == PRIME:
        return [num for num in prime_check(lict)]
    else:
        pass



    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """


print(filter_numbers(range(50,100), PRIME))
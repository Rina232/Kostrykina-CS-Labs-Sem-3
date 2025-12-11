import random


def gen_random(num_count, begin, end):
    """ Генератор рандомных чисел в заданном количестве """
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == "__main__":
    print(*(i for i in gen_random(5, 1, 3)))  # должен выдать выдать 5 случайных чисел
    # в диапазоне от 1 до 3

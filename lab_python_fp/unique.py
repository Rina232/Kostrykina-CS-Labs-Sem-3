from gen_random import *


class Unique(object):
    """ Итератор для удаления дубликатов """

    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)  # Получаем ignore_case из kwargs, по умолчанию = False
        self.items = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            item = next(self.items)

            if type(item) is str and self.ignore_case:
                item_value = item.lower()
            else:
                item_value = item

            if item_value not in self.seen:  # Если элемента еще не было - возвращаем
                self.seen.add(item_value)
                return item

    def __iter__(self):
        return self


if __name__ == "__main__":
    for test in range(3):
        if test == 0:
            data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]  # будет последовательно возвращать только 1 и 2
        elif test == 1:
            data = gen_random(10, 1, 3)  # будет последовательно возвращать только 1, 2 и 3
        else:
            data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']  # будет последовательно возвращать только a, A, b, B
        print(*(i for i in Unique(data)))

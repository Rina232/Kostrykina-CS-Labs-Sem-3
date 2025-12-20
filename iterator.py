#  Поведенческий шаблон: итератор


class BouquetIterator:
    """Итератор для букета"""
    def __init__(self, bouquet):
        self._bouquet = bouquet
        self._index = 0

    def __next__(self):
        if self._index < len(self._bouquet.flowers):
            flower = self._bouquet.flowers[self._index]
            self._index += 1
            return flower
        raise StopIteration

    def __iter__(self):
        return self

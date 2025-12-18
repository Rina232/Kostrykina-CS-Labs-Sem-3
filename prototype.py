import copy
from abc import ABC, abstractmethod


class FlowerPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Flower(FlowerPrototype):
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.color} {self.name} {self.price}₽"


class BouquetPrototype(FlowerPrototype):
    def __init__(self, name):
        self.name = name
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_cost(self):
        return sum(f.price for f in self.flowers)

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        flowers_str = "\n- ".join(str(f) for f in self.flowers)
        return f"Букет '{self.name}' {self.get_cost()}₽:\n- {flowers_str}"

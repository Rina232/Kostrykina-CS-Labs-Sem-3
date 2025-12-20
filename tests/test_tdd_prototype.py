#  Модульное тестирование через TDD - фреймворк
import sys
import os
from prototype import Flower, BouquetPrototype

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestBouquetPrototypeTDD:
    def test_bouquet_creation_tdd(self):
        bouquet = BouquetPrototype("Свадебный")

        assert bouquet.name == "Свадебный"
        assert bouquet.flowers == []
        assert bouquet.get_cost() == 0

    def test_add_flower_to_bouquet_tdd(self):
        bouquet = BouquetPrototype("Весенний")
        flower = Flower("Тюльпан", "желтый", 50)

        bouquet.add_flower(flower)

        assert len(bouquet.flowers) == 1
        assert bouquet.flowers[0] is flower

    def test_bouquet_cost_calculation_tdd(self):
        bouquet = BouquetPrototype("Дорогой букет")

        assert bouquet.get_cost() == 0

        bouquet.add_flower(Flower("Роза", "красная", 100))
        assert bouquet.get_cost() == 100

        bouquet.add_flower(Flower("Лилии", "белые", 150))
        assert bouquet.get_cost() == 250

        bouquet.add_flower(Flower("Орхидея", "фиолетовая", 300))
        assert bouquet.get_cost() == 550

    def test_bouquet_clone_tdd(self):
        original = BouquetPrototype("Оригинальный букет")
        original.add_flower(Flower("Роза", "красная", 100))
        original.add_flower(Flower("Тюльпан", "желтый", 50))

        cloned = original.clone()

        assert cloned.name == "Оригинальный букет"
        assert len(cloned.flowers) == 2
        assert cloned.get_cost() == 150

        assert cloned.flowers[0] is not original.flowers[0]
        assert cloned.flowers[1] is not original.flowers[1]

        cloned.flowers[0].price = 200
        assert original.flowers[0].price == 100

    def test_bouquet_str_method_tdd(self):
        bouquet = BouquetPrototype("Тестовый букет")
        bouquet.add_flower(Flower("Роза", "красная", 100))
        bouquet.add_flower(Flower("Тюльпан", "желтый", 50))

        result = str(bouquet)

        assert "Букет 'Тестовый букет' 150₽:" in result
        assert "красная Роза 100₽" in result
        assert "желтый Тюльпан 50₽" in result


def test_new_feature_tdd_example():
    bouquet = BouquetPrototype("Тест")
    bouquet.add_flower(Flower("Роза", "красная", 100))

from prototype import Flower, BouquetPrototype
from decorator import BasicOrder, WrappingDecorator, CardDecorator
from iterator import BouquetIterator


def demonstrate_prototype():
    rose_prototype = Flower("Роза", "красная", 300)
    tulip_prototype = Flower("Тюльпан", "желтый", 150)

    rose1 = rose_prototype.clone()
    rose2 = rose_prototype.clone()
    rose2.color = "белая"

    wedding_bouquet = BouquetPrototype("Свадебный букет")
    wedding_bouquet.add_flower(rose1)
    wedding_bouquet.add_flower(rose2)
    wedding_bouquet.add_flower(tulip_prototype.clone())
    wedding_bouquet.add_flower(tulip_prototype.clone())

    print("Оригинальный букет:")
    print(wedding_bouquet)

    cloned_bouquet = wedding_bouquet.clone()
    print("\nКлонированный букет:")
    print(cloned_bouquet)

    print(f"\nПроверка на ссылку на один и тот же объект {wedding_bouquet is cloned_bouquet}\n")


def demonstrate_decorator():
    birthday_bouquet = BouquetPrototype("Праздничный букет")
    birthday_bouquet.add_flower(Flower("Гербера", "оранжевая", 150))
    birthday_bouquet.add_flower(Flower("Хризантема", "белая", 200))
    birthday_bouquet.add_flower(Flower("Роза", "розовая", 400))

    order = BasicOrder(birthday_bouquet)
    print(f"{order.get_description()}: ${order.get_cost()}")

    order = WrappingDecorator(order, "праздничная")
    print(f"{order.get_description()}: ${order.get_cost()}")

    order = CardDecorator(order, "С Днем Рождения!")
    print(f"{order.get_description()}: ${order.get_cost()}")


def demonstrate_iterator():
    print("\nЦветы в букете:")
    bouquet = BouquetPrototype("Весенний микс")
    bouquet.add_flower(Flower("Тюльпан", "розовый", 200))
    bouquet.add_flower(Flower("Нарцисс", "желтый", 180))
    bouquet.add_flower(Flower("Гиацинт", "голубой", 300))

    for flower in BouquetIterator(bouquet):
        print(f"  - {flower}")


def main():
    demonstrate_prototype()
    demonstrate_decorator()
    demonstrate_iterator()


if __name__ == "__main__":
    main()

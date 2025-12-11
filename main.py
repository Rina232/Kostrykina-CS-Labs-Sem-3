from prototype import Flower, BouquetPrototype
from decorator import BasicOrder, WrappingDecorator, CardDecorator, DeliveryDecorator
from iterator import FlowerCollection, BouquetIterator


def demonstrate_prototype():

    # Создаем прототип цветка
    rose_prototype = Flower("Роза", "красная", 3.5)
    tulip_prototype = Flower("Тюльпан", "желтый", 2.0)

    # Клонируем цветы
    rose1 = rose_prototype.clone()
    rose2 = rose_prototype.clone()
    rose2.color = "белая"  # Модифицируем клон

    # Создаем прототип букета
    wedding_bouquet = BouquetPrototype("Свадебный букет")
    wedding_bouquet.add_flower(rose1)
    wedding_bouquet.add_flower(rose2)
    wedding_bouquet.add_flower(tulip_prototype.clone())
    wedding_bouquet.add_flower(tulip_prototype.clone())

    print("Оригинальный букет:")
    print(wedding_bouquet)

    # Клонируем целый букет
    cloned_bouquet = wedding_bouquet.clone()
    print("\nКлонированный букет:")
    print(cloned_bouquet)

    # Проверяем, что это разные объекты
    print(f"\nЭто один и тот же объект? {wedding_bouquet is cloned_bouquet}")
    print(f"Цветы одинаковые? {wedding_bouquet.flowers[0] is cloned_bouquet.flowers[0]}")


def demonstrate_decorator():
    # Создаем базовый букет
    birthday_bouquet = BouquetPrototype("Праздничный букет")
    birthday_bouquet.add_flower(Flower("Гербера", "оранжевая", 2.5))
    birthday_bouquet.add_flower(Flower("Хризантема", "белая", 3.0))
    birthday_bouquet.add_flower(Flower("Роза", "розовая", 4.0))

    # Базовый заказ
    order = BasicOrder(birthday_bouquet)
    print(f"{order.get_description()}: ${order.get_cost()}")

    # Добавляем упаковку
    order = WrappingDecorator(order, "праздничная")
    print(f"{order.get_description()}: ${order.get_cost()}")

    # Добавляем открытку
    order = CardDecorator(order, "С Днем Рождения!")
    print(f"{order.get_description()}: ${order.get_cost()}")


def demonstrate_iterator():
    # Создаем коллекцию цветов
    collection = FlowerCollection()
    collection.add_flower(Flower("Роза", "красная", 3.5))
    collection.add_flower(Flower("Тюльпан", "желтый", 2.0))
    collection.add_flower(Flower("Лилии", "белые", 4.0))
    collection.add_flower(Flower("Орхидея", "фиолетовая", 6.5))

    # Итерируемся по коллекции
    print("Все цветы в магазине:")
    for flower in collection:
        print(f"  - {flower}")

    # Итератор для букета
    print("\nЦветы в букете:")
    bouquet = BouquetPrototype("Весенний микс")
    bouquet.add_flower(Flower("Тюльпан", "розовый", 2.5))
    bouquet.add_flower(Flower("Нарцисс", "желтый", 1.8))
    bouquet.add_flower(Flower("Гиацинт", "голубой", 3.2))

    for flower in BouquetIterator(bouquet):
        print(f"  - {flower}")


def main():
    print("Предметная область: Цветочный магазин")

    demonstrate_prototype()
    demonstrate_decorator()
    demonstrate_iterator()


if __name__ == "__main__":
    main()

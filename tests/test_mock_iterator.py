#  Модульное тестирование через создание Mock-объектов
from unittest.mock import Mock
from iterator import BouquetIterator


def test_mock():
    mock_flower = Mock()
    mock_flower.name = "Тестовый цветок"

    mock_bouquet = Mock()
    mock_bouquet.flowers = [mock_flower]

    iterator = BouquetIterator(mock_bouquet)

    result = next(iterator)

    assert result is mock_flower
    assert result.name == "Тестовый цветок"

    print("Тест пройден успешно")


if __name__ == "__main__":
    test_mock()

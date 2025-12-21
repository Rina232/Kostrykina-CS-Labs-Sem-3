import unittest
from main import *


class TestProgrammingLanguages(unittest.TestCase):
    """Класс для тестирования функций"""
    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        self.languages = languages
        self.constructions = constructions
        self.language_constructions = language_constructions
        # Получаем соединения
        self.one_to_many = get_one_to_many(self.languages, self.constructions)
        self.many_to_many = get_many_to_many(self.languages, self.constructions, self.language_constructions)

    def test_task_b1(self):
        """Проверка задания B1"""
        result = task_b1(self.one_to_many)
        # Проверяем количество найденных конструкций (должно быть 2)
        self.assertEqual(len(result), 2)

        # Проверяем, что все конструкции начинаются с 'А'
        for item in result:
            self.assertTrue(item[0].startswith('А'))

    def test_task_b2(self):
        """Проверка задания B2"""
        result = task_b2(self.languages, self.one_to_many)
        # Проверяем количество языков (должно быть 4)
        self.assertEqual(len(result), 4)

        # Массив для проверки корректности вычисленных минимальных времён
        expected_results = [
            ("Python", 3),
            ("JavaScript", 7),
            ("Java", 8),
            ("C++", 12)]

        for i, (lang_name, min_time) in enumerate(result):
            expected_lang, expected_time = expected_results[i]
            # Проверяем название языка
            self.assertEqual(lang_name, expected_lang)
            # Проверяем минимальное время компиляции
            self.assertEqual(min_time, expected_time)

        # Проверяем сортировку по возрастанию времени компиляции
        times = [time for _, time in result]
        self.assertEqual(times, sorted(times))

    def test_task_b3(self):
        """Проверка задания B3"""
        result = task_b3(self.many_to_many)

        # Проверяем количество связей (должно быть 5)
        self.assertEqual(len(result), 5)

        # Проверяем сортировку по названию конструкций
        construct_names = [item[0] for item in result]
        self.assertEqual(construct_names, sorted(construct_names))

        for i, (construct_name, compile_time, lang_name) in enumerate(result):
            # Проверяем, что конструкция и язык существуют в исходных данных
            self.assertTrue(any(c.name == construct_name for c in self.constructions))
            self.assertTrue(any(lang.name == lang_name for lang in self.languages))


if __name__ == "__main__":
    unittest.main()

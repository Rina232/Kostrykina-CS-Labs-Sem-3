from operator import itemgetter


class ProgrammingLanguage:
    """Язык программирования"""

    def __init__(self, pl_id, name):
        self.id = pl_id
        self.name = name


class SyntaxConstruction:
    """Синтаксическая конструкция"""

    def __init__(self, sc_id, name, compile_time, pl_id):
        self.id = sc_id
        self.name = name
        self.compile_time = compile_time    # Время компиляции в миллисекундах - количественный признак
        self.pl_id = pl_id


class LanguageConstruction:
    """Конструкции языков для связи многие-ко-многим"""

    def __init__(self, sc_id, pl_id):
        self.sc_id = sc_id
        self.pl_id = pl_id


# Языки программирования
languages = [
    ProgrammingLanguage(1, "Python"),
    ProgrammingLanguage(2, "Java"),
    ProgrammingLanguage(3, "C++"),
    ProgrammingLanguage(4, "JavaScript")
]

# Синтаксические конструкции
constructions = [
    SyntaxConstruction(1, "Лямбда-функция", 3, 1),
    SyntaxConstruction(2, "Интерфейс", 8, 2),
    SyntaxConstruction(3, "Абстрактный класс", 10, 2),
    SyntaxConstruction(4, "Шаблон функции", 12, 3),
    SyntaxConstruction(5, "Асинхронная функция", 7, 4)
]

# Связи многие-ко-многим
language_constructions = [
    LanguageConstruction(1, 1),
    LanguageConstruction(2, 2),
    LanguageConstruction(3, 2),
    LanguageConstruction(4, 3),
    LanguageConstruction(5, 1),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(c.name, c.compile_time, pl.name)
                   for pl in languages
                   for c in constructions
                   if c.pl_id == pl.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(pl.name, lc.pl_id, lc.sc_id)
                         for pl in languages
                         for lc in language_constructions
                         if pl.id == lc.pl_id]

    many_to_many = [(sc.name, sc.compile_time, pl_name)
                    for pl_name, pl_id, sc_id in many_to_many_temp
                    for sc in constructions if sc.id == sc_id]

    print('Задание В1')
    # Список синтаксическиях конструкций, название которых начинается с 'А',
    # и названия языков, в которых они содержатся:
    result_1 = list(filter(lambda i: i[0].startswith('А'), one_to_many))
    # Сортируем по названию конструкции
    result_1_sorted = sorted(result_1, key=itemgetter(0))

    for construction_name, compile_time, language_name in result_1_sorted:
        print(f"Конструкция: {construction_name:<25} Язык: {language_name}")

    print('\nЗадание В2')
    # Список языков с минимальным временем компиляции конструкций в каждом языке программирования,
    # отсортированный по минимальному времени компиляции
    result_2_unsorted = []
    # Перебираем все языки программирования
    for pl in languages:
        # Список конструкций языка
        l_constructions = list(filter(lambda i: i[2] == pl.name, one_to_many))
        # Если конструкция не пустая
        if len(l_constructions) > 0:
            # Времена компиляции конструкций языка
            l_times = [time for _, time, _ in l_constructions]
            # Минимальное время компиляции
            l_min_time = min(l_times)
            result_2_unsorted.append((pl.name, l_min_time))

    # Сортировка по минимальному времени компиляции
    result_2 = sorted(result_2_unsorted, key=itemgetter(1))

    for lang_name, min_time in result_2:
        print(f"Язык: {lang_name:<15} Мин. время компиляции: {min_time} мс")

    print('\nЗадание В3')
    # Список всех связанных конструкций и языков, отсортированный по конструкциям
    result_3 = sorted(many_to_many, key=itemgetter(0))

    for construction_name, compile_time, language_name in result_3:
        print(f"Конструкция: {construction_name:<25} Язык: {language_name}")


if __name__ == "__main__":
    main()

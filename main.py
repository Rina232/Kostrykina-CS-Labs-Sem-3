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
        self.compile_time = compile_time
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


def get_one_to_many(lang, construct):
    """Создаёт соединение один-ко-многим между языками и конструкциями"""
    return [(sc.name, sc.compile_time, pl.name)
            for pl in lang
            for sc in construct
            if sc.pl_id == pl.id]


def get_many_to_many(lang, construct, lang_construct):
    """Создаёт соединение многие-ко-многим между языками и конструкциями"""
    many_to_many_temp = [(pl.name, lc.pl_id, lc.sc_id)
                         for pl in lang
                         for lc in lang_construct
                         if pl.id == lc.pl_id]

    return [(sc.name, sc.compile_time, pl_name)
            for pl_name, pl_id, sc_id in many_to_many_temp
            for sc in construct if sc.id == sc_id]


def task_b1(one_to_many):
    """Задание В1: Фильтрация конструкций, начинающихся на букву 'A'"""
    # Фильтруем конструкции, начинающиеся с 'А'
    result = list(filter(lambda i: i[0].startswith('А'), one_to_many))
    # Сортируем по названию конструкции (первый элемент кортежа)
    return sorted(result, key=itemgetter(0))


def task_b2(lang, one_to_many):
    """Задание В2: Поиск минимального времени компиляции для каждого языка"""
    result = []
    for pl in lang:
        # Находим все конструкции этого языка
        l_constructions = list(filter(lambda i: i[2] == pl.name, one_to_many))
        if len(l_constructions) > 0:   # Если у языка есть хотя бы одна конструкция
            l_times = [time for _, time, _ in l_constructions]  # Извлекаем времена компиляции
            l_min_time = min(l_times)  # Находим минимальное время
            result.append((pl.name, l_min_time))
    # Сортируем результат по минимальному времени компиляции (второй элемент кортежа)
    return sorted(result, key=itemgetter(1))


def task_b3(many_to_many):
    """Задание В2: Сортировка всех связанных конструкций и языков"""
    return sorted(many_to_many, key=itemgetter(0))


def main():
    # Получаем соединения
    one_to_many = get_one_to_many(languages, constructions)
    many_to_many = get_many_to_many(languages, constructions, language_constructions)

    print('Задание В1')
    result_1 = task_b1(one_to_many)
    for construction_name, compile_time, language_name in result_1:
        print(f"Конструкция: {construction_name:<25} Язык: {language_name}")

    print('\nЗадание В2')
    result_2 = task_b2(languages, one_to_many)
    for language_name, min_time in result_2:
        print(f"Язык: {language_name:<15} Мин. время компиляции: {min_time} мс")

    print('\nЗадание В3')
    result_3 = task_b3(many_to_many)
    for construction_name, compile_time, language_name in result_3:
        print(f"Конструкция: {construction_name:<25} Язык: {language_name}")


if __name__ == "__main__":
    main()

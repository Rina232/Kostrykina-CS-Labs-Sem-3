from print_result import print_result
from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from unique import Unique
import json

with open('data_light.json', encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    """ Сортируем список профессий без повторений, игнорируя регистр """
    return sorted(Unique(map(lambda x: x.lower().strip(), field(arg, 'job-name')), ignore_case=True))


@print_result
def f2(arg):
    """  Фильтруем только профессии программистов """
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    """ Добавляем "с опытом Python" к каждой профессии """
    return list(map(lambda x: f'{x} с опытом Python', arg))


@print_result
def f4(arg):
    """ Генерируем зарплаты и присоединяем к профессиям """
    salaries = list(gen_random(len(arg), 100000, 200000))
    return [f'{prof}, зарплата {salary} руб.' for prof, salary in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

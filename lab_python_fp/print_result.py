def print_result(func):
    """ Декоратор, выводящий на экран результат выполнения функции """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__)

        if type(res) == list:
            for item in res:
                print(item)
        elif type(res) == dict:
            for key, value in res.items():
                print(f"{key} = {value}")
        else:
            print(res)

        return res

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()

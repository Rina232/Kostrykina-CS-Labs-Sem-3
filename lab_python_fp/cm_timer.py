import time
from contextlib import contextmanager


class cm_timer_1:
    """ Контекстный менеджер на основе класса """
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        period = time.time() - self.start_time
        print(f"Время работы: {period:.3f}")


@contextmanager
def cm_timer_2():
    """ Контекстный менеджер с использованием contextlib """
    start_time = time.time()
    try:
        yield
    finally:
        period = time.time() - start_time
        print(f"Время работы: {period:.3f}")


if __name__ == '__main__':
    print("Тест контекстного менеджера на основе класса:")
    with cm_timer_1():
        time.sleep(1)

    print("\nТест контекстного менеджера с использованием contextlib:")
    with cm_timer_2():
        time.sleep(1.5)

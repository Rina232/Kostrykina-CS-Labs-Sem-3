from abc import ABC, abstractmethod


class Figure(ABC):
    """ Абстрактный класс «Геометрическая фигура» """

    @abstractmethod
    def get_area(self):
        """ Абстрактный метод для вычисления площади """
        pass

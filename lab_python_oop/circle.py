from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
from math import pi


class Circle(Figure):
    """ Класс «Круг» """

    def __init__(self, radius, color):
        self._radius = radius
        self._color = Color(color)

        self._name = "Круг"

    @property
    def name(self):
        """ Свойство для получения названия """
        return self._name

    def get_area(self):
        """ Вычисление площади круга """

        return pi * (self._radius ** 2)

    def __repr__(self):
        return "Объект класса {} цветом {}: R = {}, S = {}".format(self._name, self._color.color,
                                                           self._radius, self.get_area())

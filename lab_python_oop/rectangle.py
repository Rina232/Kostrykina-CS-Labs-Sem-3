from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    """ Класс «Прямоугольник» """

    def __init__(self, length, width, color):
        self._width = width
        self._length = length
        self._color = Color(color)

        self._name = "Прямоугольник"

    @property
    def name(self):
        """ Свойство для получения названия """

        return self._name

    def get_area(self):
        """ Вычисление площади прямоугольника """

        return self._width * self._length

    def __repr__(self):
        return "Объект класса {} цветом {}: a = {}, b = {}, S = {}".format(self._name, self._color.color,
                                                                   self._width, self._length, self.get_area())

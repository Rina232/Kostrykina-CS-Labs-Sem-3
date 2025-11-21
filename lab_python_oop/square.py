from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    """ Класс «Квадрат» """

    def __init__(self, length):
        super().__init__(length, length, None)

        self._name = "Квадрат"

    def __repr__(self):
        return "Объект класса {} цветом {}: a = {}, S = {}".format(self._name, self._color,
                                                                   self._length, self.get_area())

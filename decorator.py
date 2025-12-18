from abc import ABC, abstractmethod


class OrderComponent(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class BasicOrder(OrderComponent):
    def __init__(self, bouquet):
        self.bouquet = bouquet

    def get_description(self):
        return f"Заказ: {self.bouquet.name}"

    def get_cost(self):
        return self.bouquet.get_cost()


class OrderDecorator(OrderComponent):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def get_description(self):
        return self._wrapped.get_description()

    def get_cost(self):
        return self._wrapped.get_cost()


class WrappingDecorator(OrderDecorator):
    def __init__(self, wrapped, style="стандартная"):
        super().__init__(wrapped)
        self.style = style
        self.price = 50 if style == "стандартная" else 100

    def get_description(self):
        return f"{self._wrapped.get_description()} + упаковка ({self.style})"

    def get_cost(self):
        return self._wrapped.get_cost() + self.price


class CardDecorator(OrderDecorator):
    def __init__(self, wrapped, message=""):
        super().__init__(wrapped)
        self.message = message
        self.price = 75

    def get_description(self):
        if self.message:
            msg = f"с текстом '{self.message}'"
        else:
            msg = ""
        return f"{self._wrapped.get_description()} + открытка {msg}"

    def get_cost(self):
        return self._wrapped.get_cost() + self.price

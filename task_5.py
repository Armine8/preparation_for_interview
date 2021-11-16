"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна передаваться переменная —
скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        print(f'Цена товара со скидкой {self.discount}%: {self.get_price() - self.get_price() * self.discount / 100}')

    def get_parent_data(self):
        return f'{self.get_name()} {self.get_price()}'


B = ItemDiscountReport('meat', 500, 20)
B.__str__()



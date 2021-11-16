"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский,
и дочерний классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского
класса и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
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
    def get_parent_data(self):
        return f'{self.get_name()} {self.get_price()}'


A = ItemDiscount('meat', 500)
B = ItemDiscountReport('meat', 500)
A.set_price(1500)
B.set_price(1500)
print(A.get_name(), A.get_price())
print(B.get_parent_data())



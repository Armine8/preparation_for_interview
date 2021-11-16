"""
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет
отвечать за вывод названия товара, а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.

Если в нескольких классах находятся методы, имеющие одинаковые имена, но реализуемые по-разному,
их называют полиморфными.
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

    def get_info(self):
        print(self.__name, self.__price)


class ItemDiscountReport1(ItemDiscount):
    def get_info(self):
        print(self.get_name())


class ItemDiscountReport2(ItemDiscount):
    def get_info(self):
        print(self.get_price())


A = ItemDiscount('eggs', 100)
A.get_info()

B = ItemDiscountReport1('meat', 500)
B.get_info()

C = ItemDiscountReport2('meat', 80)
C.get_info()



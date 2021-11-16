"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import random


def my_func(start, end):
    my_dict = {f'elem {a}': random.randint(start, end) for a in range(1, 10) if a != 0}
    print(my_dict.values())
    print(my_dict)


my_func(0, 200)


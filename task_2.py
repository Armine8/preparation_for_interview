"""Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False."""
#
import math

a = input('Введите число ')

if '.' in a:
    print('Вы ввели дробное число')
    index = a.find('.')
    integer_part = a[:index]
    fractional_part = a[(index+1):]
    if integer_part == fractional_part:
        print('True')
    else:
        print('False')
else:
    print('Вы ввели целое число')





# a = float(input('Введите число '))
# b = (math.modf(a))
# print(b)
#
# integer_part = int(b[1])
# print(integer_part)
# fractional_part = (b[0])
# print(fractional_part)

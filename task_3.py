"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""

keys = [1, 2, 3, 4, 5]
values = ['hi', 'hello', 'good_morning']

my_dict = {}

if len(keys) > len(values):
    count = len(keys) - len(values)
    for i in range(count):
        values.append(None)
    my_dict = dict(zip(keys, values))
else:
    my_dict = dict(zip(keys, values))
print(my_dict)

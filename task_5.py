"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр, например: example345.
"""

# в числовом списке заменить на example345

def read_file(link):
    with open(link, 'r', encoding='UTF-8') as my_file:
        for line in my_file:
            old_data = my_file.read()
            what_to_change = line.find('s')
            new_data = old_data.replace(line[what_to_change], 'ppp')
    with open(link, 'w', encoding='UTF-8') as my_file:
        my_file.write(new_data)



def create_file(file_name):
    try:
        with open(file_name, 'x', encoding='UTF-8') as g:
            text_info = []
            num_info = []
            for i in range(5):
                if i % 2 == 0:
                    text_info.append(f'test_{i}')
                else:
                    text_info.append(f'test')
                num_info.append(i)
            for item in zip(text_info, num_info):
                g.write(str(item) + '\n')
        read_file(file_name)
    except FileExistsError:
        print('Файл с таким именем уже существует')


create_file('my_file.txt')


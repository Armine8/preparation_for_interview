"""
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла
(без расширения).
"""
import os
from os import path


def find_file_name(file_name):
    path_name = os.path.abspath(file_name)
    full_name = path.basename(path_name)
    name = path.splitext(full_name)[0]
    print(name)


find_file_name('task_4.py')

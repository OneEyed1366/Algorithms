from sys import argv
from random import randrange
from memory_profiler import profile

"""
Система: Windows 10 (x86)
Язык: Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:37:30) [MSC v.1927 32 bit (Intel)] on win32
Среда разработки: VSCode
    Версия: 1.52.1 (user setup)
    Фиксация: ea3859d4ba2f3e577a159bc91e3074c5d85c0523
    Дата: 2020-12-16T16:34:50.160Z
    Electron: 9.3.5
    Chrome: 83.0.4103.122
    Node.js: 12.14.1
    V8: 8.3.110.13-electron.0
    ОС: Windows_NT ia32 10.0.19041
"""


@profile
def nums():
    try:
        donor_num = int(argv[1])
    except IndexError:
        donor_num = int(input("Введите любое Положительное число: "))

    result = 0

    for i in map(int, str(donor_num)):
        if i % 2 == 0:
            result += 1

    print(f"Число: {donor_num}, чётных чисел: {result}")

nums()

"""
Аналитическая сводка по работе программы:
Было выделено 14.375 MiB памяти для запуска программы
В дальнейшем, несмотря на инициализацию переменных в строках 10/12, 14, изменения потребления памяти Выявлено Не было**
Итоговое потребление памяти для корректной работы программы составило 14.375 MiB

Результаты работы программы*:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    7     14.375 MiB     14.375 MiB           1   @profile
    8                                         def nums():
    9     14.375 MiB      0.0 MiB           1       try:
    10     14.375 MiB      0.0 MiB           1           donor_num = int(argv[1])
    11     14.375 MiB      0.0 MiB           1       except IndexError:
    12     14.375 MiB      0.0 MiB           1           donor_num = int(input("Введите любое Положительное число: "))
    13
    14     14.375 MiB      0.0 MiB           1       result = 0
    15
    16     14.375 MiB      0.0 MiB           5       for i in map(int, str(donor_num)):
    17     14.375 MiB      0.0 MiB           4           if i % 2 == 0:
    18     14.375 MiB      0.0 MiB           2               result += 1
    19
    20     14.375 MiB      0.0 MiB           1       print(f"Число: {donor_num}, чётных чисел: {result}")

*Приведены усредненные значения после, минимально, 4 запусков программы
**Судя по данным столбцов 'Increment' и 'Mem usage'

Результаты проведения тестов потребления памяти (итоговые значения): 14.3, 14.4, 14.4, 14.4
"""


@profile
def even_nums():
    donor_list = [randrange(0, 200) for i in range(15)]
    result_list = [i for i in range(len(donor_list)) if donor_list[i] % 2 == 0]

    # for i in range(len(donor_list)):
    #     if donor_list[i] % 2 == 0:
    #         result_list.append(donor_list[i])

    print(
        f"Начальный список: {donor_list}\nСписок индексов чётных чисел: {result_list}")


even_nums()

"""
Аналитическая сводка по работе программы:
Было выделено 14.475 MiB памяти для запуска программы
В дальнейшем, несмотря на инициализацию переменных в строках 7 и 8 с использованием генераторов, изменения потребления памяти Выявлено Не было**
Неисполняемый код в строках 10 - 12 не повлиял на итоговый результат потребления памяти**
Итоговое потребление памяти для корректной работы программы составило 14.475 MiB

Результаты работы программы*:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     14.475 MiB     14.475 MiB           1   @profile
     6                                         def even_nums():
     7     14.475 MiB      0.0 MiB          18       donor_list = [randrange(0, 200) for i in range(15)]
     8     14.475 MiB      0.0 MiB          18       result_list = [i for i in range(len(donor_list)) if donor_list[i] % 2 == 0]
     9
    10                                             # for i in range(len(donor_list)):
    11                                             #     if donor_list[i] % 2 == 0:
    12                                             #         result_list.append(donor_list[i])
    13
    14     14.475 MiB      0.0 MiB           1       print(f"Начальный список: {donor_list}\nСписок индексов чётных чисел: {result_list}")

*Приведены усредненные значения после, минимально, 4 запусков программы
**Судя по данным столбцов 'Increment' и 'Mem usage'

Результаты проведения тестов потребления памяти (итоговые значения): 14.4, 14.5, 14.5, 14.5
"""


@profile
def min_max():
    donor_list = [randrange(0, 50) for i in range(15)]
    min_num = min(donor_list)
    i_min_num = donor_list.index(min_num)
    max_num = max(donor_list)
    i_max_num = donor_list.index(max_num)

    msg = f"Стартовый массив: {donor_list}\nМинимальное число: {min_num} (Индекс: {i_min_num})\nМаксимальное число: {max_num} (Индекс: {i_max_num})"

    print(msg)

    donor_list[i_min_num] = max_num
    donor_list[i_max_num] = min_num

    print(f"Итоговый массив: {donor_list}\nМинимальное число: {min_num} (Индекс: {donor_list.index(min_num)})\nМаксимальное число: {max_num} (Индекс: {donor_list.index(max_num)})")



"""
Аналитическая сводка по работе программы:
Было выделено 14.475 MiB памяти для запуска программы
В дальнейшем, несмотря на инициализацию переменных в строках 7 - 11, 13, с использованием генераторов и функций вычисления наибольших/наименьших значений внутри ранее инициализированных переменных, изменения потребления памяти Выявлено Не было**
Также, несмотря на измненение значений переменных в строках 17 и 18, изменения потребления памяти выявлено не было**
Итоговое потребление памяти для корректной работы программы составило 14.475 MiB

Результаты работы программы*:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     5     14.5 MiB     14.5 MiB           1   @profile
     6                                         def min_max():
     7     14.5 MiB      0.0 MiB          18       donor_list = [randrange(0, 50) for i in range(15)]
     8     14.5 MiB      0.0 MiB           1       min_num = min(donor_list)
     9     14.5 MiB      0.0 MiB           1       i_min_num = donor_list.index(min_num)
    10     14.5 MiB      0.0 MiB           1       max_num = max(donor_list)
    11     14.5 MiB      0.0 MiB           1       i_max_num = donor_list.index(max_num)
    12
    13     14.5 MiB      0.0 MiB           1       msg = f"Стартовый массив: {donor_list}\nМинимальное число: {min_num} (Индекс: {i_min_num})\nМаксимальное число: {max_num} (Индекс: {i_max_num})"
    14
    15     14.5 MiB      0.0 MiB           1       print(msg)
    16
    17     14.5 MiB      0.0 MiB           1       donor_list[i_min_num] = max_num
    18     14.5 MiB      0.0 MiB           1       donor_list[i_max_num] = min_num
    19
    20     14.5 MiB      0.0 MiB           1       print(f"Итоговый массив: {donor_list}\nМинимальное число: {min_num} (Индекс: {donor_list.index(min_num)})\nМаксимальное число: {max_num} (Индекс: {donor_list.index(max_num)})")

*Приведены усредненные значения после, минимально, 4 запусков программы
**Судя по данным столбцов 'Increment' и 'Mem usage'

Результаты проведения тестов потребления памяти (итоговые значения): 14.4, 14.5, 14.5, 14.5
"""

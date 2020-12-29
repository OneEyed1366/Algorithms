from random import randrange

def minus_num():
    donor_list = [randrange(-200, 10) for i in range(20)]
    result_num = min(donor_list)
    result_i = donor_list.index(result_num)

    print(f"Стартовый массив: {donor_list}\nМаксимальный отрицательный элемент: {result_num} (Индекс: {result_i})")

minus_num()
from random import randrange

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

min_max()
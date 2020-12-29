from random import randrange

def check_how_much():
    donor_list = [randrange(0, 9) for i in range(19)]
    result_num = 0

    for i in donor_list:
        if donor_list.count(i) > result_num:
            result_num = i

    print(
        f"Список чисел: {donor_list}\nНаиболее часто встречающееся число: {result_num} (Число повторов внутри списка: {donor_list.count(result_num)})")

check_how_much()
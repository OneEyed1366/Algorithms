from random import randrange

def sum_between_min_max():
    donor_list = sorted([randrange(0, 50) for i in range(20)])
    min_num = min(donor_list)
    i_min_num = donor_list.index(min_num)
    max_num = max(donor_list)
    i_max_num = donor_list.index(max_num)
    result_list = [i for i in donor_list[i_min_num : i_max_num] if i != min_num and i != max_num]
    msg = f"Начальный список: {donor_list}\nМинимальное число: {min_num}, Максимальное число: {max_num}\nСрез списка между {min_num} и {max_num}: {result_list}\nСумма значений списка между {min_num} и {max_num}: {sum(result_list)}"

    print(msg)

sum_between_min_max()

from random import randrange

def two_min_nums():
    donor_list = [randrange(-10, 10) for i in range(8)]
    min_1 = min(donor_list)

    print(f"Начальный список: {donor_list}")

    donor_list.pop(donor_list.index(min_1))
    min_2 = min(donor_list)

    print(f"2 минимальных значения: {min_1} и {min_2}")

two_min_nums()

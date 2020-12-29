from random import randrange

def even_nums():
    donor_list = [randrange(0, 200) for i in range(15)]
    result_list = [i for i in range(len(donor_list)) if donor_list[i] % 2 == 0]

    # for i in range(len(donor_list)):
    #     if donor_list[i] % 2 == 0:
    #         result_list.append(donor_list[i])
    
    print(f"Начальный список: {donor_list}\nСписок индексов чётных чисел: {result_list}")

even_nums()
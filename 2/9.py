def max_sum_of_nums():
    msg = "Введите любое Положительнок число\n\nЧтобы завершить выполнение скрипта, введите '0': "
    donor_num = int(input(msg))
    result_sum = 0
    result_num = 0

    while donor_num != 0:
        cycle_num = donor_num
        cycle_sum = 0
        while donor_num > 0:
            cycle_sum += donor_num % 10
            donor_num //= 10
        if cycle_sum > result_sum:
            result_sum = cycle_sum
            result_num = cycle_num

        donor_num = int(input(msg))

    print(f'Число {result_num} имеет максимальную сумму цифр: {result_sum}')

max_sum_of_nums()
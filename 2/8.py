from sys import argv

def find_the_number():
    try:
        all_nums = int(argv[1])
        num_to_find = int(argv[2])
    except:
        all_nums = int(input("Введите любую последовательность чисел: "))
        num_to_find = int(input("Введите цифру, которую необходимо искать: "))

    result = 0

    for i in map(int, str(all_nums)):
        if i == num_to_find:
            result += 1

    if result == 0:
        print(f"Число {num_to_find} не встречается в последовательности {all_nums}.")
    else:
        print(f"Число {num_to_find} встречается в последовательности {all_nums} {result} раз.")

find_the_number()
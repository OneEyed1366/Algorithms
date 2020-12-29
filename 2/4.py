from sys import argv

def sum_of_element():
    try:
        donor_num = int(argv[1])
    except IndexError:
        donor_num = int(input("Введите Положительное число: "))
    
    result = 0
    current_state = 1

    for i in range(donor_num):
        result += current_state
        current_state /= -2

    print(f"Результат: {result}")

sum_of_element()
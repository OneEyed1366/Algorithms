from sys import argv

def reverse_num():
    try:
        donor_num = int(argv[1])
    except IndexError:
        donor_num = int(input("Введите любое Положительное число: "))
    
    result = 0

    while donor_num > 0:
        result = result * 10 + donor_num % 10
        donor_num = donor_num // 10

    print(f"Результат: {result}")

reverse_num()
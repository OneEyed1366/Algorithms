from sys import argv

def nums():
    try:
        donor_num = int(argv[1])
    except IndexError:
        donor_num = int(input("Введите любое Положительное число: "))

    result = 0

    for i in map(int, str(donor_num)):
        if i % 2 == 0:
            result += 1

    print(f"Число: {donor_num}, чётных чисел: {result}")

nums()
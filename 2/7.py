from sys import argv

def natural_nums():
    try:
        n = int(argv[1])
    except IndexError:
        n = int(input("Введите любое натуральное число: "))

    s = 0
    result = 0

    for i in range(1, n+1):
        s += i

    result = n * (n + 1) // 2

    print(f"{s} = {result}")

natural_nums()
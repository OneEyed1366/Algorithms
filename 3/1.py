def multiple_numbers():
    for i in range(2, 100):
        result = 0
        result_nums = []

        for n in range(2, 10):
            if i % n == 0:
                result += 1
                result_nums.append(n)

        if result != 0:
            print(f"Чисел, кратных {i}: {result} (Кратные числа: {result_nums})")
        else:
            print(f"Нет чисел, кратных {i}")

multiple_numbers()
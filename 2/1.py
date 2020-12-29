def math_with_2_nums():
    exceptable = [
        "0",
        "+",
        "-",
        "*",
        "/"
    ]
    operation = ""
    msg = "Пожалуйста, выберите 1 из доступных действий:\n'+' - сложение\n'-' - вычитание\n'*' - умножение\n'/' - деление\nЧтобы завершить выполнение программы, введите '0' на этапе выбора операции"
    result = 0
    num_1 = int(input("Введите 1 число: "))
    num_2 = int(input("Введите 2 число: "))

    while operation not in exceptable:
        print(msg)

        operation = input(f"Выберите, что именно Вы хотите сделать с {num_1} и {num_2}: ")
    else:
        print(f"Вы выбрали операцию '{operation}'")

    while operation != "0":
        if (operation == "/") and (num_2 == 0):
            print("Деление на '0' запрещено! Выберите другое число")

            num_2 = int(input("Введите 2 число: "))
        else:
            if operation == "+":
                result = num_1 + num_2
            elif operation == "-":
                result = num_1 - num_2
            elif operation == "*":
                result = num_1 * num_2
            else:
                result = num_1 / num_2

            print(f"Результат: {result}")

            Math_with_2_nums()
            break
    else:
        print("Вы завершили выполнение программы. Хорошего дня!")

math_with_2_nums()
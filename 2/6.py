from random import randrange

def quess_the_num():
    right_answer = randrange(0, 100)
    user_answer = int(input("Введите число, которое, по Вашему предположению, сгенерировал ПК: "))

    for i in range(9):
        if user_answer == right_answer:
            print("Поздравляем! Вы правильно угадали сгенерированное число.")

            break
        elif user_answer < right_answer:
            user_answer = int(input("Ой, Ваше число Меньше сгенерированного. Попробоуйте ввести большее число: "))
        elif user_answer > right_answer:
            user_answer = int(input("Ой, Ваше число Больше сгенерированного. Попробойте ввести меньшее число: "))

    if right_answer != user_answer:
        print(f"Сожалеем, но Вы не смогли угадать сгенерированное число.\nПравильный ответ: {right_answer}")

quess_the_num()
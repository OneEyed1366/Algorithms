from random import randrange

class Quess_the_num():
  right_answer = randrange(0, 100)
  user_answer = int(input("Введите число, которое, по Вашему предположению, сгенерировал ПК: "))

  def __init__(self):
    for i in range(9):
      if self.user_answer == self.right_answer:
        print("Поздравляем! Вы правильно угадали сгенерированное число.")

        break
      elif self.user_answer < self.right_answer:
        self.user_answer = int(input("Ой, Ваше число Меньше сгенерированного. Попробоуйте ввести большее число: "))
      elif self.user_answer > self.right_answer:
        self.user_answer = int(input("Ой, Ваше число Больше сгенерированного. Попробойте ввести меньшее число: "))
      
    if self.right_answer != self.user_answer:
      print(f"Сожалеем, но Вы не смогли угадать сгенерированное число.\nПравильный ответ: {self.right_answer}")
        
  def __str__(self):
    return str(self.right_answer)

Quess_the_num()
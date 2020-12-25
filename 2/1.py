class Math_with_2_nums():
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

  def __init__(self):
    num_1 = int(input("Введите 1 число: "))
    num_2 = int(input("Введите 2 число: "))

    while self.operation not in self.exceptable:
      print(self.msg)

      self.operation = input(f"Выберите, что именно Вы хотите сделать с {num_1} и {num_2}: ")
    else:
      print(f"Вы выбрали операцию '{self.operation}'")
  
      while self.operation != "0":
        if (self.operation == "/") and (num_2 == 0):
          print("Деление на '0' запрещено! Выберите другое число")

          num_2 = int(input("Введите 2 число: "))
        else:
          if self.operation == "+":
            self.result = num_1 + num_2
          elif self.operation == "-":
            self.result = num_1 - num_2
          elif self.operation == "*":
            self.result = num_1 * num_2
          else:
            self.result = num_1 / num_2

          print(f"Результат: {self.result}")

          Math_with_2_nums()
          break
      else:
        print("Вы завершили выполнение программы. Хорошего дня!")

Math_with_2_nums()
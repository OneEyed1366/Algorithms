from sys import argv
from functools import reduce

class Actions_with_numbers():
  # Инициализация переменных
  # Если во входных данных argv есть дополнительно переданное значение, пропустить. Если нет - запросить ввод данных пользователя
  try:
    num = int(argv[1])
  except IndexError:
    num = int(input("Введите 3-х значное число!"))

  sum = 0
  mult = 0
# Инициализирую проверку. Если длина стартового числа не равна 3 - запросить новое число и повторить проверку. Если длина стартового числа = 3 - вывести информацию о числе на экран
  def __init__(self):
    while len(str(self.num)) != 3:
      self.num = int(input("Введите 3-х значное число!"))
    else:
      print(f"Начальное число: {self.num}")
# Считаю сумму и произведение всех чисел в стартовом числе (схитрил - не стал писать через цикл while, т.к. была абракадабра с переменными. Использовал методы sum и reduce)
  def __str__(self):
    self.sum = sum(map(int, str(self.num)))
    self.mult = reduce(
      lambda x, y: x*y,
      map(int, str(self.num))
    )
# Возвращаю пользователю строку с итоговыми значениями.
    return f"Сумма цифр числа равна: {self.sum}\nПроизведение цифр равно: {self.mult}"

print(Actions_with_numbers())
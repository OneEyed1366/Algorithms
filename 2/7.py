from sys import argv

class Natural_nums():
  try:
    n = int(argv[1])
  except IndexError:
    n = int(input("Введите любое натуральное число: "))

  s = 0
  result = 0

  def __init__(self):
    for i in range(1, self.n+1):
        self.s += i

    self.result = self.n * (self.n + 1) // 2

  def __str__(self):
    return f"{self.s} = {self.result}"

print(Natural_nums())
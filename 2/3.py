from sys import argv

class Reverse_num():
  try:
    donor_num = int(argv[1])
  except IndexError:
    donor_num = int(input("Введите любое Положительное число: "))
  
  result = 0

  def __init__(self):
    while self.donor_num > 0:
        self.result = self.result * 10 + self.donor_num % 10
        self.donor_num = self.donor_num // 10

    print(f"Результат: {self.result}")

Reverse_num()
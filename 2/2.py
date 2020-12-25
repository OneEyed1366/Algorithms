from sys import argv

class Nums():
  try:
    donor_num = int(argv[1])
  except IndexError:
    donor_num = int(input("Введите любое Положительное число: "))
  
  result = 0

  def __init__(self):
    for i in map(int, str(self.donor_num)):
      if i % 2 == 0:
        self.result += 1
    
    print(f"Число: {self.donor_num}, чётных чисел: {self.result}")

Nums()
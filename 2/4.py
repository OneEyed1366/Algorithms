from sys import argv

class Sum_of_element():
  try:
    donor_num = int(argv[1])
  except IndexError:
    donor_num = int(input("Введите Положительное число: "))
  
  result = 0
  current_state = 1

  def __init__(self):
    for i in range(self.donor_num):
        self.result += self.current_state
        self.current_state /= -2

    print(f"Результат: {self.result}")

Sum_of_element()
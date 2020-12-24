from sys import argv

class Find_the_number():
  try:
    all_nums = int(argv[1])
    num_to_find = int(argv[2])
  except:
    all_num = int(input("Введите любую последовательность чисел: "))
    num_to_find = int(input("Введите цифру, которую необходимо искать: "))
  
  result = 0
  
  def __init__(self):
    for i in map(int, str(self.all_num)):
      if i == self.num_to_find:
        self.result += 1
  
  def __str__(self):
    if self.result == 0:
      return f"Число {self.num_to_find} не встречается в последовательности {self.all_num}."
    else:
      return f"Число {self.num_to_find} встречается в последовательности {self.all_num} {self.result} раз."

print(Find_the_number())
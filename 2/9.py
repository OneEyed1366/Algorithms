class Max_sum_of_nums():
  msg = "Введите любое Положительнок число\n\nЧтобы завершить выполнение скрипта, введите '0': "
  donor_num = int(input(msg))
  result_sum = 0
  result_num = 0

  def __init__(self):
    while self.donor_num != 0:
        cycle_num = self.donor_num
        cycle_sum = 0
        while self.donor_num > 0:
            cycle_sum += self.donor_num % 10
            self.donor_num //= 10
        if cycle_sum > self.result_sum:
            self.result_sum = cycle_sum
            self.result_num = cycle_num

        self.donor_num = int(input(self.msg))

  def __str__(self):
    return f'Число {self.result_num} имеет максимальную сумму цифр: {self.result_sum}'

print(Max_sum_of_nums())
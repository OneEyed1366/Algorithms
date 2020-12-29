from random import randrange
# Запутался в 3 соснах. Постараюсь доделать в ближайшие 7 дней
def min_col_matrix():
    donor_matrix = [[randrange(-20, 20) for i in range(5)] for col in range(4)]
    max_num = 0
    result = 0

    for i in range(len(donor_matrix)):
        for n in range(len(donor_matrix[i])):
            if max_num < donor_matrix[i][n]:
                max_num = donor_matrix[i][n]

    print(max_num)

    # for i in range(len(donor_matrix)):
    #     print(donor_matrix[i])
    #     for c in range(len(donor_matrix[i])):
    #         print(min(donor_matrix[i]))

min_col_matrix()

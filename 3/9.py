from random import randrange
# Запутался в 3 соснах. Постараюсь доделать в ближайшие 7 дней
def min_col_matrix():
    donor_matrix = [[randrange(-20, 20) for i in range(5)] for col in range(4)]
    cols_list = [[donor_matrix[j][i] for j in range(len(donor_matrix))] for i in range(len(donor_matrix[0]))]
    mins_list = [min(i) for i in cols_list]
    result = max(mins_list)

    print("Матрица:")
    for row in donor_matrix: 
        for x in row: 
            print ( "{:4d}".format(x), end = "" ) 
        print ()

    print(f"Наибольший среди наименьших величин каждого столбца: {result}")

min_col_matrix()

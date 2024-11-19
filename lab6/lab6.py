matrix = [
    [30, 31, 36, 63, -2],
    [2, 24, -3, -7, -1],
    [45, 28, -98, 2, -8],
    [0, -1, -2, -3, 93],
    [11, 10, 72, 85, 66]
]

def bubble_sort_method(matrix):
    sorted_matrix = []
    for row in matrix:
        n = len(row)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if row[j] < row[j + 1]: 
                    row[j], row[j + 1] = row[j + 1], row[j]
        sorted_matrix.append(row)
    return sorted_matrix

def find_average_columns(sorted_matrix):
    n = len(sorted_matrix[0]) 
    column_averages = []
    for i in range(n):
        column_sum = 0
        for row in matrix:
            column_sum += row[i]
        column_averages.append(column_sum / len(matrix))
    return column_averages

def find_geometric_mean(column_averages):
    count = len(column_averages)
    prod = 1
    for i in range(count):
        prod *= column_averages[i]
    geometric_mean = abs(prod) ** (1 / count)
    return geometric_mean
        
sorted_matrix = bubble_sort_method(matrix)
column_averages = find_average_columns(sorted_matrix)

for row in sorted_matrix:
    formated_matrix = "".join(f"{el: <6}" for el in row)
    print(f"|{formated_matrix}|")

formated_columns = "".join(f"{el: <6}" for el in column_averages)
print(f"|{formated_columns}| - averages values of columns")

geometric_mean = round(find_geometric_mean(column_averages), 3)
print(f"geometric mean of columns is: {geometric_mean}")

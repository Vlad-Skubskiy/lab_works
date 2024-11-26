def sort_decorator(func):
    def wrapper(self, *args):
        self.matrix = self.bubble_sort_method()
        return func(self, *args)
    return wrapper

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def bubble_sort_method(self):
        sorted_matrix = []
        for row in self.matrix: 
            n = len(row)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if row[j] < row[j + 1]:  
                        row[j], row[j + 1] = row[j + 1], row[j]
            sorted_matrix.append(row.copy())
        return sorted_matrix

    def find_average_columns(self):
        n = len(self.matrix[0])  
        column_averages = []
        for i in range(n):
            column_sum = 0
            for row in self.matrix:
                column_sum += row[i]
            column_averages.append(column_sum / len(self.matrix))
        return column_averages

    def find_geometric_mean(self):
        column_averages = self.find_average_columns()
        count = len(column_averages)
        prod = 1
        for i in range(count):
            prod *= column_averages[i]
        geometric_mean = abs(prod) ** (1 / count)
        return f"the geometric mean of this columns is {round(geometric_mean, 2)}"
    
    @sort_decorator
    def addition(self, other_matrix):
        result = []
        n = len(self.matrix)
        m = len(self.matrix[0])
        
        if len(other_matrix.matrix) != n and len(other_matrix.matrix[0] != m):
            return "matrixes must have the same size"
        
        for i in range(n): 
            result_row = []
            for j in range(m): 
                sum_of_el = self.matrix[i][j] + other_matrix.matrix[i][j]
                result_row.append(sum_of_el)
            result.append(result_row)
            
        formatted_result = ""    
        for row in result:
            formatted_result += "".join(f"{el:<6}" for el in row) + "\n" 
        return formatted_result
    
    @sort_decorator
    def subtraction(self, other_matrix):
        result = []
        n = len(self.matrix)
        m = len(self.matrix[0])
        
        if len(other_matrix.matrix) != n or len(other_matrix.matrix[0]) != m:
            return "matrixes must have the same size"
        
        for i in range(n): 
            result_row = []
            for j in range(m): 
                sum_of_el = self.matrix[i][j] - other_matrix.matrix[i][j]
                result_row.append(sum_of_el)
            result.append(result_row)
            
        formatted_result = ""    
        for row in result:
            formatted_result += "".join(f"{el:<6}" for el in row) + "\n" 
        return formatted_result    
    @sort_decorator
    def multiplication(self, other_matrix):
        result = []
        n = len(self.matrix)
        m = len(self.matrix[0])
        p = len(other_matrix.matrix[0])


        if m != len(other_matrix.matrix):
            return "Size of columns in the first matrix must be the same as the number of rows in the second matrix."


        for i in range(n):
            result_row = []
            for j in range(p):
                elem_of_matrix = 0
                for k in range(m):
                    elem_of_matrix += self.matrix[i][k] * other_matrix.matrix[k][j]
                result_row.append(elem_of_matrix)
            result.append(result_row)


        formatted_result = ""
        for row in result:
            formatted_result += "".join(f"{el:<6}" for el in row) + "\n"
        return formatted_result
    
    @sort_decorator
    def __str__(self):
        column_averages = self.find_average_columns()
        formatted_columns = "".join(f"{el:<6}" for el in column_averages)
        result = ""
        for row in self.matrix:
            formatted_row = "".join(f"{el:<6}" for el in row)
            result += f"|{formatted_row}|\n"
        result += f"|{formatted_columns}|"     
        return f"{result} - average values of columns"
    
matrix = [
    [30, 31, 36, 63, -2], 
    [2, 24, -3, -7, -1],
    [45, 28, -98, 2, -8],
    [0, -1, -2, -3, 93],
    [11, 10, 72, 85, 66]
]
matrix_1 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


matrix1 = Matrix(matrix)
matrix2 = Matrix(matrix_1)
print(f"Matrix1: \n{matrix1} \n")
print(f"Matrix2: \n{matrix2} \n")
print(matrix1.multiplication(matrix2))    


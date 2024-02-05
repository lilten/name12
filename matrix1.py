import random

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(0, 999))
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result


matrix1 = create_matrix(10, 10)
matrix2 = create_matrix(10, 10)


print("matrix1:")
for row in matrix1:
    print(row)

print("matrix2:")
for row in matrix2:
    print(row)


result = add_matrices(matrix1, matrix2)


print("result:")
for row in result:
    print(row)

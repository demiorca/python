# Задание 1

class Matrix:
    def __init__(self, matrices):
        self.matrices = matrices

    def __str__(self):
        matrix1 = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrices[0]])
        matrix2 = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrices[1]])
        matrix_sum = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.__add__()])
        return f'Матрица 1:\n{matrix1}\nМатрица 2:\n{matrix2}\nСумма матриц:\n{matrix_sum}'

    def __add__(self):
        matrix = []
        for i in range(len(self.matrices[0])):
            matrix.append([])
            for j in range(len(self.matrices[0][0])):
                matrix[i].append(self.matrices[0][i][j] + self.matrices[1][i][j])
        return matrix


m3_3 = Matrix([[[14, 41, 7],
                [2, 10, 81],
                [13, 8, 4]],
               [[77, 12, 5],
                [92, 64, 1],
                [9, 23, 32]]])

m2_3 = Matrix([[[14, 41, 7],
                [2, 10, 81]],
               [[77, 12, 5],
                [92, 64, 1]]])

m3_2 = Matrix([[[14, 41],
                [2, 10],
                [13, 8]],
               [[77, 12],
                [92, 64],
                [9, 23]]])

m2_2 = Matrix([[[14, 41],
                [2, 10]],
               [[77, 12],
                [92, 64]]])

print(f'Суммирование матриц 3 на 3:\n{m3_3}')
print()
print(f'Суммирование матриц 2 на 3:\n{m2_3}')
print()
print(f'Суммирование матриц 3 на 2:\n{m3_2}')
print()
print(f'Суммирование матриц 2 на 2:\n{m2_2}')

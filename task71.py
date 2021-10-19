class Matrix():

    def __init__(self, contains):
        self.contains = contains
        self.rows = len(self.contains)
        self.columns = len(self.contains[0])

    def __iter__(self):
        return (el for el in self.contains)
    #Дополнительная функция, проверяющая является ли объект матрицей
    def check(self):
        flag = True
        if type(self.contains) == list:
            flag == True
        for row in self.contains:
            if len(row) != self.columns:
                flag = False
                break
        return flag

    def __str__(self):
        if self.check() == True:
            for el in self:
                print("|", end="")
                for elt in el:
                    print(("{:5}".format(str(elt))), end="")
                print("|")

            return f"Матрицa содержит строк: {self.rows} и столбцов: {self.columns}"
        else:
            return "Объект не является матрицей. Строки разной длины."

    def __add__(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            new_matrix = matr_1.contains
            for i in range(matr_1.rows):
                for k in range(matr_1.columns):
                    new_matrix[i][k] = matr_1.contains[i][k] + matr_2.contains[i][k]
            new_matrix = Matrix(new_matrix)
            return new_matrix
        else:
            print("Сложение невозможно, матрицы разной размерности")


matr_1 = Matrix([[13, 13], [22, 15], [3, 2]])
matr_2 = Matrix([[1, 2], [4, 134], [3, 12]])

print(matr_1)
print(matr_2)
print(matr_1 + matr_2)


# Квадратную матрицу А произвольного размера умножте на квадратную матрицу B эквивалентного размера.


# создаем две матрицы
m = [[1,2,3,4],[4,5,6,7],[7,8,9,8],[7,8,9,8]]
n = [[1,2,3,5],[4,5,6,2],[7,8,9,3],[7,8,9,8]]


a = 0
B = 0
C = []
X = []
for k in range(len(m)): # определяет все строки результирующей матрицы
    for j in range(len(m)):#определяем одну строку результирующей матрицы
        for i in range(len(m[0])): #определяем одно значение результирующей матрицы
            a = m[i][j]*n[k][i]
            B += a
        C.append(B)
    X.append(C[k:len(m)+k])
    print(X[k])
print('Итоговое произведение двух матриц')

import math as m
import random
import numpy as np
from scipy import linalg 

def roots():
    a= int(input("Wprowadz współczynnik a: "))
    b= int(input("Wprowadz współczynnik b: "))
    c= int(input("Wprowadz współczynnik b: "))

    delta = ((b**2) - (4*a*c))
    x=[]
    if delta == 0:
        x.append(-b / (2*a))
    elif delta > 0:
        x.append((-b + m.sqrt(delta)) / (2*a))
        x.append((-b - m.sqrt(delta)) / (2*a))
    else:
        x.append("Rzeczywisty pierwiastek nie istnieje")
    print(x)

def sorter():
    numbers = [random.randint(0, 100) for x in range(50)]
    test_numbers = numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
             if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    test_numbers.sort(reverse=True)
    print(numbers)
    print(test_numbers)
    if numbers == test_numbers:
        print("Posortowane")
    else:
        print("Błąd")


def scalar():
    a = [1,2,12,4]
    print(a)
    b = [2,4,2,8]
    print(b)
    product = sum([a[x] * b[x] for x in range(len(a))])
    print(product)

def matrix_add():
    matrix_1 = [([random.randint(0,100) for i in range(128)]) for j in range(128)]
    #print(matrix_1)
    matrix_2 = [([random.randint(0,100) for i in range(128)]) for j in range(128)]
    #print(matrix_2)
    results = [([matrix_1[i][j] + matrix_2[i][j] for i in range(128)]) for j in range(128)]
    print(results)

def matrix_multiply():
    matrix_1 = [([random.randint(0, 100) for i in range(8)]) for j in range(8)]
    print(matrix_1)
    matrix_2 = [([random.randint(0, 100) for i in range(8)]) for j in range(8)]
    print(matrix_2)
    results =  [([0 for i in range(8)]) for j in range(8)]

    for i in range(8):
        for j in range(8):
            for k in range(8):
                results[i][j] += matrix_1[i][k] + matrix_2[j][k]
    print(results)


def determinant():
    matrix = [([random.randint(0, 5) for i in range(5)]) for j in range(5)]
    matrix = np.array(matrix, dtype='float64', copy=True)
    print("Matrix: ")
    print(matrix)
    test_det = np.linalg.det(matrix)
    print("Verification determinate: ")
    print(test_det)
    lenght = len(matrix)
    s = 0
    if lenght != len(matrix[0]):
        return ValueError

    for i in range(0, lenght):
        maxElement = abs(matrix[i, i])
        maxRow = i
        for k in range(i + 1, lenght):
            if abs(matrix[k, i]) > maxElement:
                maxElement = abs(matrix[k, i])
                maxRow = k
        if maxRow != i:
            s += 1

        for k in range(i, lenght):
            matrix[i, k], matrix[maxRow, k] = matrix[maxRow, k], matrix[i, k]

        for k in range(i + 1, lenght):
            c = -matrix[k, i] / matrix[i, i]
            for j in range(i, lenght):
                if i == j:
                    matrix[k, j] = 0
                else:
                    matrix[k, j] += c * matrix[i, j]
    det = (-1)**s

    for i in range(lenght):
        det *= matrix[i, i]
    print("Calculate determinate:")
    print (det)




if __name__ == '__main__':
    #roots()
    #sorter()
    #scalar()
    #matrix_add()
    #matrix_multiply()
    determinant()

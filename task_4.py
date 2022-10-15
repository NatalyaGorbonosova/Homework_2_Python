# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек 
# и находит расстояние между ними в N-мерном пространстве.
import math
def coordinats_point(point, n):
    array = []
    for i in range(1, n + 1):
        array.append(float(input(f'Введите {i} - ю координату точки {point}: ')))
    return array
def sum_sqrt_coordinat(point_first, point_second):
    sum_coord = 0
    for i in range(len(point_first)):
        sum_coord += (point_second[i] - point_first[i])**2
    return sum_coord
try:
    N = int(input('Введите размерность пространства: '))
    point_A = coordinats_point('A', N)
    point_B = coordinats_point('B', N)
    print(point_A)
    print(point_B)
    distant = round(math.sqrt(sum_sqrt_coordinat(point_A, point_B)), 2)
    print(f'Расстояние между точками равно: {distant}')
except: print('Вводите числа!')

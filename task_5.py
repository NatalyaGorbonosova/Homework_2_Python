# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . 
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, проверяем это утверждение 100 раз, 
# с помощью модуля time выводим на экран , сколько времени отработала программа.

from random import randint
import random
import time
def predict(n):
    list = []
    for i in range(n):
        list.append(random.choice([True, False]))
    return list
def left_side(n, list):
    for i in range(n - 1):
        if (list[i] or list[i+1]): res = True
        else: res = False
    return not(res)
def right_side(n, list):
    for i in range(n-1):
        if (not(list[i]) and not(list[i + 1])): res = True
        else: res = False
    return res
def list_for_print(list):
    list_new = []
    for i in list:
        if i == True: list_new.append(1)
        else: list_new.append(0)
    return list_new

try:
    N = randint(5, 25)
    tic = time.perf_counter()
    for i in range(1, 101):
        list_pred = predict(N)
        list_print = list_for_print(list_pred)
        if left_side(N, list_pred) == right_side(N, list_pred):
            print(f'{i} {list_print} Утверждение истино')
        else: print(f'{i} {list_print} Утверждение ложно')
    toc = time.perf_counter()
    print(f'Время выполнения программы: {toc - tic} секунд')

except: print('Something is wrong')
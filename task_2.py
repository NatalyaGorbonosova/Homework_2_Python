# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def factorial(n):
    if n==1: return 1
    else: return n*factorial(n-1)
try:
    N = int(input('Введите целое число: '))
    mult_arr = []
    for i in range(1, N + 1):
        mult_arr.append(factorial(i))
    print(mult_arr)
except: print('Введите целое число!')
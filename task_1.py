# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. 
# Через строку нельзя решать.
from decimal import Decimal
def sum_numbers(num):
    sum_num = 0
    while num > 0:
        if num // 10 == 0:
            sum_num += num
            return sum_num
        else:
            sum_num += num % 10
            num = num //10
            
try:
    number = Decimal(input('Введите число: '))
    if number < 0: number *= -1
    while (number % 1) != 0: 
       number*=10
    sum = sum_numbers(number)
    print(sum)
except: print('Введите именно число')
# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
#  вхождений одной строки в другой. COUNT или FIND нельзя юзать! говорил же на семинаре.
def count_str(str_main, str_find):
    count = 0
    for i in range(len(str_main)):
        if str_main[i: i + len(str_find)] == str_find: count += 1
    return count
try:
    str1 = input('Введите строку: ')
    str2 = input('Введите что ищите: ')
    print(count_str(str1, str2))
except: print('что-то пошло не так')
# Задание 1
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))
sum_even = 0
sum_odd = 0
sum_multiple_of_9 = 0
count_even = 0
count_odd = 0
count_multiple_of_9 = 0
for number in range(start, end + 1):
    if number % 2 == 0:
        sum_even += number
        count_even += 1
    else:
        sum_odd += number
        count_odd += 1
    if number % 9 == 0:
        sum_multiple_of_9 += number
        count_multiple_of_9 += 1
if count_even > 0:
    average_even = sum_even / count_even
else:
    average_even = 0
if count_odd > 0:
    average_odd = sum_odd / count_odd
else:
    average_odd = 0
if count_multiple_of_9 > 0:
    average_multiple_of_9 = sum_multiple_of_9 / count_multiple_of_9
else:
    average_multiple_of_9 = 0
print(f'Сумма четных чисел: {sum_even}')
print(f'Сумма нечетных чисел: {sum_odd}')
print(f'Сумма чисел, кратных 9: {sum_multiple_of_9}')
print(f'Среднеарифметическое четных чисел: {average_even}')
print(f'Среднеарифметическое нечетных чисел: {average_odd}')
print(f'Среднеарифметическое чисел, кратных 9: {average_multiple_of_9}')
# Задание 2
length = int(input("Введите число: "))
symbol = input("Введите символ: ")
for i in range(length):
    print(symbol)
# Задание 3
while True:
    a = int(input('Введите число '))
    if a > 0:
        print('Number is positive')
    elif a < 0:
        print('Number is negative')
    else:
        print('Number is equal to zero')
    if a == 7:
        print('Good bye!')
        exit()
# Задание 4
arr = []
while True:
    number = int(input('Введите число'))
    arr.append(number)
    if number == 7:
        print('Сумма введённых чисел:', sum(arr))
        print('Максимальное число:', max(arr))
        print('Минимальное число:', min(arr))
        exit()
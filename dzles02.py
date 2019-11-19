import random
# 1.	Написать программу, которая будет складывать, вычитать, умножать или делить
# два числа. Числа и знак операции вводятся пользователем. После выполнения
# вычисления программа не должна завершаться, а должна запрашивать новые данные
# для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
# снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

while True:
    FIRST_NUMBER = int(input('Введите первое число: '))
    SECOND_NUMBER = int(input('Введите второе число: '))
    DIGIT = input('Выберите знак операции: + - * / 0 ')
    if DIGIT == '0':
        break
    elif DIGIT == '+':
        print(FIRST_NUMBER + SECOND_NUMBER)
    elif DIGIT == '-':
        print(FIRST_NUMBER - SECOND_NUMBER)
    elif DIGIT == '*':
        print(FIRST_NUMBER * SECOND_NUMBER)
    elif DIGIT == '/':
        if SECOND_NUMBER == 0:
            print('Деление не возможно!')
        else:
            print(FIRST_NUMBER / SECOND_NUMBER)
    else:
        print('Вы ввели недопустимый знак.Попробуйте снова')


# 2.Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

NUMBER = int(input('Введите число: '))
EVEN = 0
ODD = 0
while NUMBER > 0:
    if NUMBER % 2 == 0:
        EVEN += 1
    else:
        ODD += 1
    NUMBER = NUMBER // 10

print(f' Четных цифр: {EVEN} и нечетных: {ODD}.')

# 3.Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран. Например, если введено число 3486,
#  то надо вывести число 6843.

MY_NUMBER = int(input('Введите число: '))
NEW_NUMBER = 0
while MY_NUMBER != 0:
    NEW_NUMBER = MY_NUMBER % 10
    print(NEW_NUMBER, end="")
    MY_NUMBER = MY_NUMBER // 10

Рекурсия
MY_NUMBER1 = int(input('Введите число: '))
def numb(a):
    if len(str(a)) == 1:
        return a
    else:
        print(a % 10, end="")
        return numb(a // 10)
print(numb(MY_NUMBER1))


# 4.Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

L = []
N = int(input('Введите количество элементов: '))
M = 1
while len(L) != N:
    L.append(M)
    M = M / -2
print(f'Сумма элементов равно: {sum(L)}')


# 5.Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

for char in range(32, 128):
    print(char, chr(char), end=" ")
    if char < 100:
        print(" ", end="")
    if (char - 1) % 10 == 0:
        print()

# 6.В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.

SECRET_NUMBER = random.randint(1, 100)
USER_NUMBER = None
USER_COUNT = 0
MAX_COUNT = 10
while USER_NUMBER != SECRET_NUMBER:
    USER_NUMBER = int(input('Введите число: '))
    USER_COUNT += 1
    if USER_COUNT == MAX_COUNT:
        print(f"Вы проиграли. Загаданное число: {SECRET_NUMBER}.")
        break
    if USER_NUMBER < SECRET_NUMBER:
        print('Ваше число меньше загаданного')
    elif USER_NUMBER > SECRET_NUMBER:
        print('Ваше число больше загаданного')
    else:
        print('Вы угадали число!')

# 7.Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
#  где n - любое натуральное число.

N = int(input('Введите число: '))

def result1(n):
    if n == 1:
        return 1
    return n + result1(n - 1)
print(result1(N))


RESULT2 = int(N * (N + 1) / 2)
print(RESULT2)

# 8.Посчитать, сколько раз встречается определенная цифра в введенной
#  последовательности чисел. Количество вводимых чисел и цифра,
#  которую необходимо посчитать, задаются вводом с клавиатуры.

COUNT_NUMBERS = int(input('Сколько чисел вы хотите ввести: '))
NUMBER_FOR_SEARCH = input('Введите цифру, которую нужно посчитать: ')
COUNT = 0
NUM = []
while COUNT != COUNT_NUMBERS:
    NUMBERS = (input("Введите число: "))
    COUNT += 1
    NUM.append(NUMBERS)

NUM = str(NUM)
print(f'В последовательности чисел {NUM} цифра {NUMBER_FOR_SEARCH}'
      f' встречается {NUM.count(NUMBER_FOR_SEARCH)} раз(а)')

# 9. Среди натуральных чисел, которые были введены, найти
# наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def counter(quantity, n, highest_number, sum_hn):
    sum = 0
    number = input("Введите число: ")
    for i in number:
        sum += int(i)
    if sum > sum_hn:
        sum_hn = sum
        highest_number = number
    n += 1
    if n == quantity:
        return print(f"Наибольшее число по сумме цифр: {highest_number}, сумма его цифр: {sum_hn}")
    else:
        return counter(quantity, n, highest_number, sum_hn)


QUANTITY = int(input("Введите количество чисел:"))
N = 0
HIGHEST_NUMBER = 0
SUM_HN = 0

counter(QUANTITY, N, HIGHEST_NUMBER, SUM_HN)

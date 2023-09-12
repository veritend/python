# name_first = "NIKITA"
# print("Hello,", name_first)
# age = 20
# print(age)
# import re
# import re
# import re


# a = 5
# print(a)
# print(type(a))
# b = "6"
# print(a)
# print(type(a))
# print(a + int(b))

# a = 4
# b = 5
# print(a)
# print(id(a))
# a = b
# print(a)

# a = b = c = 5
# a, b, c, = 2, "Hello", 4.5
# print(a, b, c)
# print(id(a))
# print(id(b))
# print(id(c))
#
# PI = 3.14
# print(PI)

# print("строка символов")

# print("Документ \r\"file.py\" находится по заданному пути: \nD:\\python\\file.py")


# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)

# print(5555555555558978789498)
# print(5.555555555558978789498)

# a = 5
# b = 7
# c = 3
# d = a + b + c
# print("Сумма:", d)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", d/3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num +=5

# n = 4321
# a = n // 1000
# b = (n // 100) % 10
# c = (n // 10) % 10
# d = n % 10
# print(a)
# print(b)
# print(c)
# print(d)
# print(d, c, b, a, sep='')
# print(d*1000 + c * 100 + b * 10 + a)

# 12345
# Найти произведение его цифр
# найти среднее арифметическое цифр числа


# a = 1
# b = 2
#
# print("a:", a)
# print("b:", b)
#
# a, b = b, a
# # c = a  # c =1
# # a = b  # a =2
# # b = c  # b =1
#
# print("a:", a)
# print("b", b)

# Функции явного преобразования типов:
# int()
# str()
# float()
# bool()

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# res2 = num1 + str(num2)
# print(res)
# print(res2)
# a = 3.891
# a = round(a, 2)  # округление - round
# print(a)
# print(int(3.891))
# print(type(a))

# num1 = "5.2"
# num2 = 10
# c = float(num1) + num2
# print(bool(0))

# name = "Виктор"
# age = 26
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="", end="\n\n")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")

# name = input("Введите имя: ")
# print("Вас зовут", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# #  num = int(num)
# #  power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите первое число: "))
# num3 = int(input("Введите первое число: "))
# num4 = int(input("Введите первое число: "))
#
# sum1 = num1 + num2
# sum2 = num3 + num4
#
# del1 = str(round((sum1 / sum2), 2))
# print("Ответ: ", del1)

# b1 = True
# b2 = False
#
# print(b1 + 5)
# print(b2 + 5)

# print(bool("Python"))
# print(bool(""))  # false
# print(bool(9))
# print(bool(0))  # false
# print(bool(None))  # false
#
# test = None
#
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(7 == 5)
# print(7 != 5)
# print(7 > 5)
# print(7 < 5)
# print("привет" == "Привет")

# print(5-3 == 2 and 1 + 3 == 4)
# print(5-3 == 2 and 1 + 3 < 4)
#
# print(5-3 == 2 or 1 + 3 < 4)
# print(5-3 == 2 or 1 + 3 < 4)


# print(not 9 - 5)
# print(not 9 - 9)
#
# a = 0
# print(not a)

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)


# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("a == b")

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = int(input("Введите длину первой стороны: "))
# b = int(input("Введите длину второй стороны: "))
# c = int(input("Введите длину третьей стороны: "))
#
# if a == b == c:
#     print("треугольник равносторонний")
# elif a == b or b == c or c == a:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день -", end=" ")
#     if day == 6:
#         print("Суббота")
#     else:
#         print("Воскресение")
# else:
#     print("Такого дня недели не существует")


# month = int(input("Введите номер месяца: "))

# if 3 <= month <= 5:
#    print("Весна")
# elif 6 <= month <= 8:
#    print("Лето")
# elif 9 <= month <= 11:
#   print("Осень")
# elif month == 12 or 1 <= month <= 2:
#    print("Зима")
# else:
#    print("Такого месяца не существует")#

# dz


# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if a <= 99 or a >= 100:
#     if 11 <= a <= 14:
#         print(a, "копеек")
#     else:
#         kop = kop % 10  # 3
#         print(a, end=" ")
#     if kop == 1:
#         print("копейка")
#     elif 2 <= kop <= 4:
#         print("копейки")
#     else:
#         print("копеек")
# else:
#     print("некорректное значение")


# match выражение:
#     case шаблон_1:
#         действие_:
#     case шаблон_2:
#         действие_2:
#     case
#         шаблон_3:
#         действие_3:
#     case _:
#         действие по умолчанию

# password = "user"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case 'moderator':
#         print("Модератор")
#     case _:
#         print("Пароль не верен")


# day = 'среда'
# time = 14
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресение':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабоче время")


# a, b = 30, 20
# minim = a if a < b else b
# print(minim)


# a, b = 30, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = int(input("Введите делимое"))
# b = int(input("Введите делитель"))
# print("на ноль делить нельзя" if b == 0 else a / b)

# tru ...except


# try:
#     n = int(input("Введите целое число: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Что-то пошло не так")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# print("Код далее")


# try:
#     n = int(input("Введите целое число: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так")
#     print("Нельзя делить на ноль")
# else:
#     print("Все нормально, Ввели числа", n, "и", m)
# finally:
#     print("Конец программы")
#
# print("\nКод далее")

# n = (input("Введите целое число: "))
# m = (input("Введите целое число: "))
# try:
#     print(int(n) + int(m))
# except (ValueError, ZeroDivisionError):
#     print("", n, "", m)
# finally:
#     print("Конец программы")

# n = (input("Введите целое число: "))
# m = (input("Введите целое число: "))
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


#  Циклы

# i = 0
# while i < 20:
#     print("i= ", i)
#     i += 2


# p = 0
# while p < 20:
#     if p % 2 == 0:
#         print("i", p)
#     p += 1

# n = int(input("Укажите количество символов: "))
#
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     print(a, end=" ")
#     if a % 2:
#         res += a
#     a += 1
# print("\n", res)


# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     i += 1


# while True:
#     n = int(input("Введите положительное число:"))
#     if not n < 0:
#         break


# res = 1
#
# while True:
#     n = int(input("Введите целое число: "))
#     if n == 0:
#         break
#     res *= n
#
# print(res)


# i = 0
# while i < 3:
#     if i == 2:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i=", i)
#
# print("За циклом")


# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j,"=", i*j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
#
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
#
# while i < 50:
#     j = 0
#     while j < 50:
#         if i == j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(end=" ")
#         j += 1
#     print("*")
#     i += 1


# for element in collection
#  тело цикла

# for i in 'Hello':
#     print(i)


# for color in 'red', 'orange', 'yellow', 'green':
#     print(color)

# print(range(9))
#  range(start,stop,step)

# for i in range(2, 9, 1):
#     print(i, end=" ")
#
# print()
# i = 2
# while i <= 9:
#     print(i, end=" ")
#     i += 1


# a = int(input("Введите целое число: "))
# b = 1
# for i in range(b, a+1):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(1, 10):
#     print(i, i, end="")


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done!")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# symbol = input("Введите символ: ")
# for i in range(h):
#     for j in range(w):
#         if (i == 0) or (j == 0) or (i == h-1) or (j == w-1):
#             print(symbol, end="")
#         else:
#             print(end=" ")
#     print()


# w = [letter * 2 for letter in "Hello"]
# print(w)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in 'Hello':
#     print(i)


#   Списки

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(nums[1])
# print(nums[-1])
#
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)
# print(len(nums))

# s = [5] * 6
# print(s)
# print(type(s))
#
# b = list("Hello")
# print(b)
# print(type(b))
#
# c = s + b
# print(c)

# n = list(range(2, 10, 2))
# # n2 = [2, 4, 6, 8]
# # print(n)
# # print(n2)
# # if n == n2:
# #     print("списки равны")
# # else:
# #     print("списки разные")


# генератор списков


# n = 5
# a = [i ** 2 for i in range(n)]
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)


# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('-> '))
# print(a)


# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)


# a = [9, 8, 6, 4, 3]
# for i in range(len(a)):
#     print(i, "=", a[i])
# print()
#
# for i in a:
#     print(i)


# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print(s)

# s = 0
# b = 0
# n = list(range(21, 41))
# print(n)
# for i in n:
#     if i % 2 == 0:
#         s += 1
#     if i % 2 != 0:
#         b += i
# print(s)
# print(b)


# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
#
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         k += 1
#     s += a[i]
# print(s / k)


# a = [6, 3, 0, 8, 2]
# #
# # a[0], a[-1] = a[-1], a[0]
# #
# # print(a)


# срез
# список[start:stop:step]


# a = [6, 3, 0, 8, 2, 7]
# print(a[1:4])
# print(a[0:-1:2])
# print(a[6:20])
#
# b = a[10:20]
# print(b)


# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1:])
# print(s[-1::])
# print(s[3:4:])
# print(s[-3::])
# print(s[4:1:-1])
# print(s[2:5:])
#
#
# a = "Hello"
# print(a[1:3])
#
# print(list(a))


# a = [6, 3, 0, 8, 2, 7]
# print(a[:3])
# a[1:3] = [1, 1, 1, 1]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)
# del a[2]
# print(a)
# del a[2:5]
# print(a)

# b = 0
# del b
# print(b)


# Методы списка

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.append([99, 2])  # добавляет элемент в конец списка
# print(a)
# a.extend([5, 6, 7]) # добавляет список элементов в конец существующего списка
# print(a)
# a.extend("add")
# print(a)


# a = []
# # a.extend([i**2 for i in range(1, 11)])
# # [a.extend([i**2]) for i in range(1, 11)]
# for i in range(1, 11):
#     a.extend([i ** 2])
# print(a)


# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.insert(2, 100)  # добавляет элемент списка (второй параметр - добавляемое значение) в определенное место (первый
# # параметр - индекс).
# print(a)


# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# print(s)


# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x,"не делиться на 3 без остатка")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
#
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# s = 1
# for i in range(len(a)):
#     a.insert(s, b[i])
#     s += 2
# print(a)


# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)


# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# a.remove(2)  # удаляет первый по найденному совпадению элемент из списка по значению
# print(a)
# last = a.pop()  # удаляет последний элемент из списка (без параметров) и возвращает удаленный элемент
# second = a.pop(0)
# print(a)
# print(last)
# print(second)
# a.clear()  # очищает список
# print(a)

# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# num = a.count(8)  # считает количество заданных значений в списке
# print(num)
#
# b = 8
# ind = a.index(b, 4, -1)  # возвращает положение первого индекса по заданному значению
# print(ind)


# c = [1, 2, 3]
# d = c.copy()
# print("c =", c)
# print("d =", d)
# c.append(4)
# d.insert(0, 100)
# print(c)
# print(d)


# a = [5, 2, 9, 2, 1, 4, 3, 2, 4]
# a.reverse()  # пере вернули элементы списка в обратном порядке
# print(a)


# a.sort(reverse=True)  # отсортировали список по возрастанию
# print(a)

# b = sorted(a)
# print(a)
# print(b)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len)
# print(s)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(0, 5))
# print(random.randrange(5, 15, 2))


# import random as r
#
# print(r.random())
# print(r.randint(0, 5))
# print(r.randrange(5, 15, 2))


# from random import randint, randrange, random
#
# print(random())
# print(randint(0, 5))
# print(randrange(5, 15, 2))


# from random import randint, randrange, random as rr
#
# print(rr())
# print(randint(0, 5))
# print(randrange(5, 15, 2))


# from random import *
#
# print(random())
# print(randint(0, 5))
# print(randrange(5, 15, 2))
# print(round(uniform(10.5, 25.5), 2))
#
#
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(choice(city_list))
# print(choices(city_list, k=3))
#
# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=5))
#
# shuffle(s)
# print(s)


# from random import randint
#
# mas = [randint(0, 20) for i in range(5)]
# print(mas)

# функции агрегирования

# lst = [7, 12, 20, 18, 9]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# from random import randint
#
# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# max_1 = max(mas)
# print(max_1)
# mas.remove(max_1)
# mas.insert(0, max_1)
# print(mas)
#
#
# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# # lst.sort(reverse=True)
# # print(lst)
#
# min_1 = min(lst)
# print(min_1)
#
# ind = lst.index(min_1)
#
# del lst[:ind]
# print(lst)


# lst = []
# if len(lst) == 0:
#     print('Список пустой')
#
# if not lst:
#     print('!!! Список пустой')

# print(bool(lst))

# from random import randint
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
#
# print("Первый список: ", a)
# print("Второй список: ", b)

# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#
# print(c)


# print("Элементы общие для двух списков: ")
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
#         continue
#
# print(c)


#    дописать

# from random import randint
# k = int(input("Размер списка: "))  # 5
# s = []
# while len(s) < k:
#     w = randint(0, k-1)
#     if w not in s:
#         s.append(w)
# print(s)


# from random import randint
# k = int(input("Размер списка: "))  # 5
# s = []
# for i in range(10):
#     while len(s) < k:
#         w = randint(0, k-1)
#         if w not in s:
#             s.append(w)
# print(s)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(len(m))
# print(m)
# print(m[1][2])
#
# a = [2, 'Hello', 5]
# print(a[1][1])

# for row in range(len(m)):
#     #  print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()

# for row in m:
# #     # print(row)
# #     for x in row:
# #         print(x**2, end="\t\t")
# #     print()
# matrix = [[0 for x in range(5)] for y in range(3)]
# matrix = []
# for y in range(3):
#     new_row = []
#     for x in range(5):
#         new_row.append(0)
#     matrix.append(new_row)

# matrix = [[0 for x in range(5)] for y in range(3)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# for x, y, z in [[1, 2, 1], [3, 4, 2], [5, 6, 3], [7, 8, 4]]:
#     print(z, ")", x, "+", y, "=", x + y)

# from random import randint
#
# matrix = [[randint(1, 30) for x in range(5)] for y in range(3)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# matrix = [[randint(-20, 10) for x in range(3)] for y in range(4)]
# print(matrix)
# s = 0
# for row in matrix:
#     for j in row:
#         print(j, end="\t\t")
#         if j < 0:
#             s +=1
#     print()
# print("Количество отрицательных элементов: ", s)

# n = int(input("n = "))
# m = [[randint(0, 100) for x in range(n)] for y in range(n)]
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
# t = m[0][0]
# for k in range(n):
#     if t < m[k][k]:
#         t = m[k][k]
# print(t)

# github.com зарегистрироваться

# print("проверка репозитория")

# import math
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.pi
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)
#
# print(dir(math))

# import math as m

# from math import *


# from math import sqrt
#
# num1 = sqrt(4)
# print(num1)

# from math import pi
#
# r = int(input("Введите радиус окружности:"))
# print(round(r*pi*2, 2))


# import time
# import locale

# locale.setlocale(locale.LC_ALL, "ru")
#
# # print(dir(time))
#
# s = time.time()
# print(s)
#
# local = time.ctime()
# print(local)
#
# res = time.localtime()
# print(res)
#
# print(res.tm_mday, ".0", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("%d.%m.%Y"))
# print(time.strftime("Сегодня: %B %d, %Y.", time.localtime()))


# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print("Программа завершена")

# text = input("Название напоминания: ")
# t = float(input("Через сколько минут:"))
# t = t * 60
# time.sleep(t)
# print(text)


# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# def hello(name):
#     print("Hello", name)
#
#
# hello("Irina")
# hello("Ivan")


# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# # get_sum("2", "5")
# print(res)

# import math
#
#
# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "@")


# x = int(input("Введите первое число: "))
# y = int(input("Введите второе число: "))
#
#
# def gg(a, b):
#     if a > b:
#         return a - b
#     if a < b:
#         return a + b
#     return "a = b"
#
#
# gg(x, y)
# print(gg(x, y))


# def cub(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cub(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     a = lst.pop()
#     b = lst.pop(0)
#     lst.append(b)
#     lst.insert(0, a)
#
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(10, 15))
#
#
# a = 10
# b = 5
#
# if func(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше второго")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a=0, b=0, c=1, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# e = 2
# print(get_sum(1, 5, d=e))
# print(get_sum())


# def display_info(name, age):
#     print("Name: ", name, "\nAge: ", age, end="\n\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")


# s1 = []
# s2 = []
# y = 0
# n = int(input("Введите длину списка: "))
# for num in range(n):
#     x = int(input("Введите элемент списка: "))
#     s1.append(x)
#     if x > 0:
#         s2.append(x)
#     if x > u:
#         u = x
#     else:
#         ...
# print("Список: ", s1)
# print("Новый список, состоящий из положительных чисел: ", s2)
# print("Наибольший элемент списка: ", y)


# s3 = []
# d = int(input("Введите элементы списка: \nn ="))
# for num in range(d):
#     y = int(input("-> "))
#     s3.append(y)
# k = int(input("Введите индекс: \nk = "))
# c = int(input("Введите значение: \nc = "))
# s3.insert(k, c)
# print(s3)


# s4 = []
# g = False
# f = int(input("Введите длину списка: "))
# for num in range(f):
#     z = int(input("Введите элемент списка: "))
#     s4.append(z)
# ch = int(input("Введите число: \nch = "))
# for num in range(f):
#     if ch == num:
#         print("Число присутствует в элементах списка")
#         g = True
# if g == False:
#     print("Числа нет в элементах списка")

# from random import randint
# s = []
# y = 0
# for num in range(20):
#     x = randint(0, 100)
#     s.append(x)
#     y += x
# print(s)
# print("Summa: ", y)

# from random import randint
# s = []
# p = 6
# for num in range(p):
#     for num1 in range(p):
#         x = randint(0, 10)
#         s.append(x)
#         print(x, end="\t\t")
#     print()
# print()
# s1 = [0, 8, 10, 0, 10, 7]
# print(s1)
# print()
# y = 0
# t = 0
# for num2 in range(p):
#     if num2 % 2 == 0 or num2 == 0:
#         for num3 in range(p):
#             del s[t]
#             s.insert(t, s1[num3])
#             print(s[t], end="\t\t")
#             t += 1
#         print()
#     else:
#         for num4 in range(p):
#             print(s[t], end="\t\t")
#             t += 1
#         print()

# def summa(a, b, c):
#     sm = a + b + c
#     avg = sm / 3
#     return avg
#
#
# a = summa(1, 2, 3)
# print(a ** 2)


# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, even=False))
# print(digits_sum(39271, even=False))
# print(digits_sum(123456789, even=False))


# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# print(id(lt1))
# print(id(lt2))
#
# a = 1
# b = 1
# print(a == b)
# print(a is b)
#
# print(id(a))
# print(id(b))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# print(id(lt1))


# s = "Hello"
# print(id(s))
# s += "World"
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))


# s = list("Hello")
# print(s[1])
# s[1] = 't'
# print(s)


# def add_number(n):
#     print(n, "=", id(n))
#     n += [4]
#     print(n, "=", id(n))
#
#
# x = [1, 2, 3]
# print("x:", x, "=", id(x))
# add_number(x)
# print("x:", x, "=", id(x))


# Картеж

# lst = [1, 2, 3]
# tpl = (1, 2, 3)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(type(tpl))

# a = (1, 2, 3, 4, 5)
# print(type(a))
# b = tuple((1, 2, 3, 4, 5))
# print(type(b))


# tpl = (1, 2, 3, 4, 5, 6, 7)
# print(tpl)
# print(tpl[2])
# # tpl[2] = 10
# print(tpl[1:3])

# from random import randint

# s = tuple(input("->") for i in range(3))
# s = tuple(randint(1, 30) for i in range(10))
# print(s)

# s1 = tuple(2 ** i for i in range(1, 13))
# print(s1)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 4, -1))
#
# ...
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def range_tuple(num1, num2):
#     return tuple(randint(num1, num2) for j in range(10))
#
#
# tpl1 = range_tuple(0, 5)
# tpl2 = range_tuple(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print(tpl3.count(0))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# first_name, year, married = user
# first_name, year, married = get_user()
# # print(first_name, year, married)
# first_name = get_user()[0:2]
# print(first_name)


# t = (1, 2, 3)
# del t


# lst = [1, 2, 3, 4, 5]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# lst = list(tpl)
# print(type(lst))
# print(lst)


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.236), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "\nНаселение:", country_population, cities)
#     for city in cities:
#         city_name, city_population = city
#         print('\t город:', city_name, "(население:", city_population, ")", sep="")


# Множество (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))
# lst = ["banana", "apple", "orange", "banana", "apple"]
# a = set(lst)
# print(type(a))
# print(a)


# s = {x for x in range(10)}
# print(s)


# def to_set(a):
#     x = set(a)
#     n = len(x)
#     return x,n
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {'red', "green", "blue"}
# # print("green1" not in t)
# for i in t:
#     print(i)

# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in lst if 'a' in i}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'}
# print(a)
#
# for i in lst:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])

# users = {"Tom", "Alice", "Bob"}
# users.add("Ann")
# print(users)
# # user = "Tom"
# # if user in users:
# #     users.remove("Tom")
# # print(users)
#
# # users.discard("Rob")
# # print(users)
#
# # users.pop()
# # print(users)
#
# users.clear()
# print(users)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# print(c)
# a |= b
# print(a)
# c = a & b
# print(c)
# a &= b
# print(a)
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# a = set(input())
# b = set(input())
# c = a | b
# print(c)
#
# str1 = "Hello"
# str2 = "How are you"
# s1 = set(str1)
# s2 = set(str2)
# s3 = s1 & s2
# print(s3)


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
#
# one = drawing ^ music
# print(one)
#
# both = drawing & music
# print(both)
#
# drawing = drawing - both
# print(drawing)


# frozenset (замороженное множество)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# a = frozenset({"hello", "world"})
# print(a)


# Словарь (dict)

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(s[1])
# print(d["two"])


# d = {"one": 1, "two": 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)

# d = {"one": 1, "two": 2, "three": 3}
# print(list(d))
# lst = ['one', 'two', 'three']
# # print(dict(lst))
#
# a = [
#     ('one', 1),
#     ('two', 2),
#     ('three', 3),
# ]
# print(dict(a))

# d = {"one": 45, 0: "text", (1, 2.3): "Кортеж", 43: [2, 3, 6, 7], 1: "text", True: 1}
# print(d[43])

# from random import randint
#
# # d = {i: i ** 2 for i in range(2, 7)}
# # d = {i: randint(1, 100) for i in range(7)}
# # print(d)
# # d = {str(i) + ")": randint(1, 100) for i in range (3)}
# d = {input("n ="): input("-> ") for i in range(3)}
# print(d)


# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# d['two'] = 200
# d['one'] += 100
# print(d)
#
# for key in d:
#     print(key, ":", d[key])


# from math import pi  //dz
#
#
# def square():
#     t = str(input("Введите для какой фигуры хотите найти площадь (прямоугольник, треугольник, круг) \n->"))
#     if t == "прямоугольник":
#         a = int(input("a: "))
#         b = int(input("b: "))
#         s = a * b
#         print("Площадь: ", s)
#     elif t == "треугольник":
#         a = int(input("Основание: "))
#         h = int(input("Высота: "))
#         s = a * h / 2
#         print("Площадь: ", s)
#     elif t == "круг":
#         r = int(input("Радиус: "))
#         s = pi * r * r
#         print(round(s, 2))
#     else:
#         print("Нет такой фигуры")
#         square()
#
#
# square()

# from random import randint
#
# s = list(randint(1, 20) for i in range(10))
# print(s)
# print("\nMin: ", min(s), "\nMax: ", max(s))

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# d['two'] = 200
# d['one'] += 100
# print(d)

# key = "two1"
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом" + key + "нет в словаре")
# print(d)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой ключ исключить: "))
# del d[dislike]
# print(d)


# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400],
# }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб.", sep='')
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         qty = int(input("Количество: "))
#         goods[n][1] = qty
#     else:
#         break
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб.", sep='')

# d = {"a": 1, "b": 2, "c": 3}
# d2 = d.copy()
# d2 = d
# print("D =", d)
# print("D =", d2)
# d['b'] = 5
# d2["e"] = 7
# print("D =", d)
# print("D =", d2)

# d = {"a": 1, "b": 2, "c": 3}
# print(d["e"])
# value = d.get("b1", 'Такого ключа нет')
# print(value)


# d = {"a": 1, "b": 2, "c": 3}
# print(d.keys())   # ключи
# print(d.values())   # значение
# print(d.items())   # ключи + значения
#
# for i in d:
#     print(i)
#
# print(list(d.items()))
#
# for k, v in d.items():
#     print(k, v)

# d = {"a": 1, "b": 2, "c": 3}
# item = d.setdefault('e', 100)   # устанавливает значение по умолчанию
# # item = d.pop('b')
# # item = d.popitem()
# # d.clear()
# # print(item)
# d.update([("r", 7), ('t', 6)])
# d.update({'r': 8, 'c': 6})
# print(d)

# x = {'a':1,'b':2}
# y = {'b':3,'c':4}
# # z = x.copy()
# # z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', "age": 25, "salary": 8000, "city": "New York"}
# # new_d = dict()
# # new_d['name'] = d.pop("name")
# # new_d['salary'] = d.pop("salary")
# # print(d)
# # print(new_d)
#
# d['location'] = d.pop('city')
# print(d)


# a = {
# #     'first':{
# #         1: "one",
# #         2: "two",
# #         3: "three",
# #     },
# #     'second': {
# #         4: "four",
# #         5: "five"
# #     }
# # }
# # print(a)
# # for x in a:
# #     print(x)
# #     for y in a[x]:
# #         print("\t", y, ": ", a[x][y], sep="")


# sales = {
#     'John': {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     'Tom': {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     'Anne': {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     'Fiona': {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y], sep="")
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person][region])

# d = {"a": 1, "b": 2, "c": 3, "d": 4}
# print({key: value for key, value in d.items()})
# print({key: value for key, value in d.items() if value <= 2})

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)
#
#
# b = 5
# print(b)
# b = "Hello"
# print(b)

# a = [12, 1, 2]
# b = ['Dec', 'Jan', 'Feb']
# c = [4.0, 8.5, 4.9]
# # d = dict(zip(a, b))
# # f = {k: v for k, v in zip(a, b)}
# # print(f)
# # print(d)
#
# f = zip(a, b, c)
# print(list(f))

# dict_one = {'name': 'Igor', 'email': 'igor@gmail.com', 'job': 'Consultant'}
# dict_two = {'name': 'Irina', 'email': 'irina@gmail.com', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# a = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
# d = list(a.items())
# print(d)
# n, m = zip(*d)
# print(n)
# print(m)
# c = list(zip(m, n))
# print(c)
# c.sort()
# print(c)
# print(dict(c))
# c = {v: k for k, v in c}
# print(c)

# month = ['January', "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в", m, "=", profit)

# one = {'a': 1, 'b': 2}
# two = {'c': 3, 'd': 4}
# print({**one, **two})   # {}


# data = ["red", "green", "blue"]
# ind = 1
# for i in data:
#     print(ind, i)
#     ind += 1
# for n, i in enumerate(data, 1):
#     print(n, i)

# dict_one = {'name': 'Igor', 'email': 'igor@gmail.com', 'job': 'Consultant'}
#
# for i, (j, v) in enumerate(dict_one.items(), 1):
#     print(i, j, "->", v)
#
# for i, v in enumerate(dict_one.values(), 1):
#     print(i, "->", v)


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 3, 2, 7))

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 4, 5))


# def to_dict(*args):
#     return {k: k for k in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def to_dict(*args):
#     avg = sum(args) / len(args)
#     print(avg)
#     return [x for x in args if x < avg]
#
#
# print(to_dict(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(to_dict(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 5, 7, 8, 9, 4))


# def print_scores(student, *scores):
#     print("\nStudent Name:", student)
#     # for score in scores:
#     #     print(score, end=' ')
#     print(*scores)
#     print()
#
#
# print_scores("Jonathan", 10, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33, 56)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))


# def intro(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name='Irina', surname='Sharma', age=22)
# intro(name='Igor', surname='Wood', email='igor@mail.com', age=25, phone=9876543210)


# my_dict = {"one": "first"}
#
#
# def db(**kwargs):
#     # global my_dict
#     # my_dict = my_dict | kwargs
#     # return my_dict
#     my_dict.update(kwargs)
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyer_color='gray')
# print(my_dict)


# def func1(*args):
#     print(args[0])
#
#
# func1(1, 2, 3, 4, 5, 6)
# func1(5)

# def func(first, *args, c=100, **kwargs):
#     return first, args, c, kwargs
#
#
# print(func(5, 4, 8, 9, 7, a=6, b=2, c=10))


# Области видимости (scope)

# name = 'Tom'
# surname = ""
#
#
# def hi():
#     global name, surname
#     name = "Sam"
#     surname = "johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
# print(surname)

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()

# x = 3
#
#
# def add_two(a):
#     x = 2
#
#     def add_some():
#         return a + x
#     return add_some()
#
#
# print(add_two(3))


# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# min = 5
# print(min)
# a = [4, 5, 7, 8, 9]
# print(a)
# print(min(a))

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print('a =', a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print(z)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()


# def outer(a1, a2, b1, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, 5, 7))


# x = ('ab', 'abcd', 'cde', 'abc', 'def')
#
# s = input("s =")
# for i in x:
#     if s == i:
#         print(s)

# s = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
# t = set(s)
# u = 0
# for i in s:
#     for j in t:
#         if i == j:
#             u += 1
#             print(j, "=", u)

# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#
#
# print(rect_paral_square(2, 4, 6))
# print(s)
# print(rect_paral_square(5, 8, 2))
# print(s)
# print(rect_paral_square(1, 6, 8))
# print(s)

# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     # s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
#
# print(rect_paral_square(5, 8, 2))
#
# print(rect_paral_square(1, 6, 8))


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(11))
#
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def incr():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return incr
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()


# students = {
#     'alice': 98,
#     'bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = make(80,101)
# B = make(70, 80)
# C = make(50, 70)
# D = make(0, 50)
#
#
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))

# Анонимные функции(lambda)


# def name(x, y):
#     return x + y
#
#
# print(name(3, 5))
# print((lambda x, y: x + y)(1, 2))
# print()

# func = lambda x, y: x + y
#
# print(func(1, 2))
# print(func('a', 'b'))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda *args: args)(1, 2, 3, 4, 5, 6))

# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
#
# for t in c:
#     print(t("abc_"))


# def outer1(n):
#     return lambda x: n + x
#
# add2 = outer1(5)
# print(add2(10))
#
#
# outer2 = lambda n: lambda x: x + n
# add3 = outer2(5)
# print(add3(10))
#
# print((lambda n: lambda x: x + n)(5)(10))
#
# print((lambda n: lambda y: lambda x: x + n + y)(5)(10)(10))

# def func(i):
#     return i[1]
#
# d = {'d': 10, 'b': 15, 'c': 4}
#
# list_d = list(d.items())
# print(list_d)
# # list_d.sort(key=lambda i: i[1])
# list_d.sort(key=func)
# print(list_d)
# print(dict(list_d))


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
#
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x / y]
#
# print(a[0](12, 3))


# a = {'one': lambda x: x - 1, 'two': lambda x: x * (-1), 'three': lambda x: x ** 5}
#
# b = {-3, 10, 0, 4}
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#      1: lambda: print('Понедельник'),
#      2: lambda: print('Вторник'),
#      3: lambda: print('Среда')
# }
#
# d[2]()

# print((lambda a, b, c: a if a < b and a < c else b if b < c and b < a else c)(5, 13, 33))


# map(func, iterables), filter(func, iterables)


# def mult(l):
#     return l * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# a = list(map(mult, lst))
# print(a)
#
# a1 = list(map(lambda t: t * 2, lst))
# print(a1)


# t = (2.88, -1.75, 100.55)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
#
# t3 = tuple(map(int, t))
# print(t3)

# areas = [3.564897, 7.4512368, 8.412578, 4.456712, 7.456782, 2.321456]
#
# print(list(map(round, areas, [2, 5, 2, 4, 6, 1])))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x, y: (x, y), st, num)))
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))
#
# a = l1, l2
# print(a)

# t = ('abcd', 'abc', 'cdrfg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint
#
# lst =[randint(1, 20) for i in range(10)]
# print(lst)
# print("[10; 20] = ", list(filter(lambda s: 10 <= s <= 20, lst)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))


# декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_hello"')
#     print(func())


# super_func(hello)


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello()
# print(test)
# print(type(test))


# def my_decorator(func):
#     def func_wrapper():
#         print('Код до функции')
#         func()
#         print('Код после функции')
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Тело функции "func_test"')
#
#
# func_test()
# test = my_decorator(func_test)
# test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции: ', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print()
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print("Меня зовут:", name, surname)
#
#
# print_full_name("Ирина", "Леонова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print()
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study='JavaScript')
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# print(int("19"))
# print(int("19.5"))  # ValueError

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010)
# print(0o22)
# print(0x12)


# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# print(e * -3)
# print("Py1" in e)


# s = "Hello"
# print(s[1])
# print(s[-5])
# print(s[1:4])
# print(s[::-1])

# s = 'python'
# # s[3] = 't'
# s = s[:3] + 't' + s[4:]
# print(s)


# def change_to_str(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык"
# str2 = change_to_str(str1, "N", "P")
# print("str1", str1)
# print("str2", str2)

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
# print(r"C:\folder\file\\"[:-1])
# print(r"C:\folder\file" + "\\")
# print("C:\\folder\\file\\")


# name = "Дмитрий"
# age = 25
#
# print("Меня зовут ", name, ". Мне", age, " лет", sep="")
# print("Меня зовут " + name + ". Мне" + str(age) + " лет")
# print(f"Меня зовут {name}. Мне {age} лет")

# from math import pi
#
# print(f"Число PI: {pi}")
# print(f"Число PI: {round(pi, 2)}")
# print(f"Число PI: {pi:.2f}")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")


# a = 74
# print(f"{{{a}}}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')

# s = ""
# s1 = ''
# s3 = """"""
# s4 = ''''''

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра.
#     :param h: положительное число, высота цилиндра.
#     :return: положительное число, площадь цилиндра.
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('м'))

# while True:
#     n = input('=> ')
#     if n != -1:
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# arr = [ord(i) for i in my_str]
# print("ASCII коды:", arr)
#
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
#
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
#
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(1080))

# a = 122
# b = 97
# # if a > b:
# #     print([chr(i) for i in range(b, a + 1)])
# # else:
# #     print([chr(i) for i in range(a, b + 1)])
#
# if b > a:
#     a, b = b, a
# print([chr(i) for i in range(b, a + 1)])
# for i in range(b, a + 1):
#     print(chr(i), end=' ')


# print('apple' == 'Apple')
# print('apple' > 'Apple')


# from random import randint
#
# short = 7
# long = 10
# min_ASCII = 33
# max_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(short, long)
#     res = ''
#     for i in range(rand_len):
#         rand_char = chr(randint(min_ASCII, max_ASCII))
#         res += rand_char
#
#     return res
#
#
# print('Случайный пароль', random_password())

#  Методы строк
# print(dir(list), "\n")
# print(dir(str))

# s = "hello, WORLD! I am learning Python."

# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.

# print(s.lower().count('h'))  # подсчет количества вхождений подстроки в строку
# print(s.find('Python'))  # возвращает индекс, который соответствует началу подстроки или -1 если элемента нет
# print(s.rindex('h'))  # возвращает последний индекс
#
# s = 'один два'
# one_world = s[:s.find(' ')]
# print(one_world)
# two_world = s[s.find(' ') + 1:]
# print(two_world)
# print(two_world + ' ' + one_world)

# s1 = 'ab12c59p7dq'
# digits = []
# for symbol in s1:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
#
#
# print(digits)
# digits.append('1')
# print(digits)

# st = 'the original words and form a written or printed work'
# ch = 't'
# if st.count(ch) == 1:
#     print(st.find(ch))
# elif st.count(ch) >= 2:
#     print(st.find(ch), st.rfind(ch))

# s = "hello, WORLD! I am learning Python."
#
# print(s.endswith('lo', 0, 5))  # строка заканчивается заданными символами
# print(s.startswith('hello'))  № строка начинается с заданных символов

# print('abc123'.isalnum())  # определяет ли строка из букв и цифр
#
# print('abcABC'.isalnum())  # определяет, состоит ли строка из букв
# print('Aabc123'.isdigit())  # определяет, состоит ли строка из цифр
# print('abcABC'.islower())  # определяет ли строка из цифр букв в нижнем регистре
#
# print('ADF456'.isupper())  # определяет, состоит ли строка из символов букв в верхнем регистре

# print('py'.center(10))  # выравнивает строку по центру
# print('py'.center(10, "-"))
# print('py'.center(1))


# print('      py'.lstrip())
# print('py        '.rstrip())
# print('      py    '.strip())


# print('https://www.python.org'.lstrip("/:pths"))
# print('https://www.python.org'.rstrip("/:pths"))
# print('https://www.python.org'.rstrip("/:pths"))

# print('https://www.python.org'.rstrip("org.").lstrip("/:pths"))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace('Nython', 'Python', 2))

# s = "Заменить в этой строке все пояления буквы 'о' на букву 'О', кроме первого и последнего вхождения."
# a = s[:s.find('о') + 1]
# b = s[s.find('о') + 1:s.rfind('о')]
# c = s[s.rfind('о'):]
# s = a + b.replace('о', 'О') + c
# print(s)

# s = '-'
# seq = ("a", 'b', 'c')
# print(s.join(seq))
#
# print('..'.join(['1', '2']))

# print(':'.join('Hello'))
# print('H:e:l:l:o'.split(':'))
# print('Строка разделенная пробелами'.split())
# print('www.python.org.ru'.split(".", 1))
# print('www.python.org.ru'.rsplit(".", 2))


# a = input("-> ").split()
# print(a)

# a = input('Введите ФИО: ').split()
# print(a)
# print(f"{a[0].capitalize()} {a[1][0].upper()}. {a[2][0].upper()}.")


# Регулярные выражения

# import re

# s = 'Я ищу совпадения в 2023 году. И я их найду в два счёта.'
# reg = 'я'

# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения с шаблоном
# print(re.search(reg, s))   # местоположение первого совпадения объекта
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # местоположение совпадения объекта в начале строки
# print(re.split(reg, s, 2))  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, 'Я', s, 3))  # поиск и замена

# import re

# s = 'Я ищу совпадения в 2023 году. И я их найду в [ два ] счёта.'
# # reg = '[12][0-9][0-9][0-9]'
# # reg = '[А-яЁё]'
# # reg = '[A-Za-z]'
# # reg = r'\.'
# # reg = r'[0-9.\[\]].'
# reg = r'[^0-9]'  # ^ = все кроме указанных сиволов
# print(re.findall(reg, s))
# print(ord("Я"))
# print(ord("а"))
# print(chr(96))


# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = r'[2][0-9]:[0-5][0-9]'
# print(re.findall(reg, s))

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# # reg = r'\w\s\w'
# # reg = r'\w+'
# reg = r'20*'
# print(re.findall(reg, s))


# d = "Цифры: 7, +17, -42, 0012, 0.3"
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# s = "06-03-1987 # Дата рождения"
# print('Дата рождения:', re.sub(r'#.*', '', s))
#
# print('Дата рождения:', re.sub(r'-', '.',  re.sub(r'#.*', '', s)))

# s = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+[\s\w.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, s))


# s = "12 сентября 2021 года"
# # reg = r"\d{2,4}"
# reg = r"\d{2,}"
# print(re.findall(reg, s))

# s = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
#
# reg = r"\0+?7\d{10}"
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2023 году. И я их найду в [ два ] счёта.'
# # reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
# print(re.findall(reg, s))


# def validate_login(name):
#     return re.findall(r'^[A-Za-z_0-9-]{3,16}$', name)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Pyt09%%%'))

#
# print(re.findall(r'\w+', '10 + й'))
# print(re.findall(r'\w+', '10 + й', flags=re.ASCII))
# print(re.findall(r'\w+', '10 + й', flags=re.A))
# print(re.findall(r'\w+', '10 + й', re.A))


# text = 'hello world'
# print(re.findall(r"\w+", text))
# print(re.findall(r"\w+", text, re.DEBUG))

# s = 'Я ищу совпадения в 2023 году. И я их найду в [ два ] счёта.'
# reg = r"я"
# print(re.findall(reg, s, re.IGNORECASE))


# text = '''
# one
# two
# '''
# print(re.findall(r'one.\w+', text, re.DOTALL))

# print(re.findall('one$', text))
# print(re.findall('one$', text, re.MULTILINE))
# print(re.findall('^two$', text,))
# print(re.findall('^two$', text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+    # part 1
# @           # @
# [a-z.-]+    # part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))

# lambda n: lambda y: lambda x: x + n + y)(int(5))(int(30))(int(10))

# from math import pi
#
# s_1 = lambda x: 2 * x * pi
# s_2 = lambda y: lambda x: y * x
# s_3 = lambda h: lambda b: lambda a: h*(a + b)/2
#
# add = s_2(10)
# add_1 = s_3(3)
# print("Площадь окружности радиуса 2: ", s_1(2))
# print("Площадь треугольника размером 10*13: ", add(13))
# print("Площадь треугольника размером 10*13: ", add_1(5)(7))


# def args_decorator(fn):
#     def wrap(args):
#         print(f"Среднее арифметическое чисел {zip(args[1])} = {sum(args)/len(args)}")
#         fn(args)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(args):
#     print("Сумма чисел", list(args), "=", sum(args))
#
#
# print_full_name(tuple(int(input("->")) for i in range(int(input("Введите количество чисел: ")))))

# дописать с начала занятия

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d*)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счё_та."
# reg = r"(\d+)\s(\D+)"
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[2])


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_count(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print("<select name='city'>")
# print(re.sub(r'\s*(\w+)\s*', repl_count, text))
# print("</select>")

# s = "Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021"
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.ru and yandex.com"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))


#  Рекурсия

# def elevator(n):
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#

# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
#
# print(names[1])
# print(isinstance(names[1], list))
#
# print(names[1][1])
# print(isinstance(names[1][1], list))
#
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# count = 0
# for i in range(len(names)):
#     count += 1
#     for j in range(len(names[i]) - 1):
#         if isinstance(names[i], list):
#             count += 1
#             for k in range(len(names[i][j]) - 1):
#                 if isinstance(names[i][j], list):
#                     count += 1
#
#
# print(isinstance(names))


#
#
#
#
# print(count_items(names))


# def remove(text): # Hello\tWorld
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])  # H
#
#
# print(remove("  Hello\tWorld "))
#
# print(bool(" "))


# Файлы

# f = open(r'D:\python\pythonProject\text.txt')
# f = open('text.txt', mode="r")
# print(f)
# print(*f)
# print(f.mode)
# print(f.encoding)
# print(f.name)
# f.close()
# print(f.closed)

# f = open('text.txt')
# print(f.read(3))
# f.close()

# f = open('11.txt')
# # # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# f.close()

# f = open('11.txt')
# print(f.readlines(15))
# print(f.readlines())
# f.close()


# f = open('11.txt')
# for line in f:
#     print(line)
# f.close()

# f = open('11.txt')
# print(len(f.readlines()))
# f.close()

# f = open('text.txt', 'w')
# f.write('Hello\nWorld\n')
# f.close()
# f = open('text.txt', 'r')
# print(f.readline())
# f.close()


# f = open("xyz.txt", "a")
# f.write('New text\n')
# line = ['This if line 1', 'This is line 2']
# f.writelines(line)
# f.close()

# f = open("xyz.txt", "a")
# lst = [str(i ** 5) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('text2.txt', 'w')
# f.write('Заменить строку в текстовом файле\n изменить строку в списке\nзаписать список в файл')
# f.close()


# f = open('text5.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = 'Замена'
# print(read_file)
# f.close()

# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('text2.txt', 'w')
# f.write('''Заменить строку в текстовом файле;
# изменить строку в списке;
# записать список в файл''')
# f.close()
# n = int(input('введите номер строки удаляемой строки '))
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# if 0 < n < 3:
#     read_file[n - 1] = ''
# print(read_file)
# f.close()
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('text.txt', 'r')
# print(f.read(3))  # Hel
# print(f.tell())  # 3 - возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # 1 = перемещает условный курсор в заданную позицию
# print(f.read())
# f.close()


# f = open('text1.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# # with open('text.txt', 'w+') as f:
# #     print(f.write('0123456789'))
#
#
# with open ('text.txt', 'r+') as f:
#     for line in f:
#         print(line)


# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     get_line(lst)
#     f.write(str(lst))
#
# print('Done!')

# with open('res.txt', 'r') as f:
#     read_file = f.read().split(" ")
#     print(read_file)
#     len(read_file)
#     print(sum(map(float, read_file)))


# def longest_words(file,):
#     with open(file) as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         print(w)
#         print(res)
#         if len(res) == 1:
#             return res [0]
#         return max_length
#
#
# print(longest_words('test.txt'))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)
#
# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r', encoding = ETF8) as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)
# #
#
# read_file = 'one.txt'
# write_file = 'two.txt'
# other_file = 'three.txt'
# with open(read_file, 'r') as fr, open(write_file, 'r') as frr, open(other_file, 'w') as fw:
#     # for line in fr:
#     #     line = line.replace('Строка', 'Линия - ')
#     #     fw.write(line)
#     a = fr.readlines()
#     b = frr.readlines()
#     # print(a)
#     # print(b)
#     # c = a + b
#     # print(c)
#     # for line in c:
#     #     fw.write(line)
#     # fw.writelines(c)
#     for i, j in zip(a, b):
#         c = i + j
#         fw.write(c)

# file_name = 'dz.txt'
# text = 'Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n'
# write_file = 'dz1.txt'
#
# with open(file_name, 'w') as f:
#     f.write(text)
#
# pos1 = int(input('введите номер заменяемой строки строки '))
# pos2 = int(input('введите номер заменяемой строки строки '))
#
# with open(file_name, 'r') as fr, open(write_file, 'w') as fw:
#     a = fr.readline()
#     b = fr.readline()
#     c = fr.readline()
#     if pos1 == 1 and pos2 == 2 or pos1 == 2 and pos2 == 1:
#         fw.writelines(b + a + c)
#     elif pos1 == 3 and pos2 == 1 or pos1 == 1 and pos2 == 3:
#         fw.writelines(c + b + a)
#     elif pos1 == 3 and pos2 == 2 or pos1 == 2 and pos2 == 3:
#         fw.writelines(a + c + b)
#
# file_name2 = 'dz3.txt'
# text = 'Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n'
# write_file = 'dz4.txt'
#
# with open(file_name2, 'w') as f:
#     f.write(text)
#
# with open(file_name2, 'r') as fr, open(write_file, 'w') as fw:
#     a = fr.readline()
#     b = fr.readline()
#     c = fr.readline()
#     fw.writelines(c + b + a)

# with open(file_name, 'r') as f:
#     for line in f:
#         if line == pos1 - 1:
#             f.write(t[pos2 - 1])
#         elif line == pos2 - 1:
#             f.write(t[pos1 - 1])
#         else:
#             ...
#
# with open(file_name, 'r') as f:
#     f.readlines()


# Модули OS b OS.PATH

# import os
# import os.path

# print(os.path.split(r"D:\python\pythonProject\nested1\nested2\nested3\text.txt"))

# print("Текущая дериктория:", os.getcwd())
# print(os.listdir())  # возвращает имена файлов и папок из текущей директории
# print(os.listdir(".."))
# os.mkdir("folder")  # создание папки
# os.makedirs("nested1/nested2/nested3")  # создание папки и всех папок
# os.rmdir("folder")  # удаление пустой директории
# os.remove('xyz.txt')  # удаляет файл или папку
# os.rename("three.txt", "directory/three.txt")
# os.renames("text2.txt", "test/text.txt")  # создает промежуточные директории

# import os
#
# sc = os.getcwd()
# s = os.listdir()
# for i in s:
#     path = sc + "\\" + i
#     t = os.path.isdir(path)
#     if t:
#         print(f"{i} - dir")
#     else:
#         w = os.path.getsize(path)
#         print(f"{i} - file - {w} bytes")
# for i in s:

# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk("nested1"):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
# remove_empty_dirs("nested1")


# print(os.path.split(r"D:\python\pythonProject\nested1\nested2\nested3\text.txt"))  # разбивает путь на кортеж (head,
# # tail),
# tail - последний компонент пути, head - остальная часть

# print(os.path.dirname(r"D:\python\pythonProject\nested1\nested2\nested3\text.txt")) # путь до последнего компонента
# print(os.path.basename(r"D:\python\pythonProject\nested1\nested2\nested3\text.txt")) # последний компонент пути

# print(os.path.join(r'D:\python', 'pythonProject', 'nested1', 'nested2', 'nested3', 'text.txt'))  # соединяет один или
# # несколько компонентов пути с учетом особенностей OS


# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, 'w').close()
#
# files_width_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# # Work\w.txt
# # Work\F1\f11.txt
# # Work\F1\f12.txt
# # Work\F1\f13.txt
# # Work\F2\F21\f211.txt
# # Work\F2\F21\f212.txt
#
# for file in files_width_text:
#     with open(file, 'w') as f:
#         f.write(f'Некоторый текст для документа: {file}')
#
#
# def print_tree(root, topdown=True):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fl in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)


# print_tree("Work", False)
# print_tree("Work")
#
# print(os.path.exists(r'D:\python\pythonProject\Work\F2\F21\f211.txt'))  # возвращает True, если путь указывает
# # на существующий файл, False на несуществующий

# import time, os
#
# path = r'D:\python\pythonProject\Work\F2\F21\f211.txt'
# print(os.path.getsize(path) // 1024, "КВ") #
# print(os.path.getmtime(path))  # время последнего изменения файла
# print(os.path.getatime(path))  # время последнего доступа к файлу
# print(os.path.getctime(path))  # время создания файла
#
#
# a_time = os.path.getatime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a_time)))
#
# print(os.path.isdir(r'D:\python\pythonProject\Work\F2\F21\f211.txt'))  # Возвращает True если путь является
# директорией
# print(os.path.isfile(r'D:\python\pythonProject\Work\F2\F21\f211.txt'))  # Возвращает True если путь является файлом
# import os
#
# path = r"nested1\nested2\nested3\text.txt"
#
# if os.path.exists(path):
#     d, name = os.path.split(path)
#     print(d)
#     print(name)
#     print(f"{name} ({d}), -last access time", os.path.getatime(path))
# else:
#     print("File is not exist")

# class Point:
#     """R"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(type(p1))
# print(p1.x)
# print(Point.__doc__)
# print(dir(Point))

# class Point:
#     """R"""
#     x = 1
#     y = 2
#
#
# p1 = Point()
# p2 = Point()
# p1.x = 30
# p1.y = 60
# p1.z = 90
# Point.x = 100
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(Point.__dict__)
#
#
# print(p2.x)
# print(p2.y)
# print(id(p1))
# print(id(p2))

# class Point:
#     """R"""
#     x = 1
#     y = 2
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coord(5, 10)
# Point.set_coord(p1, 5, 10)
#
# p2 = Point()
# p2.x = 10
# p2.y = 20
# p2.set_coord()


# class Human:
#     name = "name"
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = "country"
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_name(self, first_name):
#         self.name = first_name
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1А')
# h1.print_info()
# h1.set_city("Саратов")
# h1.print_info()
# print(h1.get_city())


# class Person:
#     skill = 10  # статическое свойтсво
#
#     def __init__(self, name, surname):
#         self.name = name  # динамическое свойство
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person('Victor', "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
#
# p1 = Person('Anna', "Dolgin")
# p1.print_info()
# p1.add_skill(2)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра")
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# del p1
# print(p1.x)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if isinstance(x, int) and isinstance(y, int):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# p1.set_coord('abc', 'aaa')
# print(p1.get_coord())


# class Point:
#     count = 0
#
#     def __init__(self, x=1, y=1):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print("Point", Point.count)

# class Auto:
#     def __init__(self, mark =" ", year = " ", manufacturer = " ", power = " ", color = " ", price = " "):
#         self.mark = mark
#         self.year = year
#         self.manufacturer = manufacturer
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def set_info(self, mark, year, manufacturer, power, color, price):
#         if isinstance(mark, str) and isinstance(year, int) and isinstance(manufacturer, str) and\
#                 isinstance(power, int) and isinstance(color, str) and isinstance(price, int):
#             self.mark = mark
#             self.year = year
#             self.manufacturer = manufacturer
#             self.power = power
#             self.color = color
#             self.price = price
#         else:
#             print("Данные введены некорректно")
#
#     def get_info(self):
#         return self.mark, self.year, self.manufacturer, self.power, self.color, self.price
#
#     def print_info(self):
#         print(' Данные автомобиля '.center(40, "*"))
#         print(f'Название модели: {self.mark}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\n'
#                      f'Мощность двигателя: {self.power} л.с.\nЦвет машины: {self.color}\nЦена: {self.price}')
#         print("=" * 40)
#         return "\n"
#
#     def set_mark(self, mark):
#         if isinstance(mark, str):
#             self.mark = mark
#         else:
#             print("Марка автомобиля должна быть строкой")
#
#     def get_mark(self):
#         return self.mark
#
#     def set_year(self, year):
#         if isinstance(year, int):
#             self.year = year
#         else:
#             print("Год выпуска должен быть числом")
#
#     def set_manufacturer(self, manufacturer):
#         if isinstance(manufacturer, str):
#             self.manufacturer = manufacturer
#         else:
#             print("Год выпуска должен быть строкой")
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#     def set_power(self, power):
#         if isinstance(power, int):
#             self.power = power
#         else:
#             print("Год выпуска должен быть строкой")
#
#     def get_power(self):
#         return self.power
#
#     def set_color(self, color):
#         if isinstance(color, str):
#             self.color = color
#         else:
#             print("Год выпуска должен быть строкой")
#
#     def get_color(self):
#         return self.color
#
#     def set_price(self, price):
#         if isinstance(price, int):
#             self.price = price
#         else:
#             print("Год выпуска должен быть строкой")
#
#     def get_price(self):
#         return self.price
#
#
# p = Auto()
# p.set_info("X7 M50i", 2021, "BMW", 530, "white", 10790000)
# # p1 = Auto("X7 M50i", 2021, "BMW", 530, "white", 10790000)
# print(p.print_info())
# p.set_mark("iX M60")
# print(p.print_info())
# p.set_year(2017)
# print(p.print_info())
# p.set_manufacturer("Hyundai")
# print(p.print_info())
# p.set_power(435)
# print(p.print_info())
# p.set_color("Blue")
# print(p.print_info())
# p.set_price(8500000)
# print(p.print_info())


# class Math:
#     @staticmethod
#     def minn(a, b, c, d):
#         minn = min(a, b, c, d)
#         return f'Минимальное число: {minn}'
#
#     @staticmethod
#     def maxx(a, b, c, d):
#         maxx = max(a, b, c, d)
#         return f'Максимальное число: {maxx}'
#
#     @staticmethod
#     def sr(a, b, c, d):
#         f = (a + b + c + d) / 4
#         return f'Среднее арифметическое: {f}'
#
#     @staticmethod
#     def fa(b):
#         i = 1
#         t = 1
#         for r in range(b):
#             t = t * i
#             i += 1
#         return f'Факториал числа ({b}): {t}'
#
#
# p = Math
# print(p.minn(3, 5, 7, 9))
# print(p.maxx(3, 5, 7, 9))
# print(p.sr(3, 5, 7, 9))
# print(p.fa(5))


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Иницилизация робора", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# print()
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print('\nЗдесь роботы могут проделать какую-то работу.\n')
# print("Роботы закончили свою работу. Давайте их выключим.\n")
#
# del droid1
# del droid2
#
# print("Численность роботов:", Robot.k)

# class Point:
#     def __init__(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print('-')
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 10
# print(p1.__dict__)
# print(p1.get_coord())
# p1.set_coord(80.2, 120)
# print(p1.get_coord())
# p1.set_x(20)
# print(p1.get_x())


# дописать

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, int):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pound(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pound(), "фунтов")


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.verify_surname(surname)
#         self.verify_num(num)
#         self.verify_percent(percent)
#         self.verify_value(value)
#
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт")
#         print('*' * 50)
#
#     @staticmethod
#     def verify_surname(surname):
#         if not isinstance(surname, str) or not len(surname) != 1:
#             raise TypeError('Неверно введена фамилия')
#         fam = "".join(re.findall(r'[a-za-яё-]', surname, re.IGNORECASE))
#         print(fam)
#         f = surname.strip(fam)
#         print(f)
#         if len(surname.strip(fam)) != 0:
#             raise TypeError('В Фамилии использовать только буквы и дефис')
#
#     @staticmethod
#     def verify_num(num):
#         if not isinstance(num, str) or not len(num) != 1:
#             raise TypeError('Лицевой счет введен некорректно')
#         numb = "".join(re.findall(r'[0-9]', num, re.IGNORECASE))
#         if len(num.strip(numb)) != 0:
#             raise TypeError('В лицевом счете использовать только цифры')
#
#     @staticmethod
#     def verify_percent(percent):
#         print(percent)
#         if not isinstance(percent, float) or not 0.31 > percent > 0.009:
#             raise TypeError('Процент должен быть числом от 0.01 до 0.3')
#
#     @staticmethod
#     def verify_value(value):
#         print(value)
#         if not isinstance(value, int):
#             raise TypeError('Баланс введен некорректно')
#
#     def __del__(self):
#         print('*' * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         usd_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {usd_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", '12345', 0.03, 3000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.set_usd_rate(2)
# acc.convert_to_usd()
# acc.set_eur_rate(3)
# acc.convert_to_eur()
# acc.edit_owner('Дюма')
# acc.print_info()
#
# acc.add_percents()
# acc.withdraw_money(100)
# acc.withdraw_money(3000)
#
# acc.add_money(5000)


# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#         self.__fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r'[a-zа-яё-]', fio, re.IGNORECASE))
#         print(letters)
#         for s in f:
#             print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 2 и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должен быть строкой')
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) !=6:
#             raise TypeError('')
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспота должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_old(ps)
#         self.__old = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.5)
# p1.fio = "Соболев Игорь Николаевич"

# print(issubclass(Point, object))

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии {self._sp}, {self._ep}, {self._color}, {self._width}, ")
#
#
# class Rect(Prop):
#     def draw_line(self):
#         print(f"Рисование прямоугольника {self._sp}, {self._ep}, {self._color}, {self._width}, ")
#
#
# line = Line(Point(1, 2), Point(10, 20), "green", 5.2)
# line.draw_line()
#
#
# line = Line(Point(1, 2), Point(10, 20), "green", 5.2)
# line.draw_line()


#  дописать 25 03 2023   время 15 08

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Фон: {self.fon}")
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка: {self.border}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))
#
# print(" ".join['1', '2', '3'])

#  переделать за пол час до конча занятия 25 03 2023
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
# class Rect(Prop):
#     if ep is None
#         def draw_rect(self):
#             print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     else:
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# rect = Rect(Point(1, 2), Point(10, 20))
# rect.draw_rect()
# rect.set_coord(Point(10, 30), Point(40, 70))
# rect.draw_rect()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе ")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())

#  пересмотреть 26.03.2023 начало
# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self._value = value
#
#     @abstractmethod
#     def convert_tu_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self._value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_tu_rub(self):
#         return self._value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar, end=" ")
#
#
# class Evro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self._value * Evro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Evro.suffix, end=" ")
#
#
# elem2 = [Evro(5), Evro(10), Evro(50), Evro(100)]
#
# for s in elem2:
#     s.print_value()
#     print(f" = {s.convert_to_rub():.2f} RUB")

# elem = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]

# for d in elem:
#     d.print_value()
#     print(f"={d.convert_to_rub():.2f} RUB")

# def func():
#     x = 2
#
#     def inner():
#         n = 4
#         return n + x
#
#     return inner()
#
#
# print(func())


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("outer method")
#
#     def outer_obj_method(self):
#         print("outer_obj_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("innre_method", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# print(out.name)
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.info = self.InfoLap()
#
#     def print_info(self):
#         print(f'{self.name} => {self.info.mod}, {self.info.proc}, {self.info.memory}')
#
#     class InfoLap:
#         def __init__(self):
#             self.mod = 'HP'
#             self.proc = 'i7'
#             self.memory = 16
#
#         def mod(self, mod):
#             return mod
#
#         def proc(self, proc):
#             return proc
#
#         def memory(self, memory):
#             return memory
#
#
# comp = Student("Roman")
# comp1 = Student("Vladimir")
# ss = comp.info
# comp.print_info()
# comp1.print_info()


# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#
#     def display(self):
#         print("Name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name, self.intern.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "alba"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# emp = Employee()
# emp.show()
# d1 = emp.intern
# d1.display()
# d2 = emp.head
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("внешний класс")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Вложенный класс")
#
#         class InnerClass:
#             def show(self):
#                 print("Класс внутри вложенного класса")
#
#
# outer = Outer()
# outer.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("Базовый класс")
#
#     class Inner:
#         def display1(self):
#             print("Вложенный класс внутри базового")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("Дочерний класс")
#         super().__init__()
#
#     class Ineer(Base.Inner):
#         def display2(self):
#             print("Вложенный класс внутри дочернего")
#
#
# a = SubClass()
# a.display()
# d = a.db
# d.display1()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

# class Point:
#     def __init__(self, *args):
#         print(args)
#         self.__coord = args
#         self.length = 0
#
#     # def __len__(self):
#     #     return len(self.__coord)
#
#
# p = Point(5, 9, 4)
# print(len(p))

# import math
#
# class Point:
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(5, 10)
# print(p1.length)


# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point20:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p2 = Point20(5, 10)
# print("p1 = ", p1.__sizeof__())
# print("p2 = ", p2.__sizeof__() + p2.__dict__.__sizeof__())
# print("p2 = ", p2.__sizeof__())

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name, "is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name, "it playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name, "is barking")
#
#
# b = Dog("Buddy")
# b.bark()
# b.sleep()
# b.play()


# class A:
#     def __init__(self):
#         print("Класс А")
#
#
# class B(A):
#     def __init__(self):
#         print("Класс B")
#
#
# class C(A):
#     def __init__(self):
#         print("Класс C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Класс D")
#
#
# d = D()
# print(D.mro())


# дописать начало 01.04.2023

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def price_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLOG")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_save_log(self):
#         print(f"{self.id}: товар был продан в 00:00")
#
#
# class NoteBook(Goods,MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.price_info()
# n.save_save_log()
# print(NoteBook.mro())


# class Clock:
#     __Day = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("секунды")
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return x if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом данных Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом данных Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом данных Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("правый операнд должен быть типом данных Clock")
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         if self.sec == other.sec:
#             return True
#         return False
#
#     def __gt__(self, other):
#         if self.sec > other.sec:
#             return True
#         return False
#
#     def __ge__(self, other):
#         if self.sec >= other.sec:
#             return True
#         return False
#
#     def __lt__(self, other):
#         if self.sec < other.sec:
#             return True
#         return False
#
#     def __le__(self, other):
#         if self.sec <= other.sec:
#             return True
#         return False
#
#
# c1 = Clock(600)
# c2 = Clock(200)
# c3 = c1 + c2
# c4 = c1 - c2
# c5 = c1 * c2
# c6 = c1 // c2
# c7 = c1 % c2
# c8 = c1 - c2
# c9 = c1 * c2
# print("c1: " + c1.get_format_time())
# print("c2: " + c2.get_format_time())
# print("c1 + c2: " + c3.get_format_time())
# print("c1 - c2: " + c4.get_format_time())
# print("c1 * c2: " + c5.get_format_time())
# print("c1 // c2: " + c6.get_format_time())
# print("c1 % c2: " + c7.get_format_time())
# c1 -= c2
# print("c1 -= c2: " + c1.get_format_time())
# c1 *= c2
# print("c1 *= c2: " + c1.get_format_time())
# c1 //= c2
# print("c1 //= c2: " + c1.get_format_time())
# c10 = c1 % c2
# print("c1 % c2: " + c10.get_format_time())
# print()
# c11 = c3 > c1
# print(f"c3 > c1 {c11}")
# c11 = c3 >= c1
# print(f"c3 >= c1 {c11}")
# c11 = c3 < c1
# print(f"c3 < c1 {c11}")
# c11 = c3 <= c1
# print(f"c3 <= c1 {c11}")

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol={self.pol})"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Else", 5, "F")
# cat3 = Cat("Murzik", 5, "M")
# print(cat1)
# print(cat2)
# print(cat3)
# print(cat1 + cat2)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# print(r1.get_perimetr(), r2.get_perimetr())
#
# s1 = Square(10)
# s2 = Square(20)
# print(s1.get_perimetr(), s2.get_perimetr())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2]
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text('10')
#
# print(t1.total(35))
# print(t2.total(35))

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         return f'{self.name} мяукает'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         return f'{self.name} гавкает'
#
#
# shape = [Cat("Пушок", 2.5), Dog("Мухтар", 4)]
# for a in shape:
#     a.info()
#     print(a.make_sound())


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"{self.surname} {self.name} {self.age}", end=' ')
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, group, rating):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, speciality, experience):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"\n{self.speciality} {self.experience}")
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, speciality, group, rating, topic):
#         super().__init__(surname, name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"\n{self.topic}", end=' ')
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
#     ]
#
# for i in group:
#     i.info()


# Функторы

# def func():
#     def wrap():
#         return "Hello"
#
#     return wrap
#
# a = func()
# print(a())


# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print(self.count)
#
#
# c1 = Counter()
# c1()


# class StripChars:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string):
#         # print(string)
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string[0].strip(self.chars)
#
#
# s1 = StripChars("?;!.: ")
# print(s1(" !  ?Hello World; . :"))
#
#
# def strip_char(chars):
#     def call(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return call
#
#
# s2 = StripChars("?;!.: ")
# print(s2(" !  ?Hello World; . :"))


# 08.04.2023 дописать начало (пол часа)


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             return func(*args, **kwargs) ** self.arg
#
#         return wrap
#
#
# @Power(3)
# def result(a, b):
#     return a * b
#
#
# print(result(2, 2))

# from abc import ABC, abstractmethod
#
# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 28)
#         fn(*args, **kwargs)
#         print("*" * 28)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def method_2(self, value):
#             print("cla =", cls)
#             return value * 2
#
#     return Wrapper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def method_1(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.method_1(4))
# print(obj.method_2(4))


# Дескрипторы

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Иван", "Петров")
# p.name.set("Виктор")
# print(p.name.get())


# class ValidSting:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError (f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidSting()
#     surname = ValidSting()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Петров")
# print(p.name)
# print(p.surname)


# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Значение должно быть положительным")
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#         # return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)
# Создание модулей

# import math
# import random
# from random import randint
#
#
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())

# from car import electrocar
#
# car = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
#
#
# def main():
#     car1 = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
#     car1.show_car()
#     car1.description_battery()
#
#
# if __name__ == "__main__":
#     main()

# from math import sqrt
#
#
# class Shape:
#     def __init__(self, a, b=None, c=None):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimetr(self):
#         if self.c == None:
#             if self.b == None:
#                 return self.a * 4
#             else:
#                 return (self.a + self.b) * 2
#         else:
#             return self.a + self.b + self.c
#
#     def squar(self):
#         if self.c == None:
#             if self.b == None:
#                 return self.a * self.a
#             else:
#                 return self.a * self.b
#         else:
#             p = (self.a + self.b + self.c) / 2
#             t = p * (p - self.a) * (p - self.b) * (p - self.c)
#             return round(sqrt(t), 2)
#
#     def show(self):
#         if self.c == None:
#             if self.b == None:
#                 for h in range(self.a):
#                     print(f"*" * self.a)
#             else:
#                 for k in range(self.a):
#                     print(f"*" * self.b)
#         else:
#             for t in range(self.b):
#                 print((f"*" * (1 + 2 * t)).center(self.a, " "))
#
#     def info(self):
#         print(f"Площадь: {self.squar()}")
#         print(f"Периметр: {self.perimetr()}")
#         self.show()
#
#
# class Square(Shape):
#     def __init__(self, a, color):
#         super().__init__(a)
#         self.color = color
#
#     def info(self):
#         print("Квадрат".center(13, '='))
#         print(f"Сторона: {self.a}")
#         print(f"Цвет: {self.color}")
#         super().info()
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b, color):
#         super().__init__(a, b)
#         self.color = color
#
#     def info(self):
#         print()
#         print("Прямоугольник".center(20, '='))
#         print(f"Длина: {self.a}")
#         print(f"Ширина: {self.b}")
#         print(f"Цвет: {self.color}")
#         super().info()
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, с, color):
#         super().__init__(a, b, с)
#         self.color = color
#
#     def info(self):
#         print()
#         print(' Треугольник '.center(24, '='))
#         print(f"Сторона 1: {self.a}")
#         print(f"Сторона 2: {self.b}")
#         print(f"Сторона 3: {self.c}")
#         print(f"Цвет: {self.color}")
#         super().info()
#
#
# s = (
#     Square(3, "red"),
#     Rectangle(3, 7, "green"),
#     Triangle(11, 6, 6, "yellow"),
#      )
# for i in s:
#     i.info()


# class Rectangle(Shape):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#
#     def info(self):
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         super().__init__(a, b, c)git

# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"{self.surname} {self.name} {self.age}", end=' ')
#

# class Triangle:
#     @staticmethod
#     def verify_size(size):
#         if not isinstance(size, int) or size <= 0:
#             raise TypeError(f"Размер стороны должен быть целым и положительным")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_size(value)
#         setattr(instance, self.name, value)
#
#
# class Sides:
#     a = Triangle()
#     b = Triangle()
#     c = Triangle()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def check(self):
#         if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
#             print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует.")
#         else:
#             print(f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует.")
#
#
# s = Sides(1, 2, 3)
# print(s.c)
# print(s.__dict__)
# Sides(2, 5, 6).check()
# Sides(5, 2, 8).check()
# Sides(7, 3, 6).check()

#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, group, rating):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, speciality, experience):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"\n{self.speciality} {self.experience}")
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, speciality, group, rating, topic):
#         super().__init__(surname, name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"\n{self.topic}", end=' ')
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
#     ]
#
# for i in group:
#     i.info()

# Упаковка данных (сериализация)
# Распаковка данных (дусуриализация)

# json

# dump() - сохраняет данные в открытый файл
# load() - считывает данные из открытого файла

# dumps() - сохраняет данные в строку
# loads() - считывает данные из строки

# import pickle

# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "овощи": 'морковь',
#     "бюджет": 1000
# }
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, 'rb') as f:
#     shop_list_2 = pickle.load(f)
# print(shop_list_2)


# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#     d = {"first": 'a', 'second': 2}
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nКортеж: {Test.tpl}\nСловарь: {Test.d}"
#
#
# obj = Test()
# # print(obj)
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
# obj = pickle.loads(my_obj)
# print(obj.num)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# import json
#
# data = {
#     'name': 'Olga',
#     'age': 35,
#     "20": None,
#     "True": 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'firstname': 'Alice',
#             'age': 6
#         }
#     ]
# }

# with open('data_file.json', 'w') as f:
#     json.dump(data, f, indent=4)
#
# with open('data_file.json') as f:
#     data1 = json.load(f)
# print(data1)

# json_string = json.dumps(data, sort_keys=True)
# # print(json_string)
#
# data1 = json.loads(json_string)
# print(data1)
# print(data1['name'])

# import json
#
# x = {
#     "name": "Виктор"
# }
# d = json.dumps(x)
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))
# data1 = json.loads(d)
# print(data1)


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'm', 'n', 'k']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open('persons1.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict
#     with open('persons1.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     print(i)
#     write_json(gen_person()[0], gen_person()[1])


# for i in range(5):
#     person.append(gen_person())

# with open('persons.json', 'w') as f:
#     json.dump(person, f, indent=2)
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ''
#         # for i in self.marks:
#         #     a += str(i) + ", "
#         # return f"Студент: {self.name} - {a[:-2]}"
#         a = ", ".join(map(str, self.marks))
#         return f"Студент: {self.name} - {a}"
#
#     # def __repr__(self):
#     #     a = ", ".join(map(str, self.marks))
#     #     return f"Студент: {self.name} - {a}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': self.name, 'marks': self.marks})
#         with open(file_name, 'w') as f:
#             json.dump(data, f)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = "\n".join(map(str, self.students))
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_group(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         with open(file_name, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             json.dump(stud_list, f, indent=2)
#
#     @staticmethod
#     def upload_journal(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Niekolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# file1 = 'Student_list.json'
# # st1.dump_to_json(file1)
# # st1.load_from_file(file1)
# st2.dump_to_json(file1)
# Student.load_from_file(file1)
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(1, 5)
# # print(st1)
# # print(st1.average_mark())
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# # # print(my_group)
# my_group.add_student(st3)
# # # print(my_group)
# my_group.remove_student(1)
# # print()
# # print(my_group)
# #
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# # print(my_group2)
# Group.change_group(my_group, my_group2, 0)
# # print()
# # print(my_group)
# # print()
# # print(my_group2)
# file2 = "Group_list.json"
# my_group.dump_group(file2)
# Group.upload_journal(file2)


# pip install requests

# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(response.text)
# todos = json.loads(response.text)
#
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_user = " and ".join(users)
# print(max_user)
#
# n = 's' if len(users) > 1 else ''
# print(f"User{n} {max_user} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)

# CSV (Comma Separated Values - )

# import csv

# with open('data2.csv') as f:
#     file_reader = csv.reader(f, delimiter=',')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы {', '.join(row)}")
#         else:
#             print(f"\t\t{row[0]} - {row[1]}, Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")

# import csv

# with open('data2.csv') as f:
#     file_reader = csv.reader(f, delimiter=';')
#     for row in file_reader:
#         print(row)


# with open('data2.csv') as f:
#     fields = ['Имя', "Профессия", 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=';', fieldnames=fields)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы {'; '.join(row)}")
#         print(f"\t\t{row[0]} - {row[1]}, Родился в {row[2]} году.")
#         count += 0


# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
#
# with open('data_new.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     for row in data:
#         writer.writerow(row)
#     writer.writerow(data)

# with open('student1.csv', 'w') as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     writer.writerow({"Имя": "Саша", "Возраст": "7"})
#     writer.writerow({"Имя": "Саша", "Возраст": "12"})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_writer.csv', 'w') as f:
#     write = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     write.writeheader()
#     for d in data:
#         write.writerow(d)

# from bs4 import BeautifulSoup
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find('div', class_='row')
# print(row)

# import requests
#
# res = requests.get("https://ru.wordpress.org/")
# res.encoding = 'utf-8'
# # print(res.headers['content-type'])
# # print(res.content)
# print(res.text)

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find('header', id='masthead').find('p', class_='site-title').text
#     print(p1)
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     res.encoding = 'utf-8'
#     return res.text
#
#
# def write_csv(data):
#     with open('pars.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['tip'], data['t']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('div', class_='hide-header section')[0]
#     texts = p1.find_all('div', class_='section')
#     for text in texts:
#         name = text.find('h2').text
#         tip = text.find('p').text
#         lis = text.find_all('li', class_='toctree-l1')
#         for li in lis:
#             t = li.find('a', class_="reference internal").text
#             uls = li.find_all('li', class_='toctree-l2')
#             data = {'name': name, 'tip': tip, 't': t}
#             write_csv(data)
#
#
# def main():
#     url = "https://flask.palletsprojects.com/en/2.0.x/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r'\D+', '', s)
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('section', class_='plugin-section')[3]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a').get('href')
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r'\D+', '', s)
#
#
# def write_csv(data):
#     with open('flask.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('section', class_='hide-header section')[1]
#     plugins = p1.find_all('article')
#     print(plugins)
#     # for plugin in plugins:
#     #     name = plugin.find('h1').text
#         # url = plugin.find('h3').find('a').get('href')
#         # rating = plugin.find('span', class_='rating-count').find('a').text
#         # r = refined(rating)
#
#         # data = {'name': name, 'url': url, 'rating': r}
#         # write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins_1.csv", 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy'],))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('article', class_='plugin-card')
#     for el in p1:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ""
#
#         try:
#             url = el.find('h3').find('a')['href']
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_='entry-excerpt').find('p').text
#         except ValueError:
#             snippet = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ""
#
#         try:
#             c = el.find('span', class_='tested-with').text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#
#         write_csv(data)
#
#
# def main():
#     for i in range(2, 5):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/top/#", "news2.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# import socket
#
# URLS = {
#     '/': "index page",
#     '/blog': 'blog page'
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found\n\n', 404
#     return 'HTTP/1.1 200!\n\n', 200
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     # body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))  # 127.0.0.1:5000
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n{request}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()

# import socket
#
#
# URLS = {
#     '/': 'index page',
#     '/blog': 'blog page'
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return "HTTP/1.1 404 Page Not Found\n\n", 404
#     return "HTTP/1.1 200!\n\n", 200
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = URLS[url]
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(("127.0.0.1", 5000))  # 127.0.0.1:5000
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(f"Клиент: {addr} => \n {request}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(request)
#         client_socket.close()
#
#
# if __name__ == '__main__':
#     run()
#
#
# def parse_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     return headers.encode()


# import sqlite3
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     #  id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # phone BLOB NOT NULL DEFAULT '+79090000000'
#     # age INTEGER CHECK(age > 0 AND age < 100)
#     # email TEXT UNIQUE
#     # )""")
#     #
#     # cur.execute("""
#     # ALTER TABLE person
#     # RENAME TO person_table
#     # """)
#
#     # cur.execute("""
#     # ALTER TABLE person_table
#     # ADD COLUMN address TEXT NOT NULL DEFAULT 'city, address'
#     # """)
#
#     cur.execute("""
#     DROP TABLE person_table
#     """)


# import sqlite3
#
# cars = [
#     ('BMW', 54000),
#     ('Chevrolet', 51000)
# ]
#
# with sqlite3.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#         )
#         """)
#
#     cur.executescript("""
#             DELETE FROM cars WHERE model LIKE 'B%';
#             UPDATE cars SET price = price + 100;
#             """)
#
#     cur.execute("UPDATE cars SET price=0 WHERE model LIKE 'B%'", {"Price": 0})
#
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", cars)
#
#     for car in cars:
#         cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
#
#     cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000")
#     cur.execute("INSERT INTO cars VALUES(2, 'Renault', 22000")
#     cur.execute("INSERT INTO cars VALUES(3, 'Renault', 22000")
#     cur.execute("INSERT INTO cars VALUES(4, 'Renault', 22000")
#
# con = None
# try:
#     con = sqlite3.connect('cars.db')
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса" + str(e))
# finally:
#     if con:
#         con.close()
#
#
# with sqlite3.connect("cars.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     cur.execute("SELECT model, price FROM cars")
#
#     rows = cur.fetchone()
#     print(rows)
#
#     rows2 = cur.fetchone(5)
#     print(rows2)
#
#     for res in cur:
#         print(res['model'], res['price'])
#
#
# with sqlite3.connect('cars.db') as con:
#     cur = con.cursor()
#
#     with open('sql_dump.sql', 'w') as f:
#         for sql in con.iterdump():
#             f.write(sql)
#
# with sqlite3.connect('cars_dump.db') as con:
#     cur = con.cursor()
#
#     with open('sql_dump.sql', 'r') as f:
#         sql = f.read()
#         cur.executescript(sql)


import sqlite3

headphones = [
    ('Razor', 22000),
    ('Bloody', 12000),
    ('Sennheiser', 15000),
]

with sqlite3.connect("headphones.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS headphones(
        headphones_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )
    """)

    for headphone in headphones:
        cur.execute("INSERT INTO headphones VALUES(NULL, ?, ?)", headphone)

# ORM - SQLAlchemy

# pip install sqlalchemy

# import os
#
# from sqlalchemy import and_, or_, not_, distinct
#
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
#
# from models.lesson import Lesson, association_table
# from models.student import Student
# from models.group import Group
#
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
#
#     # print(session.query(Lesson).all())
#     # print("*" * 60)
#
#     # for it in session.query(Lesson):
#     #     print(it)
#
#     # for it in session.query(Lesson).filter(not_(Lesson.id > 3), not_(Lesson.lesson_title.like('M%'))):
#     #     print(it)
#
#     # print(session.query(Lesson).filter(Lesson.lesson_title is None).all())
#     # print('*' * 60)
#
#     # print(session.query(Student).filter(not_(Student.age.between(16,17))).all())
#     # print('*' * 60)
#
#     # for it in session.query(distinct(Student.age)).filter(Student.age < 20):
#     #     print(it)
#
#     # for it in session.query(Lesson):
#     #     print(it)
#     #
#     # i = session.query(Lesson).first()
#     # i.lesson_title = "Информатика"
#     # session.add(i)
#     # session.commit()
#
#     # for it in session.query(Lesson):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # session.query(Lesson).filter(
#     #     Lesson.lesson_title.like('%м%')
#     # ).update({'lesson_title': 'M'},
#     #          synchronize_session='fetch')
#     # session.commit()
#
#     i = session.query(Lesson).filter(Lesson.lesson_title == "Физика").first()
#     session.delete(i)
#     session.commit()

# Jinja
# pip install jinja

# from jinja2 import Template
#
# name = "Игорь"
# age = 28
# per = {"name": "Игорь", "age": 28}
#
# tm = Template("Привет {{ p.name.upper() }}. Тебе {{ p['age'] }} лет")
# msg = tm.render(p=per)
#
# print(msg)
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age

# from jinja2 import Template
#
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'GG'},
#     {'id': 3, 'city': 'Мds'},
#     {'id': 4, 'city': 'Мdd'},
#     {'id': 5, 'city': 'Мdas'},
# ]
#
# link = """<select name="sities">
# {%- for c in cities %}
#     {%- if c.id > 3 %}
#     <option value="{{ c.id }}">{{ c.city }}</option>
#     {% elif c.city == 'Москва' %}
#     <option>{{ c.city }}</option>
#     {% else %}
#     {{ c['city'] }}
#     {%- endif %}
# {%- endfor %}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# from jinja2 import Template
#
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolsvagen', 'price': 21300},
# ]
#
# # tpl = "{{ (cs | min(attribute='price')).model }}"
# tpl = "{{ cs | random }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# from jinja2 import Template
#
# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.0},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.5},
# ]
#
# tpl = """
# {%- for u in users %}
#     {% filter upper %}{{ u.name}} {% endfilter%}
#     {%- filter string %}{{ u.year }} - {{ u.weight }}{% endfilter%}
# {%- endfor%}
# """
#
# tm = Template(tpl)
# msg = tm.render(users=persons)
#
# print(msg)


# from jinja2 import Template
#
# html = """
# {% macro text_input(name, value='', type='text', size=20 ) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ text_input('username') }}</p>
# <p>{{ text_input('email') }}</p>
# <p>{{ text_input('password', 'Пароль', 'password') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# from jinja2 import Template
#
# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.0},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.5},
# ]
#
# html = """
# {%- macro list_users(list_of_user) %}
#     <ul>
#         {%- for u in list_of_user %}
#         <li>{{ u.name }} {{ caller(u)}}</li
#         {%- endfor%}
#     </ul>
#
# {%- endmacro %}
#
# {%- call(user) list_users(users) %}
#     <ul>
#         <li>age: {{ user.year }}</li>
#         <li>weight: {{ user.weight }}</li>
#     </ul>
# {%- endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)

# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.0},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.5},
# ]
#
# subs = ["Культура", "Наука", "Политика", "Спорт"]
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render(list_ta

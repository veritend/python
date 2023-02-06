# name_first = "NIKITA"
# print("Hello,", name_first)
# age = 20
# print(age)

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


# from math import pi
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

from random import randint

s = list(randint(1, 20) for i in range(10))
print(s)
print("\nMin: ", min(s), "\nMax: ", max(s))

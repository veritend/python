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

from math import pi

s_1 = lambda x: 2 * x * pi
s_2 = lambda y: lambda x: y * x
s_3 = lambda h: lambda b: lambda a: h*(a + b)/2

add = s_2(10)
add_1 = s_3(3)
print("Площадь окружности радиуса 2: ", s_1(2))
print("Площадь треугольника размером 10*13: ", add(13))
print("Площадь треугольника размером 10*13: ", add_1(5)(7))

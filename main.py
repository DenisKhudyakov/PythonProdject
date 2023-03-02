
#Задачка №1
a, b, c, d = 8, 10, 12, 18
res = ((-3 + a ** 2) * 10 - 2 ** 3) / (c - 2 * d)
print(res)

#Задачка 2
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите третье число: '))
number4 = int(input('Введите четвертое число: '))
res = (number1 + number2) / (number3 + number4)
print(res)

#Задачка 3
number = int(input('Введите число: '))
print('После числа', number, 'идёт число', number + 1)
print('До числа', number, 'идёт число', number - 1)

#Задачка 4
a = int(input('Введите длину первого катета: '))
b = int(input('Введите длину второго катета: '))
print('Площадь треугольника = ', (a * b) / 2)

#Задачка 5
clock = int(input('Введите время в минутах: '))
hour = clock // 60
minute = clock % 60
print('Длительность процесса составила:', hour, 'часов', minute, 'минут')

#Задачка 6
number5 = int(input('Введите первое число: '))
number6 = int(input('Введите второе число: '))
sum = number5 % 100 + number6 % 100
print('Сумма:', sum)

#Задачка 7
number7 = int(input('Введите четырёхзначное число: '))
print('Тысячи', number7 // 1000)
print('Сотни', int((number7 % 1000 - number7 % 100) / 100))
print('Десятки', int((number7 % 100 - number7 % 10) / 10))
print('Единицы', number7 % 10)

#Задачка 8
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)


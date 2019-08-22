# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

print("Задание 1")
equation = 'y = -12x + 11111140.2121'
x = 2.5
k=float(equation.split()[2][:equation.split()[2].find("x")])
b=float(equation.split()[4])
print("Значение y для функции ",equation," при x = ",x," составит: ", k*x+b)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)
print("Задание 2")
# Пример корректной даты
date = '31.05.1985'
while not (len(date)== 10 and date[2]==date[5]=="."):
    date=input("Некорректный синтаксис даты, введите в формате dd.mm.yyyy: ")
dd=int(date.split(".")[0])
mm=int(date.split(".")[1])
yyyy=int(date.split(".")[2])
if yyyy>0 and yyyy<10000:
    if mm>0 and mm<13:
        if mm in (1,3,5,7,8,10,12):
            if dd>0 and dd <32:
                print("OK. Верный формат даты")
            else:
                print("Неправильно. Количество дней неверно")
        elif dd>0 and dd <31:
                print("OK. Верный формат даты")
        else:
            print("Неправильно. Количество дней неверно")
    else:
        print("Неправильно. Месяц указан неверно")
else:
    print("Неправильно. Год указан неверно")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.

print("Задание 3")
room=15
n=1
k=room
f=0
if room == 1:
    print("1 1")
else:
    while n * (n + 1) * (2 * n + 1) / 6 < room:
        f = f + n
        k = k - n**2
        n = n + 1
    count = (k - 1) % n + 1
    floor = (k - count) // n + 1
    print(f + floor,count)

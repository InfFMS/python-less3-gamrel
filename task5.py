# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.
x=int(input())
a=0
b=0
t=0
while (x>0):
    n = int(1)
    while (n < x + 1):
        if ((2 ** n) == x):
            a += 1
            b += x
            t += 1
        n += 1
    x = int(input())
if t>0:print(b/a)
else: print('нет')
#оформить ответ


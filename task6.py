# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
x=int(input())
a=0
B=x
C=x
while (x!=0):
    while (x>0):
        if (B<x):B=x
        elif (C>x): C=x
        x = int(input())
    while (x<0):
        if (B<x):B=x
        elif (C>x): C=x
        x = int(input())
if (B==C): print(B)
else: print(B, C)
#сделать отрицательные числа
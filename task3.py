# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.
import math
x=int(input())
a=0
t=0
n=1
c=0
while (x>0):
    while (n<x+1):
        if((x%n)==0):
            t+=1
        n+=1
    n=1
    x=int(input())
    if(t==2): a+=1
    else: c+=1
    t=0
print(a, c)
#почти пусто
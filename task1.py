#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.
x=int(input())
a=0
c=0
while (abs(x)>0):
    if (x>0):a+=1
    else: c+=1
    x = int(input())
print (a, c)
#оформить ответ
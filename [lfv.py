N=int(input())
t=0
a=0
n=1
c=0
m=0
for i in range(N):
    x = int(input())
    while (m<1):
        C=x
        B=x
        m+=1
    while (n < x + 1):
        if ((x % n) == 0):
                t += 1
        n += 1
    n = 1
    if (t == 2):
        a+=1
        if (B < x):
                B = x
        elif (C > x):
                C = x
    t=0
if(a>0): print(B,C)
else: ('нет')
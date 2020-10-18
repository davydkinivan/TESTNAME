from math import *

def area(x1,y1,x2,y2,x3,y3):
    a=sqrt((x1-x2)**2+(y1-y2)**2)
    b=sqrt((x3-x2)**2+(y3-y2)**2)
    c=sqrt((x1-x3)**2+(y1-y3)**2)
    p=0.5*(a+b+c)
    return sqrt(p*(p-a)*(p-b)*(p-c))

n=int(input())
x=[0]*n
y=[0]*n
for i in range(0,n):
    x[i],y[i] = [int(s) for s in input().split()]
s=0
for i in range(1,n-1):
    s+=area(x[0],y[0],x[i],y[i],x[i+1],y[i+1])
print(round(s,1))


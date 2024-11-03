import math

x=10
y=12
num=20
den=0
b=2
c=5
a=1



if x < 0 :
    x=-x
if x < y :
    temp=x
    x=y
    y=temp
if x > y :
    maximum=x
else:
    maximum=y
if den ==0 :
    print('division by zero')
else :
    print('remainder='+ num % den)

discriminant=(b*b) -4 *a*c
if discriminant < 0 :
    print('no real roots')
else:
    d=math.sqrt(discriminant)
    b-=b
    print(( b + d )/2.0)
    
    print((b-d )/2.0)



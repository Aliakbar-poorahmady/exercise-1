import math
n=0
x=10
# indentation
if x>=0:
    print('Not ', end='')
    print('negative')

if x >=0:
    print('Not', end=' ')
    print ('negative')

# write first n+1 powers of 2
power = 1
for i in range(n + 1):
    print(str(i) +' ' + str(power))
    power *= 2

# compute a finite sum
total = 0
for i  in range(1, n+1):
    total += i
    print(total)

# compute a finite product
product = 1
for i in range(1, n+1):
    product *= i
print(product)

# print a table of function values
for i in range(n+ 1):
    print(str(i)+'   '+ str(2 * math.pi * i/ n))
# import math

# print(math.gcd(253, 341))
a = 341 % 253
c = 253 % a
e = a % c
c = c % e
print(c)

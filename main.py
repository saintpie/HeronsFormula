import math

a = int(input())
b = int(input())
c = int(input())
P = (a + b + c) / 2
S  = math.sqrt(P * (P - a) * (P - b) * (P - c))
print(P)
print(S)







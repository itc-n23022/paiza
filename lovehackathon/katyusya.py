import math

n,p = map(int,input().split())
m,q = map(int,input().split())

answer = math.ceil(n/m)*q + n*p
print(answer)

N = int(input())
N = int(input())
A = set(map(int, input().split()))
N = int(input())
B = set(map(int, input().split()))
C = sorted(list(B.difference(A)))
if C:
    print(*C)
else:
    print("None")

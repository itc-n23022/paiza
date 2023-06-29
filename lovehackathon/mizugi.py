n, m = map(int, input().split())

s = input()
t = input()

counter = {}
for c in s:
    if not c in counter:
        counter[c] = 1
    else:
        counter[c] += 1
for c in t:
    if not c in counter:
        counter[c] = -1
    else:
        counter[c] -= 1

answer = sum(-1 * i for i in counter.values() if i < 0)
print(answer)

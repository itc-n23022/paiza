n = int(input())
m = int(input())
s = ""
for i in range(m):
    if i // n % 2 == 0:
        s += "R"
    else:
        s += "W"
print(s)

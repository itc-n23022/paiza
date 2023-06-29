N = int(input())

eue2 = 0
temp = 0
lasttime = 0
for i in range(N):
    ti, si = input().split()
    up = 5 if si == "in" else 3
    tdiff = int(ti) - lasttime
    eue2 += up
    temp += up - tdiff if temp - tdiff >= 0 else up - temp
    lasttime = int(ti)
temp -= 24 - lasttime

answer = 24 - eue2 + 2 * eue2 if temp <= 0 else 24 - eue2 + 2 * eue2 - temp
print(answer)

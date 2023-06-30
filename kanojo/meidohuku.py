def f(n, m):
    list = []
    for i in m:
        over = 0 if i == 0 else 60 if i == 180 else 60 - i // 3
        if over in [0, 60]:
            list.append("00:00" if over == 60 else "01:00")
        else:
            list.append(
                f"00:{over:02d}"
                if over > 0
                else f"{(24*60+over)//60:02d}:{(24*60+over)%60:02d}"
            )
    return "\n".join(list)


n = int(input())
m = [int(input()) for _ in range(n)]

result = f(n, m)
print(result)

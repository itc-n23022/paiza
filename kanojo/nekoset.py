def f(s):
    c, a, t = s.count("c"), s.count("a"), s.count("t")
    mn, mx = min(c, a, t), max(c, a, t)
    return "\n".join(str(i) for i in [mn, mx - c, mx - a, mx - t])


s = input()

result = f(s)
print(result)

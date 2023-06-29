def func1(s, t):
    print("".join(["+" if i == t - 1 else "-" for i in range(s)]))


def func2(s, t):
    print("-" * (t - 1) + "+" + "-" * (s - t))


def func3(s, t):
    line = "-" * s
    print("{}+{}".format(line[: t - 1], line[t:]))


def func4(s, t):
    array = ["-"] * s
    array[t - 1] = "+"
    return array


def display(array):
    print("".join(array))


if __name__ == "__main__":
    s, t = [int(input()) for _ in range(2)]
    display(func4(s, t))

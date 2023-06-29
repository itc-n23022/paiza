def func1(des):
    count = sum(1 for d, e in des if d == e)

    if count >= 3:
        return "OK"
    else:
        return "NG"


def func2(des):
    count = sum(d == e for d, e in des)

    return "OK" if count >= 3 else "NG"


def func3(des):
    count = sum(d == e for d, e in des)

    return "OK" if count >= 3 else "NG"


if __name__ == "__main__":
    des = [input().split() for _ in range(5)]
    result = func3(des)
    print(result)

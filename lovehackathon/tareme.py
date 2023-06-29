def check_condition(s, n):
    return 'OK' if s >= n else 'NG'

if __name__ == '__main__':
    s, n = map(int, input().split())
    result = check_condition(s, n)
    print(result)

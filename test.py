n = 4567


def cal(n):
    for i in range(2, n + 1):
        if n % 2 == 0:
            print("x")
            break

    return n


print(cal(n))

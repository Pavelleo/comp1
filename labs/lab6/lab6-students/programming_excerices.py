def sum_odd_while_v2(n):
    """(int)->int
    Returns the sum of all odd integers between 5 and n
    """
    s = 0
    i = 5
    while i <= n:
        s += i
        i += 2

    return s


def ex2():
    ansa = "yes"
    while ansa == "yes":
        num1 = int(input("give one number: "))
        num2 = int(input("give second number: "))
        print(num1 + num2)
        ansa = input("do you wish to continue: ")


def first_neg(l):
    if len(l) == 0:
        return

    i = 0
    while i < len(l):
        if l[i] < 0:
            return i

        i += 1


def sum_5_consecutive_for(a):
    if len(a) < 5:
        return False

    for i in range(len(a) - 4):
        if a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4] == 0:
            return True

    return False


def sum_5_consecutive_while(a):
    if len(a) < 5:
        return False

    i = 0
    while i < len(a) - 4:
        if a[i] + a[i + 1] + a[i + 2] + a[i + 3] + a[i + 4] == 0:
            return True
        i = i + 1

    return False


def fib(n):
    fib = [1] * n
    i = 2
    while i < n:
        fib[i] = fib[i - 1] + fib[i - 2]
        i = i + 1

    return fib


def inner_product(x, y):
    inn = 0
    for i in range(len(x)):
        inn = inn + x[i] * y[i]

    return inn

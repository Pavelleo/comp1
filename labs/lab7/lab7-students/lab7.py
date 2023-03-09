def indexes(w, l):
    out = []

    for i in range(len(w)):
        if w[i] == l:
            out.append(i)

    return out


def doubles(l):
    for i in range(1, len(l)):
        if l[i] == 2 * l[i - 1]:
            print(l[i])


def four_letter(l):
    out = []

    for i in l:
        if len(i) == 4:
            out.append(i)

    return out


def inBoth(a, b):
    for i in a:
        if i in b:
            return True

    return False


def intersect(a, b):
    out = []

    for i in a:
        if i in b:
            out.append(i)

    return out


def pair(a, b, n):
    for i in a:
        for j in b:
            if i + j == n:
                print(i, j)


def pairSum(l, n):
    bruh = []

    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] + l[j] == n and (l[i] not in bruh or l[j] not in bruh):
                print(i, j)
                bruh.append(l[i])
                bruh.append(l[j])


def lastfirst(l):
    first = []
    last = []

    for i in range(len(l)):
        bruh = l[i].split(",")
        last.append(bruh[0])
        first.append(bruh[1])

    return [first, last]


def subsetSum(l, n):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == n:
                    return True
    return False


def mystery(n):
    out = 0
    while n / 2 >= 1:
        n /= 2
        out += 1

    return out


def inversions(s):
    inv = 0

    for i in range(len(s) - 1, -1, -1):
        for j in range(0, i):
            if s[i] < s[j]:
                inv += 1

    return inv


def sublist(l1, l2):
    bruh = []

    for i in l2:
        if i in l1:
            bruh.append(i)

    return bruh == l1


def mssl(l):
    negative = 0
    for i in l:
        if i < 0:
            negative += 1

    if negative == len(l):
        return 0

    bruh = 0
    temp = 0

    for i in l:
        bruh += i
        if bruh > temp:
            temp = bruh

    return bruh

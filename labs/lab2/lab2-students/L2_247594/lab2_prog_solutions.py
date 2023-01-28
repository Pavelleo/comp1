# ===========================================================================================
# Programming exercises 1
def repeater(s1, s2, n):
    newString = (s1 + s2) * n
    return "_" + newString + "_"


# ===========================================================================================
# Programming exercises 2
def roots(a, b, c):
    root1 = ((-1 * b) + (b**2 - 4 * a * c) ** 0.5) / 2 * a
    root2 = ((-1 * b) - (b**2 - 4 * a * c) ** 0.5) / 2 * a
    return str(root1) + " and " + str(root2)


# ===========================================================================================
# Programming exercises 3
def real_roots(a, b, c):
    return (b**2 - 4 * a * c) >= 0


# ===========================================================================================
# Programming exercises 4
def reverse(x):
    num1 = x // 10
    num2 = x - (10 * num1)
    return (num2 * 10) + num1

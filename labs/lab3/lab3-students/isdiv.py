# exercise 3a
# (int, int) -> bool
# true if the first number(n) is divisible by the second number(m), false if otherwise
def is_divisible(n, m):
    return n % m == 0


# exercise 3a
# (int) -> str
# returns "yes" if the number given is divisible by 2 or 3 and not 8, return "no" otherwise
def is_divisible23n8(x):
    if (is_divisible(x, 2) or is_divisible(x, 3)) and not is_divisible(x, 8):
        return "yes"
    else:
        return "no"


x = int(input("Enter and integer: "))
if is_divisible23n8(x) == "yes":
    print(x, "is divisible by 2 or 3 but not 8")
else:
    print("It is not true that", x, "is divisible by 2 or 3 but not 8")

# Course: IT1 1120
# Lab 3
# Nangfack, Pavel
# 300247594

# ======================================================================================================================================================


# exercise 1
# (number, number) -> number
# takes a wage and the amount of hours worked, then determines the amount of pay with proper overtime pay
def pay(wage, hours):
    if 40 < hours <= 60:
        return (40 * wage) + (wage * (hours - 40) * 1.5)
    elif hours > 60:
        return (40 * wage) + (20 * wage * 1.5) + (wage * (hours - 60) * 2)
    else:
        return hours * wage


# ======================================================================================================================================================


# exercise 2
# (char, char) -> int
# rock paper scissors game where you get input of player 1 and 2 and get the result relative to player 1
def rps(p1, p2):
    if p1 == p2:
        return 0
    elif p1 == "R" and p2 == "P":
        return 1
    elif p1 == "R" and p2 == "S":
        return -1
    elif p1 == "P" and p2 == "R":
        return -1
    elif p1 == "P" and p2 == "S":
        return 1
    elif p1 == "S" and p2 == "R":
        return 1
    elif p1 == "S" and p2 == "P":
        return -1


# ======================================================================================================================================================


# exercise 3a
# (int, int) -> bool
# true if the first number(n) is divisible by the second number(m), false if otherwise
def is_divisible(n, m):
    return n % m == 0


n = int(input("Enter 1st integer: \n"))
m = int(input("Enter 2nd integer: \n"))

if is_divisible(n, m):
    print(n, "is divisible by", m)
else:
    print(n, "is not divisible by", m)

# Course: IT1 1120
# Assignment 3
# Nangfack, Pavel
# 300247594

# ======================================================================================================================================================


# question 1
# (str) -> boolean
# takes in a string as input and returns true if somewhere in the string there is an instance of the same letter 3 times in a row, false if not
def triples(str):
    s = 0

    for i in range(len(str) - 1):
        if str[i + 1] == str[i]:
            s += 1
            if s == 2:
                return True
        else:
            s = 0

    return s >= 2


# ======================================================================================================================================================


# question 2
# (str) -> str
# takes in a string, returns a new string that is in the form of every letter followed by the amount of times that letter was repeated in a row
def countMe(s):
    final = ""
    count = 1
    letter = s[0]

    # store the first letter
    # increment and if leetter == s[i] then count ++
    # else then append that number to the string and make letter the new letter u r on
    for i in range(len(s) - 1):
        if letter == s[i + 1]:
            count += 1
        else:
            final = final + s[i] + str(count)
            letter = s[i + 1]
            count = 1

    final = final + s[len(s) - 1] + str(count)

    return final


# ======================================================================================================================================================


# question 3
# (int) -> int
# takes a number as input and returns the sum of all its positive odd divisors
def sum_odd_divisors(x):
    if x == 0:
        return

    if x < 0:
        x = x * -1

    div = 1
    s = 0

    while div != x + 1:
        if x % div == 0:
            if div % 2 == 1:
                s += div
        div += 1

    return s


# ======================================================================================================================================================


# question 4
# (str) -> str
# takes a string as input and encrypts the string according to the given encryption pattern then returns that encrypted string
def encrypt(s):
    rep = ""

    for i in range(len(s)):
        rep = rep + s[len(s) - i - 1]

    out = ""
    for i in range(len(rep)):
        if i % 2 == 0:
            out = out + rep[int(i / 2) + i % 2]
        else:
            out = out + rep[len(rep) - (int(i / 2) + i % 2)]

    return out

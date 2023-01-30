# Course: IT1 1120
# Assignment 2
# Nangfack, Pavel
# 300247594

# ======================================================================================================================================================


# question 1
# (int, int) -> boolean
# using parameters it determines if the skating rink is open
def skate(thick, temp):
    return thick >= 30 and temp <= -10


# ======================================================================================================================================================


# question 2
# (int) -> none
# inputs a number grade and determines the letter grade
def alphaNote(num):
    if 100 >= num >= 90:
        return "A+"
    if 90 > num >= 85:
        return "A"
    if 85 > num >= 80:
        return "A-"
    if 80 > num >= 75:
        return "B+"
    if 75 > num >= 70:
        return "B"
    if 70 > num >= 65:
        return "C+"
    if 65 > num >= 60:
        return "C"
    if 60 > num >= 55:
        return "D+"
    if 55 > num >= 50:
        return "D"
    if 50 > num >= 40:
        return "E"
    if 40 > num >= 0:
        return "F"
    return


# ======================================================================================================================================================


# question 3
# () -> none
# asks user for a valid mark, if the user inputs something outside of the range of a valid mark it asks again
# if the user inputs a valid mark it gives the letter grade and wether the mark is a pass or fail
def alphaNoteVerif():
    note = -1
    passed = ""

    while 0 > note or note > 100:
        note = int(float(input("Please input the final mark (from 0 to 100): ")))

    if note < 50:
        passed = "Failed"
    else:
        passed = "Passed"

    print("The letter mark is: " + str(alphaNote(note)) + "\n" + passed)


# ======================================================================================================================================================


# question 4
# (int) -> none
# first loops starting from 1 and increments by 2 numbers until it reaches n
# loops a second time starting from n and decrementing by 2 until 0
def loops(n):

    for i in range(int(n / 2) + n % 2):
        print(str(i * 2 + 1) + " ", end="")

    print()

    for i in range(int(n / 2) + n % 2):
        print(str(n - (i * 2)) + " ", end="")


# ======================================================================================================================================================


# question 5
# (str) -> boolean
# checks for different password requirements and returns true if the pasword is valid and false if not
def test_password(pw):
    valid = 0
    hasUpper = False
    hasLower = False
    hasNumbers = False

    if 8 <= len(pw) <= 16:
        valid += 1

    if "@" in pw or "-" in pw or "#" in pw or "$" in pw or "%" in pw:
        valid += 1

    for i in pw:
        if i.isupper():
            hasUpper = True
    if hasUpper:
        valid += 1

    for i in pw:
        if i.islower():
            hasLower = True
    if hasLower:
        valid += 1

    for i in pw:
        if i.isnumeric():
            hasNumbers = True
    if hasNumbers:
        valid += 1

    return valid == 5


# () -> none
# tester to test the test_password() function with user input
def tester():
    pw = input("Enter your password: ")

    if test_password(pw):
        print("Great, your password meets all requirements")
    else:
        print("Try again, your password does not meet all requirements")

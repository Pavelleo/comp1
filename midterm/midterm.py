# ---------------------Part II: Coding ---------------------#
# Pavel Nangfack
# 300247594


def alpha(s):
    if s == "613" or s == "343":
        return "Ottawa"
    elif s == "819":
        return "Gatineau"
    else:
        return "xxxx"


def beta():
    code = input("What is the area code of your phone? ")
    if alpha(code) == "Ottawa":
        return True
    else:
        return False


i = 20

while True:
    if i % 2 == 0:
        break
    print(i)
    i = i + 2

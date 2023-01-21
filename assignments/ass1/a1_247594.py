# Course: IT1 1120
# Assignment 1
# Nangfack, Pavel
# 300247594

# ======================================================================================================================================================


# question 1
# (int) -> int
# function reverses a given integer without using string data type
def reverse_int(toReverse):

    # get each digit of the number and assign them to num1-3
    num1 = int(toReverse / 100)
    num2 = int((toReverse - (num1 * 100)) / 10)
    num3 = int(toReverse - (num1 * 100) - (num2 * 10))

    # return the digits into the places that would reverse the numbers
    return num3 * 100 + num2 * 10 + num1


# ======================================================================================================================================================


# question 2
# (float, float, float, float, float) -> float
# function to calculate the final mark of a student given different class component marks
def finalMark(labs, assignments, test, midterm, exam):

    # return calculation of final mark
    return (
        (labs * 0.1)
        + (assignments * 0.2)
        + (test * 0.1)
        + (midterm * 0.2)
        + (exam * 0.4)
    )


# ======================================================================================================================================================


# question 3
# (str, str, str, str, int) -> str
# takes parameters and prints a description of a book in a certain format
def bibformat(author, title, city, publisher, year):

    # return formatted string
    return author + " (" + str(year) + "). " + title + ". " + city + ": " + publisher


# ======================================================================================================================================================


# question 4
# () -> none
# takes user input and prints a description of a book in a certain format
def bibformatPrint():

    # get every needed user input
    author = input("Enter the name of the author: ")
    title = input("Enter the title of a book: ")
    city = input("In what city are the headquarters of the publisher? ")
    publisher = input("Enter the name of the publisher: ")
    year = input("What year was the book bublished? ")

    # return formatted string
    print(author + " (" + str(year) + "). " + title + ". " + city + ": " + publisher)


# ======================================================================================================================================================


# question 5
# (float, float) -> float
# calculates how long it will take to go a given distance at a given speed and returns the time in minutes
def travelTime(distance, speed):

    # return calulated time in minutes
    return distance / speed * 60.0


# ======================================================================================================================================================


# testing
# reverse_int(456)
# finalMark(100.0, 80.0, 90.0, 83.0, 86.0)
# bibformat("TahaHussein", "Days", "Egypt", "ARN", 1967)
# travelTime(400, 100)
# bibformatPrint()

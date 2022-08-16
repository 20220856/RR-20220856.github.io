# This program determines whether an input is an integer or not.
try:
    a=int(input("Input a string: "))
    print("The input is an integer.")
except ValueError:
    print("The input is not an integer.")
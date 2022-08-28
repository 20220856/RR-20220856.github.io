# This is my first attempt at writing code.

Num1 = int(input("Enter First Number: ")) # This is the assignment of the variable for the first number
Num2 = int(input("Enter Second Number: ")) # This is the assignment of the variable for the second number
Opp = input("Enter an Arithmetic Operation: (+, -, *, /) ") # This is the assignment of a third variable, responsible for an arithmetic operation.
if (Opp == "+"):
    sum=Num1+Num2 # This operation adds the first and second number if the arithmetic input is "+"
elif (Opp == "-"):
    sum=Num1-Num2 # This operation subtracts the second number from the first if the arithmetic input is "-"
elif (Opp == "*"):
    sum=Num1*Num2 # This operation multiplies the first and second number if the arithmetic input is "*"
elif (Opp == "/"):
    sum=Num1/Num2 # This operation divides the first number by the second number if the arithmetic input is "/"
print("%d %s %d = %d" %(Num1, Opp, Num2, sum)) # This operation provides readable formatting; it takes user input, and provides an output dependant on user inputs. In practice, it prints the first number, the arithmetic operation, the second number, and the result of the arithmetic operation (eg. 2 + 4 = 6 , 3 * 5 = 15 , etc.).

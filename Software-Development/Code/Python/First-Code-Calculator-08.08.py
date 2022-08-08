#This is my first attempt at writing code.

Num1 = int(input("Enter First Number: "))
Num2 = int(input("Enter Second Number: "))
Opp = input("Enter an Arithmetic Operation: (+, -, *, /) ")
if (Opp == "+"):
    sum=Num1+Num2
elif (Opp == "-"):
    sum=Num1-Num2
elif (Opp == "*"):
    sum=Num1*Num2
elif (Opp == "/"):
    sum=Num1/Num2
print("%d %s %d = %d" %(Num1, Opp, Num2, sum))

#sum = Num1 + Num2
#print(sum)
#print("%d+%d=%d" %(Num1, Num2, sum)) # Can insert integers whilst keeping a string using %d

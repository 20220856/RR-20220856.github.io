# This program requests two inputs, checks if they are divisible by 2 or 3, multiplies them together if yes and addds them if no.

#nums=list(map(int, input("enter multiple values").split()))
#print(nums)

try:
    x,y=[int(x) for x in input("Enter two whole numbers: ").split()]
    if x and y%(2 or 3)==0:
        z=(x*y)
        print("Both numbers are divisible by either 2 or 3, and their multiplied value is:",z)
    else:
        z=(x+y)
        print("One or both numbers are not divisible by neither 2 nor 3, but their sum is",z)
except ValueError:
    print("Error: Please ensure you enter two whole numbers.")
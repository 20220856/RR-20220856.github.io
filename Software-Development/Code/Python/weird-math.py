# This program requests two inputs, checks if they are divisible by 2 or 3, multiplies them together if yes and addds them if no.

#nums=list(map(int, input("enter multiple values").split()))
#print(nums)

try: # This TRY assumes TWO integer user inputs, and redirects to the EXCEPT if it is anything else
    x,y=[int(x) for x in input("Enter two whole numbers: ").split()] # It took me such a long time to wrap my head around the use of "int(x) for x in input", but I now know this it is used to ensure that the temporary value "x" is assigned type INT (therefore meaning both "x" and "y" are of type INT). The split() is to ensure that the resulting inputs ("x" and "y") are assigned to their respective variables, rather than "x" being assigned both inputs and "y" being assigned nothing.
    if x and y%(2 or 3)==0: # Checks that BOTH inputs are either divisible by two OR three with a remainder of zero (ie. directly divisible)
        z=(x*y) # Multiplies the inputs and prints the result
        print("Both numbers are divisible by either 2 or 3, and their multiplied value is:",z)
    else: # If one or both inputs are not divisible by two OR three, adds them together instead, and prints the result
        z=(x+y)
        print("One or both numbers are not divisible by neither 2 nor 3, but their sum is",z)
except ValueError: # If the input is NOT specifically TWO integers, prints this error
    print("Error: Please ensure you enter two whole numbers.")

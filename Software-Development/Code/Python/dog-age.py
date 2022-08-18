# Write a program that calculates a dog's age in dog years.
# The first two human years are 10.5 dog years, and any after that are 4 human years.
try:
    humanage=float(input("How old is the dog in Human years? "))
    if humanage<=2:
        dogage=humanage*10.5
    else:
        dogage=(21+((humanage-2)*4))
    print("The dog is",dogage,"dog years old.")
   except:
    print("Please insert a number")

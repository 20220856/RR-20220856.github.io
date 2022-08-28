# Write a program that calculates a dog's age in dog years.
# The first two human years are 10.5 dog years, and any after that are 4 human years.

try: # I added a "Try" to ensure that the input is a float; if the input is NOT a float, the code below the Try is skipped directly to the except.
    humanage=float(input("How old is the dog in Human years? ")) # This requests the age of the dog as a FLOAT, rather than an integer, because I wanted users to be able to insert ages with decimals (for example, 3.5 years old).
    if humanage<=2:
        dogage=humanage*10.5 # Because the first two years are ALWAYS equal to 10.5, any value lower than 2 can always be multiplied directly by 10.5.
    else:
        dogage=(21+((humanage-2)*4)) # Any years OVER the first two are ALWAYS equal to 4 (rather than 10.5), so a subtraction of two years from the total to account for this, before multiplying the new total by four, (plus 21 for the two subtracted years) results in an accurate calculation.
    print("The dog is",dogage,"dog years old.")
   except: # If the value is NOT in an expected format (ie. not a float), this piece of code triggers, acting as a way to ensure only numbers are entered.
    print("Please insert a number")

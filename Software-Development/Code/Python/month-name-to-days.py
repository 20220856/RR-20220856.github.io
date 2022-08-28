# Write a program to convert month name to the number of days correspondant to that month

month=str(input("Input the Month name: ")) # Requests a string input from the user
feb="February has 28 or 29 days." # February is its own variable, as it is the only month with an entirely new, non-fixed value
a=["January","March","May","July","August","October","December"] # Months with 31 days are grouped into a LIST
b=["April","June","September","November"] # Months with 30 days are grouped into a second LIST
if month==("February"):
    print(feb) # If the month happens to be February, prints February's own message
for i in a: # My first use of a FOR loop, uses "i" as a temporary value to scan through the contents of list [a]
    if i==month: # When the temporary value "i" is the same as the user input as outlined in list [a], prints the 31 day message
        print(month,"has 31 days.")
for i in b:
    if i==month: # When the temporary value "i" is the same as the user input as outlined in list [b], prints the 30 day message
        print(month,"has 30 days.")
# I found this to be a very troublesome piece of code when I was not aware of for loops, and very easy after having figured them out.

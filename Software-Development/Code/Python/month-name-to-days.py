# Write a program to convert month name to the number of days correspondant to that month

month=str(input("Input the Month name: "))
feb="February has 28 or 29 days."
a=["January","March","May","July","August","October","December"]
b=["April","June","September","November"]
if month==("February"):
    print(feb)
for i in a:
    if i==month:
        print(month,"has 31 days.")
for i in b:
    if i==month:
        print(month,"has 30 days.")
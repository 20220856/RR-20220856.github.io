#This program provides a GUI - if it could be called that - to convert temperatures.

a=int(input(("******************************\nTemperature Conversion Program\n******************************\n\nEnter 1 for: Celsius to Fahrenheit\nEnter 2 for: Fahrenheit to Celcius\nEnter 3 to Quit\n\nInput: "))) # This acts as a menu interface, requesting one of three user inputs that will run different pieces of code.
# Small side note, I am truly glad that I was able to make the formatting nice for this proto-GUI.
if a==1: # If the user chose the first option from the menu
    a1=float(input("\nInput the temperature in Celcius: ")) # A second, floating point input is requested from the user, for the temp in Celcius to be converted to Fahrenheit
    if a1>=-273.15: # Checks the temperature is higher than absolute zero in Celcius
        a1=(a1*1.8)+32 # Celcius to Fahrenheit conversion equation
        result="{:.2f}".format(a1) # This rounds the output to TWO decimal places (as otherwise, the floating point could have infinitely recurring results
        print("The temperature is",result,"degrees Fahrenheit. ")
    else: # If the temperature is BELOW absolute zero, informs the user that it is an impossibility
        print("Temperatures cannot be below absolute zero. (-273.15°C, -459.67°F)")
elif a==2: # If the user chose the second option from the menu
    a2=float(input("Input the temperature in Fahrenheit: ")) # Floating point input for the temperature in Fahrenheit
    if a2>=-459.67: # Checks the temperature is higher than absolute zero in Fahrenheit
        a2=(a2-32)*0.5556 # Fahrenheit to Celcius conversion equation
        result="{:.2f}".format(a2) # This rounds the output to TWO decimal places (as otherwise, the floating point could have infinitely recurring results
        print("The temperature is",result,"degrees Celcius.")
    else: # If the temperature is BELOW absolute zero, informs the user that it is an impossibility
        print("Temperatures cannot be below absolute zero. (-273.15°C, -459.67°F)")
elif a==3: # If the user chose the third option from the menu
    print("Exiting program. ") # Adds a message to let the user know the program is stopping
    exit() # Forces the program to close
else: # If the user made an invalid selection (ie. did not input exactly 1, 2, or 3 for the initial menu, this code fires to ensure that the user knows to select from the menu
    print("Please make a selection from the menu.")

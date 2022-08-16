#This program provides a GUI - if it could be called that - to convert temperatures.
a=int(input(("******************************\nTemperature Conversion Program\n******************************\n\nEnter 1 for: Celsius to Fahrenheit\nEnter 2 for: Fahrenheit to Celcius\nEnter 3 to Quit\n\nInput: ")))
if a==1:
    a1=float(input("\nInput the temperature in Celcius: "))
    if a1>=-273.15:
        a1=(a1*1.8)+32
        result="{:.2f}".format(a1)
        print("The temperature is",result,"degrees Fahrenheit. ")
    else:
        print("Temperatures cannot be below absolute zero. (-273.15°C, -459.67°F)")
elif a==2:
    a2=float(input("Input the temperature in Fahrenheit: "))
    if a2>=-459.67:
        a2=(a2-32)*0.5556
        result="{:.2f}".format(a2)
        print("The temperature is",result,"degrees Celcius.")
    else:
        print("Temperatures cannot be below absolute zero. (-273.15°C, -459.67°F)")
elif a==3:
    print("Exiting program. ")
    exit()
else:
    print("Please make a selection from the menu.")
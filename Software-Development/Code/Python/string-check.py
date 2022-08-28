# This program determines whether an input is an integer or not.
try: # This TRY sends the user to the EXCEPT in the event that the input is not an integer.
    a=int(input("Input a string: ")) # This code runs on the assumption that the input IS an integer, as it would not be able to run if it were not.
    print("The input is an integer.") # I found this to be an interesting way to do this - I dont know if it was the "intended" way, but I am quite the fan.
except ValueError: # If the TRY is not positively fulfilled, prints the error message.
    print("The input is not an integer.")
# I quite like this one.

#Start the program by listing options for the user:

#Celsius to Fahrenheit
#Fahrenheit to Celsius
#Exit
#Prompt user to insert choice. After the decision to convert, ask the amount of current temperature (use the floating point datatype). Lastly show the converted value to the user.

#For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

#Data representation examples:

#50.0 °F
#10.0 °C
#If the user chooses option Exit, notify the user: Exiting...

#Use 1 decimal precision to round the converted value.

#Example program runs

#run 1 run 2 run 3
#Program starting.
print("Program starting.\n")
#Options:
#1 - Celsius to Fahrenheit
#2 - Fahrenheit to Celsius
#0 - Exit
print("Options:")
print("#1 - Celcius to Fahrenheit")
print("#2 - Fahrenheit to Celcius")
print("#3 - Exit")
Choise = int(input("Your choise: "))
#Your choice: 1
#Insert the amount of Celsius: 23
#23.0 °C equals to 73.4 °F
#Program ending.
if(Choise == 1):
    Cels = float(input("Insert the amount of Celcius: "))
    Fahr = Cels * 1.8 + 32
    print(f"{round(Cels, 1)}°C equals to {round(Fahr, 1)}°F\n")
elif(Choise == 2):
    Fahr2 = float(input("Insert the amount of Fahrenheit: "))
    Cels2 = (Fahr2 - 32) / 1.8
    print(f"{round(Fahr2, 1)}°F equals to {round(Cels2, 1)}°C\n")
elif(Choise == 3):
    print("Exiting...\n")
print("Program ending.")

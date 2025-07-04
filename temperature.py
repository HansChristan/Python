unit = input("Enter the unit Celcius/Fahrenheit/Kelvin (C/F/K): ")
temperature = float(input("Enter the temperature: "))
if unit == 'C':
    temperature = round(temperature * 9/5 + 32)
    print(f"Temperature in Fahrenheit: {temperature} F")
elif unit == 'F':
    temperature = round((temperature - 32) * 5/9)
    print(f"Temperature in Celcius: {temperature} C")
elif unit == 'K':
    temperature = round(temperature - 273.15)
    print(f"Temperature in Celsius: {temperature} C")
else:
    temperature = "Invalid unit"

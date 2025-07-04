weight = float(input("Enter Your Weight: "))
unit = input("Enter the unit (kg/lb): ")

if unit == 'kg':
    weight = weight * 2.20462
    unit = 'lb'
elif unit == 'lb':
    weight = weight / 2.20462
    unit = 'kg'
else:
    weight = "Invalid unit"
    
print(f"your weight is: {weight} {unit}")
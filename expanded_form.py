# expanded_form.py
# Input a 3-digit number and print its expanded form
num = int(input("Enter 3-digit number (100-999): "))

if num < 100 or num > 999:
    print("Number out of range (100-999)")
else:
    hundreds = num // 100 * 100
    tens = num % 100 // 10 * 10
    units = num % 10
    
    parts = []
    if hundreds != 0:
        parts.append(str(hundreds))
    if tens != 0:
        parts.append(str(tens))
    if units != 0:
        parts.append(str(units))
    
    print(" + ".join(parts))

# round_number.py
# Input a number (1-100) and print it rounded to nearest 10
num = int(input("Enter number (1-100): "))

if num < 1 or num > 100:
    print("Number out of range (1-100)")
else:
    rounded = round(num / 10) * 10
    print(f"Rounded to nearest 10: {rounded}")

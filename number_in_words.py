# number_in_words.py
# Input a number (1-100) and print it in words
units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

num = int(input("Enter number (1-100): "))

if num < 1 or num > 100:
    print("Number out of range (1-100)")
elif num == 100:
    print("one hundred")
elif num >= 20:
    ten_part = tens[num // 10]
    unit_part = units[num % 10]
    if unit_part:
        print(f"{ten_part}-{unit_part}")
    else:
        print(ten_part)
elif num >= 10:
    print(teens[num - 10])
else:
    print(units[num])

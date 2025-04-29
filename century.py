

# Get year input from user
year = int(input("Enter a year: "))

# A century year ends with "00"
if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")
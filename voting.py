

# Get age input from user
age = int(input("Enter your age: "))

# Check if eligible to vote (age 18 or older)
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    years_left = 18 - age
    if years_left > 0:
        print(f"You can vote after {years_left} year(s).")
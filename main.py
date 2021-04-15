# Task 1 Sample Solution
# Given two sides of the right angled triangle
# Calculate the third side. Get twp sides from
# the user

ab = float(input("Please enter ac of triangle: "))
bc = float(input("Please enter bc of triangle: "))

ac = (ab**2 + bc**2) ** (1/2)
print("The third side of the triangle equals: " + str(ac))

# Part 2 of Task 1

ab = float(4)
bc = float(3)
height = ab
base = bc
area = (height * base) / 2
print(area)

# Task 2

myNumbers = [2,56,12,67,1000,32,89,29,44,39,200,11,21]
a = min(myNumbers)
b = max(myNumbers)
print("Minimum number of my list " + str(min(myNumbers)))
print("Maximum number of my list " + str(max(myNumbers)))

# Reminder to print on GitHub!

import math
#This part of the code is to get the user inputs needed to do the equation
print("Given a quadratic equation of the form a*x^2 + b * x + c")
a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

#This part of the code is to find the discriminant value to help us determine how many solutions
discriminant = b ** 2 - 4 * a * c

#This part of the equation is so we can decide by using the discriminant value if there is one, two, or no solutions
#Once we determine how many solutions we are also letting the user know how many solutions and what the solution is
if discriminant < 0:
    print("There are no real solutions")
elif discriminant == 0:
    onesolution = -b / (2 * a)
    print(f"There is one real solution: {onesolution:.2f}")
else:
    solution1 = (-b + math.sqrt(discriminant)) / (2 * a)
    solution2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("There are 2 real solutions")
    print(f"Solution 1: {solution1:.2f}")
    print(f"Solution 2: {solution2:.2f}")
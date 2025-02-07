# hcf and lcm program

import math

def calculate_hcf(x, y):
    return math.gcd(x, y)

def calculate_lcm(x, y):
    return (x * y) // calculate_hcf(x, y)

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = calculate_hcf(num1, num2) 
lcm = calculate_lcm(num1, num2)

print(f"The HCF of {num1} and {num2} is {hcf}")
print(f"The LCM of {num1} and {num2} is {lcm}")

# Output:
# Enter first number: 54
# Enter second number: 24
# The HCF of 54 and 24 is 6
# The LCM of 54 and 24 is 216

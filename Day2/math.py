# hcfLCM using math library

from math import gcd

def calculate_hcf_lcm(a, b):
    # Calculate HCF using gcd from the math module
    hcf = gcd(a, b)
    
    # Calculate LCM using the formula: LCM(a, b) = (a * b) / HCF(a, b)
    lcm = abs(a * b) // hcf  # abs() ensures LCM is positive
    
    return hcf, lcm

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Get HCF and LCM
hcf, lcm = calculate_hcf_lcm(num1, num2)

# Output the results
print(f"The HCF of {num1} and {num2} is: {hcf}")
print(f"The LCM of {num1} and {num2} is: {lcm}")

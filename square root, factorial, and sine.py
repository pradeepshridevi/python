import math

def math_operations(number):
    
    square_root = math.sqrt(number)
    
    # Changed condition: Check if number is non-negative for factorial calculation
    if number >= 0:  
        factorial = math.factorial(int(number))
    else:
        factorial = "Factorial is only defined for non-negative integers"

    sine_value = math.sin(number)
    
    print(f"Square root of {number}: {square_root}")
    print(f"Factorial of {number}: {factorial}")
    print(f"Sine of {number}: {sine_value}")
number = 5
math_operations(number)

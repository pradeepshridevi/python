def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
  
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operator!"

result = calculator(10, 5, "+")
print(result)  

result = calculator(10, 5, "/")
print(result)  

result = calculator(10, 0, "/")
print(result) 

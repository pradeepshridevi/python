from ast import operator
num1 =float(input("Enter first number:"))
num2 =float(input("Enter second number:"))
operator = input("Enter operator(+,-,*,/):")
if operator == '+':
  print("result:",num1+num2)
elif operator == '-':
  print("result:",num1-num2)
elif operator == '*':
  print("result:",num1*num2)
elif operator == '/':
  print("result:",num1/num2)

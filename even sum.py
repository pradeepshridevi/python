start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
even_sum = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        even_sum += num
print(f"The sum of even numbers between {start} and {end} is: {even_sum}")

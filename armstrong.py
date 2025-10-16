n = int(input("Enter a number: "))  # taking an input number

sum_cubes = sum(int(digit) ** 3 for digit in str(n)) # finding sum cubes

if n == sum_cubes:

print(f"The number {n} is an Armstrong number") # printing if n is armstrong

else:

print(f"The number {n} is not an Armstrong number") # printing if n is not armstrong


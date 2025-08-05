# Question One
# Write a function that checks if a number is a perfect number.
import math
x = int(input("Enter a number: ")) 
sum_of_factors = 0
for i in range(1,int(math.sqrt(x)) + 1):
    if x % i == 0:
        sum_of_factors += i
        sum_of_factors += (x // i)  # Add the corresponding factor
sum_of_factors -= x  # Remove the number itself from the sum
if sum_of_factors == x:
    print(f"{x} is a perfect number.")
else:
    print(f"{x} is not a perfect number.")

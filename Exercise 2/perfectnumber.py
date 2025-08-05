# Question One
# Write a function that checks if a number is a perfect number.
x = int(input("Enter a number: ")) 
sum_of_factors = 0
for i in range(1,x):
    if x % i == 0:
        sum_of_factors += i
if sum_of_factors == x:
    print(f"{x} is a perfect number.")
else:
    print(f"{x} is not a perfect number.")

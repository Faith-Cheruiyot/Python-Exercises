length = 400
width = 300
height = 250
area_one = 2 * (length * height)
area_two = 2 * (width * height)
area_three = length * width
total_area = area_one + area_two + area_three
#Assuming 25 litres of paint covers 100000 square centimeters
coverage_per_liter = 100000 / 25  # cm² per liter
paint_needed = total_area / coverage_per_liter
print("Paint needed:", round(paint_needed, 2), "liters")
# End of code
# This code calculates the amount of paint needed to cover the walls and ceiling of a room.
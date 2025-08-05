time = 86400  # seconds in a day
seconds = int(input("Enter time in seconds: "))
if seconds <= time:
    hours = (time - seconds) // 3600
    minutes = (time - seconds) % 3600 // 60
else:
    print("Please enter a value less than 86400 seconds")

if hours != 1:
    hr_str = "hours"
else:
    hr_str = "hour" 
if minutes != 1:
    min_str = "minutes"
else:
    min_str = "minute"
if seconds != 1:
    sec_str = "seconds"
else:
    sec_str = "second"
print(f"Time in the day is: {int(hours)} {hr_str}, {int(minutes)} {min_str}, {int(seconds)} {sec_str}")    
#Ebd of code
# This code converts a given time in seconds to hours, minutes, and seconds within a day.    1

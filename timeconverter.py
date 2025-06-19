time = 86400  # seconds in a day
seconds = int(input("Enter time in seconds: "))
if seconds <= time:
    minutes = (time - seconds) / 60
    hours = (time - seconds) % 60
    print("Time in the day is:", int(hours), "hours", int(minutes), "minutes", int(seconds), "seconds")
else:
    print("Please enter a value less than 86400 seconds")
#Ebd of code
# This code converts a given time in seconds to hours, minutes, and seconds within a day.    1

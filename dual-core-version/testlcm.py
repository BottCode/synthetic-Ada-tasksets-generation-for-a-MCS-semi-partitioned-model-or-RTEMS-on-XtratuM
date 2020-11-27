import utils

numbers = [190, 130, 90, 40, 120, 110, 130]

i = 0
multiplier = 100
while i < len(numbers):
    numbers[i] = numbers[i] * multiplier
    i += 1

print("lcm: ", numbers)

microseconds = utils.compute_hyperperiod (numbers)
seconds = microseconds / 1000000
minutes = seconds / 60
hours = minutes / 60

print ("microseconds => ", microseconds, ", seconds => ", seconds, ", minutes => ", minutes, ", hours => ", hours)

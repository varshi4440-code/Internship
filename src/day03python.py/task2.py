temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

# Print first and last readings
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])

# Extract Afternoon Peak readings (4th, 5th, 6th items)
afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)

# Extract Last 3 Hours readings
last_3_hours = temperatures[-3:]
print("Last 3 Hours Readings:", last_3_hours)

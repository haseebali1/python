import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    # creates a reader object
    reader = csv.reader(f)
    # next returns the next line in the file
    header_row = next(reader)

    # high temps are in column 5
    highs = [int(row[5]) for row in reader]

# plot the high temperatures.
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(highs, c = 'red')

#format plot
plt.title("Daily high temperatures, july 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

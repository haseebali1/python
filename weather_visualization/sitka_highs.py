import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    # creates a reader object
    reader = csv.reader(f)
    # next returns the next line in the file
    header_row = next(reader)

    highs, dates = [], []
    # high temps are in column 5 and date is in column 2
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        highs.append(int(row[5]))

# plot the high temperatures.
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red')

#format plot
plt.title("Daily high temperatures, july 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

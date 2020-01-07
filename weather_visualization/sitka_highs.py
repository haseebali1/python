import csv

filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    # creates a reader object
    reader = csv.reader(f)
    # next returns the next line in the file
    header_row = next(reader)

    # high temps are in column 5
    highs = [int(row[5]) for row in reader]

print(highs)

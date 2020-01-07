from die import Die

#create a six-sided die
die = Die()

# make some reolls and store results in a list
results = []

for roll_num in range(100):
    results.append(die.roll())

#analyzing the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequencies.append(results.count(value))
print(results)

print(frequencies)

from die import Die

#create a six-sided die
die = Die()

# make some reolls and store results in a list
results = []

for roll_num in range(100):
    results.append(die.roll())

print(results)

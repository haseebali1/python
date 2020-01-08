import json

# explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Get all the features from the dictionary
# which stores the information about each earthquake
all_eq_data = all_eq_data['features']

#magnitudes
mags = []

for eq_data in all_eq_data:
    mags.append(eq_data['properties']['mag'])

print(mags)

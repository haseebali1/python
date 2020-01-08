import json

# explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Get all the features from the dictionary
# which stores the information about each earthquake
all_eq_data = all_eq_data['features']

#magnitudes
mags, lons, lats = [], [], []

# usually it is written lattitude and longtitude,but in this json format
# longtitude is written first and then latitude
for eq_data in all_eq_data:
    mags.append(eq_data['properties']['mag'])
    lons.append(eq_data['geometry']['coordinates'][0])
    lats.append(eq_data['geometry']['coordinates'][1])

print(mags)
print(lons[:10])
print(lats[:10])

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# explore the structure of the data
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Get all the features from the dictionary
# which stores the information about each earthquake
file_title = all_eq_data['metadata']['title']
all_eq_data = all_eq_data['features']

#magnitudes
mags, lons, lats, hover_texts = [], [], [], []

# usually it is written lattitude and longtitude,but in this json format
# longtitude is written first and then latitude
for eq_data in all_eq_data:
    mags.append(eq_data['properties']['mag'])
    lons.append(eq_data['geometry']['coordinates'][0])
    lats.append(eq_data['geometry']['coordinates'][1])
    hover_texts.append(eq_data['properties']['title'])

#Map the earthquakes
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'colorscale' : 'Viridis',
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'}
        }
    }]
my_layout = Layout(title=file_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

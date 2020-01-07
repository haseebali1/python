from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create a six-sided die
die1 = Die()
die2 = Die()

# make some reolls and store results in a list
results = [ die1.roll() + die2.roll() for value in range(1000)]

#for roll_num in range(1000):
#    results.append(die1.roll() + die2.roll())

#analyzing the results
max_result = die1.num_sides + die2.num_sides
frequencies = [results.count(value) for value in range(2,max_result+1)]
#for value in range(2, max_result + 1):
#    frequencies.append(results.count(value))

print(frequencies)

# Visualize the results
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values,y=frequencies)]

# dtick label every bar
x_axis_config = {'title' : 'Result', 'dtick' : 1}
y_axis_config = {'title' : 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data' : data, 'layout':my_layout}, filename='d6_d6.html')

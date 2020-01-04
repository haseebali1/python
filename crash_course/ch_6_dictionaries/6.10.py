# Favorite Numbers

favorite_numbers = {
        'John': [ 7, 234, 65646 ],
        'Adam': [ 453, 344, 344 ],
        'Sam' : [ 980, 566, 234, 32 ],
        'Bill': [ 767, 324, 12, 9879],
        'Tom' : [ 234, 2347, 45794 ],
        'Will' : [ 324 ]
        }

for name in favorite_numbers:
    output = name + " : "
    for number in favorite_numbers[name]:
        output += str(number) + ", "
    print(output.rstrip().rstrip(','))

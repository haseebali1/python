# Rivers

longest_rivers = {
        'nile' : 'africa',
        'amazon' : 'south america',
        'yangtze' : 'asia',
        'mississippi/missouri' : 'north America',
        'yenisei/angara/selenga' : 'Europe'
        }

for river in longest_rivers:
    print (f"The {river.title()} River is located in \
{longest_rivers[river].title()}")

print("\nRivers:")

for river in longest_rivers:
    print(river.title())

print("\nCountries:")

for country in longest_rivers.values():
    print(country.title())

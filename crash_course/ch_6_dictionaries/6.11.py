# Cities

cities = {
        'los angeles' : {
            'state' : 'california',
            'population' : 3_792_621
            },
        'las vegas' : {
            'state' : 'nevada',
            'population' : 583_756
            },
        'new york city' : {
            'state' : 'new york',
            'population' : 8_175_133
            }
        }

# WORKS
#for city,city_info in cities.items():
#    print ( f"{city.title()} : " )
#    print ( f"\t{city_info['state'].title()}")
#    print ( f"\t{city_info['population']}")

# WORKS
#for city,city_info in cities.items():
#    print ( f"{city.title()} : " )
#    for info in city_info:
#        print ("\t" + info.title() + " : " + str(city_info[info]).title())

for city in cities:
    print ( f"{city.title()}" )
    for info in cities[city]:
        print ( "\t" + info.title() + " : " + str(cities[city][info]).title())

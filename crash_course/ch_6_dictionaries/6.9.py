#favorite places

favorite_places = {
        'jack' : [ "London", "New York" ],
        'rachel' : [ "Singapore" , "Vietnam", "Germany" ],
        'ross' : [ "France" ],
        'eddie' : [ "Brazil", "Argentina", "Peru", "Mexico" ]
        }

for name in favorite_places:
    print (f"{name.title()} : ")
    count = 1
    for place in favorite_places[name]:
        print ( "\t" + str(count) + " : " + place)
        count += 1
    print()

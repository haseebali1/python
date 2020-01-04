def get_formatted_city_name(city, country, population =''):
    """ Generate a neatly formatted City name"""

    if population:
        formatted_city_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_city_name = f"{city.title()}, {country.title()}"

    return formatted_city_name

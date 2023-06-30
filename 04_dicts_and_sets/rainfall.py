def get_rainfall():
    """
    The user inputs a city name and how much rain fell in that city.
    When the user exits, give the total rainfall for each city entered.
    """
    print("Enter a city name and rainfall amount. Press 'enter' to quit.\n")
    rainfall = {}
    
    while True:
        city_name = input("City name: ")
        if not city_name:
            break
        
        rain_amt = int(input("Amount of rainfall: "))
        if not rain_amt:
            break
        
        # get the value if it exists, or set it to zero, then add the new value
        rainfall[city_name] = rainfall.get(city_name, 0) + rain_amt
    
    message = '\nRainfall recorded:\n'
    for city, rain in rainfall.items():
        message += f"{city}: {rain} mm\n"
    
    return message

print(get_rainfall())

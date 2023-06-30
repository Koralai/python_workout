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
        
        if city_name in rainfall:
            rainfall[city_name] += rain_amt
        else:
            rainfall[city_name] = rain_amt
    
    return rainfall

print(get_rainfall())

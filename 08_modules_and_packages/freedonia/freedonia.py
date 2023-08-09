def calculate_tax(price, province, hour):
    """
    Calculate the tax for a purchase in 'Freedonia' based on the price of the
    item, the province in which the purchase was made, and the hour the 
    purchase occurred (an integer from 0 to 24).
    """
    
    tax_per_province = {
        'chico': 0.5,
        'groucho': 0.7,
        'harpo': 0.5,
        'zeppo': 0.4,
    }
    
    if hour == 0:
        tax_per_hour = 1
    else:
        tax_per_hour = hour / 24
    
    tax = price * (tax_per_province[province.lower()]) * tax_per_hour
    
    return round(tax, 2)

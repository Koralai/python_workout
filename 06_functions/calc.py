import operator

def prefix_calc(prefix_notation):
    """
    Parse a string using mathematical prefix notation and two numbers.
    (Example: "+ 2 3" would return "5.")
    """
    
    string_items = prefix_notation.split()    
    given_operator = string_items[0]
    num_1 = int(string_items[1])
    num_2 = int(string_items[2])
    
    calculate = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
    }
    
    return calculate[given_operator](num_1, num_2)

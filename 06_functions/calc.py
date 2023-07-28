import operator

def prefix_calc(prefix_notation):
    """
    Parse a string using mathematical prefix notation and two numbers.
    (Example: "+ 2 3" would return "5.")
    """
    
    string_items = prefix_notation.split(' ')    
    given_operator = string_items[0]
    num_1 = int(string_items[1])
    num_2 = int(string_items[2])
    
    operators = {
        '+': operator.add(num_1, num_2),
        '-': operator.sub(num_1, num_2),
        '*': operator.mul(num_1, num_2),
        '/': operator.truediv(num_1, num_2),
        '%': operator.mod(num_1, num_2),
        '**': operator.pow(num_1, num_2)
    }
    
    return operators[given_operator]

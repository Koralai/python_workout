from decimal import *

def add_decimals():
    """
    Take 2 strings from the user, turn them into decimals, and return the sum
    """
    num_1 = input("Decimal number one: ")
    num_2 = input("Decimal number two: ")
    new_sum = Decimal(num_1) + Decimal(num_2)
    return float(new_sum)
    
def main():
    print("Write two decimal numbers, and I'll add them together.\n")    
    print(add_decimals())
    
if __name__ == '__main__':
    main()
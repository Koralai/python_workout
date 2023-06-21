from decimal import *

def add_decimals():
    """
    Take 2 strings from the user, turn them into decimals, and return the sum
    """
    new_sum = Decimal(0)
    number_counter = 1

    while True:            
        new_number = input(f"Decimal number {number_counter}: ")
        
        if not new_number:
            break
        
        new_sum += Decimal(new_number)
        number_counter += 1

    return float(new_sum)
    
def main():
    print("Enter some decimal numbers, and I'll add them together.\n")    
    print(add_decimals())
    
if __name__ == '__main__':
    main()
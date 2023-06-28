def get_any_sum(*args):
    """Return the sum of the arguments, of any quantity and type"""
    
    output = args[0] # Get an initial value that is type-agnostic
    
    for arg in args[1:]:
        output += arg
    
    return output

def main():
    print(get_any_sum('abc','def'))
    print(get_any_sum(1,3,5))
    print(get_any_sum([123],[456],[789]))

if __name__ == '__main__':
    main()

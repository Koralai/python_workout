def get_any_sum(*args):
    """Return the sum of the arguments, of any quantity and type"""
    
    if not args:        
        return args
    
    output = args[0]    # Set an initial value that is type-agnostic    
    for arg in args[1:]:
        output += arg    
    return output


def main():
    print(get_any_sum('abc','def'))
    print(get_any_sum(1,3,5))
    print(get_any_sum([123],[456],[789]))
    print(get_any_sum())
    print(get_any_sum('just one string'))

if __name__ == '__main__':
    main()

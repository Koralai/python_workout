def get_numeric_sum(*args):
    """
    Return the sum of all args that are integers
    or can be converted to integers
    """
    
    if not args:
        return args
    
    output = 0
    for arg in args:
        try:
            output += int(arg)
        except ValueError:
            continue
    return output


def main():
    print(get_numeric_sum('5', 'grape', 10, '25'))

if __name__ == '__main__':
    main()

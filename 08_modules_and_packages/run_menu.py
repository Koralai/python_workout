from menu import menu

def func_a():
    return 'First option'

def func_b():
    return 'Second option'

return_value = menu(a=func_a, b=func_b)
print(f'Result: {return_value}')

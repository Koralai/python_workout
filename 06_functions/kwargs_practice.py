def list_rankings(**kwargs):
    output = ''
    for key, value in kwargs.items():
        output += f'{key}: {value}\n'
    
    return output

print(list_rankings(gold='nadine', silver='henry', bronze='louisa'))

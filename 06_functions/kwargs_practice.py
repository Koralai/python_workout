def list_rankings(**rankings):
    output = ''
    for rank, name in rankings.items():
        output += f'{rank}: {name}\n'
    
    return output

print(list_rankings(gold='nadine', silver='henry', bronze='louisa'))

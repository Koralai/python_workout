import tax_data as td

def get_tax_bracket(current_income):
    """Assign an income to the correct tax bracket."""
    
    if current_income >= td.INCOME_BRACKETS[td.HIGHEST_BRACKET]:
        return td.HIGHEST_BRACKET   

    for bracket, income in td.INCOME_BRACKETS.items():
        if current_income <= income:
            return bracket


def calculate_income_tax(income):
    """A basic model to estimate income tax based on U.S. tax brackets."""
    
    bracket = get_tax_bracket(income)
    min_tax = td.MINIMUM_TAX[bracket]
    marg_rate = td.MARGINAL_RATE[bracket]
    
    if bracket == 1:
        return income * marg_rate
    
    prev_bracket = td.INCOME_BRACKETS[bracket - 1]
    
    return min_tax + ((income - prev_bracket) * marg_rate)

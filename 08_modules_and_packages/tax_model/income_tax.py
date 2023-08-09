INCOME_BRACKETS = {
    1: 11000,
    2: 44725,
    3: 95375,
    4: 182100,
    5: 231250,
    6: 578125,
    7: 578126,
}

HIGHEST_BRACKET = 7

MINIMUM_TAX = {
    1: 0,
    2: 1100,
    3: 5147,
    4: 16290,
    5: 37104,
    6: 52832,
    7: 174238,
}

MARGINAL_RATE = {
    1: 0.1,
    2: 0.012,
    3: 0.22,
    4: 0.24,
    5: 0.32,
    6: 0.35,
    7: 0.37,
}

def get_tax_bracket(income):
    """Assign an income to the correct tax bracket."""
    
    if income >= INCOME_BRACKETS[HIGHEST_BRACKET]:
        return HIGHEST_BRACKET   

    for bracket, amt in INCOME_BRACKETS.items():
        if income <= amt:
            return bracket


def calculate_income_tax(income):
    """A basic model to estimate income tax based on U.S. tax brackets."""
    
    bracket = get_tax_bracket(income)
    prev_bracket = INCOME_BRACKETS[bracket - 1]
    min_tax = MINIMUM_TAX[bracket]
    marg_rate = MARGINAL_RATE[bracket]
    
    if bracket == 1:
        return income * marg_rate
    
    return min_tax + ((income - prev_bracket) * marg_rate)

print(calculate_income_tax(400000))

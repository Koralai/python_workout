BRACKETS = {
    1: 11000,
    2: 44725,
    3: 95375,
    4: 182100,
    5: 231250,
    6: 578125,
    7: 578126,
}

HIGHEST_BRACKET = 7

MIN_PER_BRACKET = {
    1: 0,
    2: 1100,
    3: 5147,
    4: 16290,
    5: 37104,
    6: 52832,
    7: 174238,
}

MARGINAL_RATE_PER_BRACKET = {
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
    
    if income >= BRACKETS[HIGHEST_BRACKET]:
        return HIGHEST_BRACKET   
    else:
        for bracket, amt in BRACKETS.items():
            if income <= amt:
                return bracket


def calculate_income_tax(income):
    """A basic model to estimate income tax based on U.S. tax brackets."""
    
    RATES = {
        BRACKETS[1]: 0.1,
        BRACKETS[2]: MIN_PER_BRACKET[2] + ((income - BRACKETS[1]) * 0.012),
        BRACKETS[3]: MIN_PER_BRACKET[3] + ((income - BRACKETS[2]) * 0.22),
        BRACKETS[4]: MIN_PER_BRACKET[4] + ((income - BRACKETS[3]) * 0.24),
        BRACKETS[5]: MIN_PER_BRACKET[5] + ((income - BRACKETS[4]) * 0.32),
        BRACKETS[6]: MIN_PER_BRACKET[6] + ((income - BRACKETS[5]) * 0.35),
        BRACKETS[7]: MIN_PER_BRACKET[7] + ((income - BRACKETS[6]) * 0.37)
    }
    
    pass

print(get_tax_bracket(1150000))

from tax import calculate_income_tax

def test_tax_lowest_bracket():
    """Can we calculate the tax for an income in the lowest bracket?"""
    income = 9000
    assert calculate_income_tax(income) == 900

def test_tax_mid_bracket():
    """Can we calculate the tax for an income in a middle bracket?"""
    income = 83000
    assert calculate_income_tax(income) == 13567.5

def test_tax_highest_bracket():
    """Can we calculate the tax for an income in the highest bracket?"""
    income = 650000
    assert calculate_income_tax(income) == 200832

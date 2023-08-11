from tax import calculate_income_tax

def main():
    income_1 = 55000
    income_1_tax = calculate_income_tax(income_1)
    print(f"${income_1_tax:,.2f}")

if __name__ == '__main__':
    main()

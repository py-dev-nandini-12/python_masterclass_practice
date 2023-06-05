total_income = 10_000
gross_income = float(input('Please enter your gross income : '))
if gross_income < total_income:
    print(gross_income)

if 10_000 <gross_income <30_000:
    after_tax = round(gross_income - 0.20*gross_income)
    print(f"The after tax income is {after_tax} ")
elif 30_000 < gross_income < 50_000:
    after_tax = round(gross_income - 0.35*gross_income)
    print (f"The after tax income is {after_tax}")
elif gross_income > 50_000:
        after_tax = round(gross_income - 0.50*gross_income)
        print(f"The after tax income is {after_tax}")
    



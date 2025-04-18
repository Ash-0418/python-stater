monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01


#get_yearly_revenue
def get_yearly_revenue(monthly_revenue):
  yearly_revenue = monthly_revenue * 12
  return yearly_revenue


#get_yearly_expenses
def get_yearly_expenses(monthly_expenses):
  yearly_expenses = monthly_expenses * 12
  return yearly_expenses


#get_tax_amount
def get_tax_amount(profit):
  if (profit <= 0 and profit <= 1000000):
    tax_amount = profit * 0.15
    return tax_amount
  elif (profit > 1000000):
    tax_amount = profit * 0.25
    return tax_amount


#apply_tax_credits
def apply_tax_credits(tax_amount, tax_credits):
  discount = tax_amount * tax_credits
  return discount


yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")

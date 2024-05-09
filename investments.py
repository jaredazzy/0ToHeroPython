#This part of the code is creating the function where we can check for validity of the inputs the user gives us
def valid(prompt, data_type=float, min_value=0):
    while True:
        try:
            value = data_type(input(prompt))
            if value >= min_value:
                return value
        except ValueError:
            pass
#This part of the code is to check for the validity of the age
def valid_age(prompt, current_age=0):
    return valid(prompt, int, current_age)

#This part of the code to calculate the monthly interest
def calculate_monthly_interest(annual_rate):
    return annual_rate / 12


#This part of the code is the function for the algorithm to choose which financial strategy to choose from
def strategy(loan, loan_rate, min_payment, monthly_budget, invest_rate, current_age, retirement_age):
    months = (retirement_age - current_age) * 12
    monthly_loan_interest = calculate_monthly_interest(loan_rate)
    monthly_invest_interest = calculate_monthly_interest(invest_rate)

    # This code is for the minimum payments on loan and invest the rest
    min_loan_balance = loan
    max_investments = 0
    for _ in range(months):
        if min_loan_balance > 0:
            min_loan_balance *= (1 + monthly_loan_interest)
        max_investments *= (1 + monthly_invest_interest)
        payment = min(min_loan_balance, min_payment)
        min_loan_balance -= payment
        excess_money = monthly_budget - payment
        max_investments += excess_money
#This part of the code is the function for the algorithm to choose which financial strategy to choose from
def strategy(loan, loan_rate, min_payment, monthly_budget, invest_rate, current_age, retirement_age):
    months = (retirement_age - current_age) * 12
    monthly_loan_interest = calculate_monthly_interest(loan_rate)
    monthly_invest_interest = calculate_monthly_interest(invest_rate)

    # This code is for the minimum payments on loan and invest the rest
    min_loan_balance = loan
    max_investments = 0
    for _ in range(months):
        if min_loan_balance > 0:
            min_loan_balance *= (1 + monthly_loan_interest)
        max_investments *= (1 + monthly_invest_interest)
        payment = min(min_loan_balance, min_payment)
        min_loan_balance -= payment
        excess_money = monthly_budget - payment
        max_investments += excess_money
    max_investments -= max(0, min_loan_balance)

    #This part of the code the strategy of if they decide to just pay the loan off fully
    full_loan_balance = loan
    min_investments = 0
    for _ in range(months):
        if full_loan_balance > 0:
            full_loan_balance *= (1 + monthly_loan_interest)
            pay
    max_investments -= max(0, min_loan_balance)

    #This part of the code the strategy of if they decide to just pay the loan off fully
    full_loan_balance = loan
    min_investments = 0
    for _ in range(months):
        if full_loan_balance > 0:
            full_loan_balance *= (1 + monthly_loan_interest)
            payment = min(full_loan_balance, monthly_budget)
            full_loan_balance -= payment
            if full_loan_balance == 0:
                excess_money = monthly_budget - payment
                min_investments += excess_money
        else:
            min_investments *= (1 + monthly_invest_interest)
            min_investments += monthly_budget

    return max_investments, min_investments

#This part of the code is so we can just efficiently ask the user for all the inputs.
loan = valid("Enter how much money you owe in loans: ")
loan_rate = valid("Enter the annual interest rate of the loans: ")
min_payment = valid("Enter your minimum monthly loan payment: ")
monthly_budget = valid("Enter how much money you will be putting towards loans/retirement each month: ",
                                min_value=min_payment)
current_age = valid("Enter your current age: ", int)
retirement_age = valid_age("Enter the age you plan to retire at: ", current_age)
invest_rate = valid("Enter your predicted annual rate of return: ")

min_payments_savings, full_payments_savings = strategy(loan, loan_rate, min_payment,
                                                                        monthly_budget, invest_rate, current_age,
                                                                        retirement_age)
#This part of the code is the result of either to pay the minimum loan and invest or fully pay off first.
if min_payments_savings >= full_payments_savings:
    print("You should only make minimum payments on your loans and invest the rest")
    print(
        f"If you do you will have ${min_payments_savings:.2f} as opposed to ${full_payments_savings:.2f} when you retire.")
else:
    print("You should pay of all of your loans before you start investing")
    print(
        f"If you do you will have ${full_payments_savings:.2f} as opposed to ${min_payments_savings:.2f} when you retire.")
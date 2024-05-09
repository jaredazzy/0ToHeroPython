#This part of code is so we can get all the necessary inputs for the calculations
principal = float(input("Please enter the amount of money you borrowed: "))
annual_rate = float(input("$Please enter the annual interest rate: "))
num_payments = int(input("Please enter the number of payments to be made: "))

#This part of the code is so that the annual interest rate is turned into monthly rate
monthly_rate = annual_rate / 12

#This part of the code is the formula so we can calculate the monthly payment
monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** - num_payments)

#This part of the code is for the total cost
total_loan = (monthly_payment * num_payments)
total_interest = total_loan - principal

#This part of the code is to let the user know how much the monthly payments are , and total cost of loan
print(f"A loan of ${principal:.2f} with an annual interest of {annual_rate} paid off over {num_payments} months will have monthly payments of ${monthly_payment:.2f}.")
print(f"In total, you will pay ${total_loan:.2f}, making the cost of your loan ${total_interest:.2f}.")

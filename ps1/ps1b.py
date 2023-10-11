# Part B: Saving, with a raise Background
# ​Please make your
# In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate, and clearly you are going to be worth more to your company over time! So we are going to build on your solution to Part A by factoring in a raise every six months.
# In ​ps1b.py​, copy your solution to Part A (as we are going to reuse much of that machinery). Modify your program to include the following
# 1. Have the user input a semi-annual salary raise ​semi_annual_raise​ (as a decimal percentage) 2. After the 6t​h​ month, increase your salary by that percentage. Do the same after the 12t​h
# month, the 18​th​ month, and so on.
# Write a program to calculate how many months it will take you save up enough money for a down payment. LIke before, assume that your investments earn a return of ​r​ = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semi­annual salary raise (semi_annual_raise)
# Hints
# To help you get started, here is a rough outline of the stages you should probably follow in writing your code:
# ● Retrieve user input.
# ● Initialize some state variables. You should decide what information you need. Be sure to be
# careful about values that represent annual amounts and those that represent monthly amounts.
# ● Be careful about when you increase your salary – this should only happen ​after​ the 6t​h,​ 12t​h​, 18t​h
# month, and so on.

portion_down_payment = .25
current_savings = 0
annual_salary = float(input('Enter your annual salary: '))
monthly_salary = annual_salary/12
portion_saved = float(input('Enter the percent of your salary to save as a decimal: '))
investment_return_rate = .04/12
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
num_months = 0

#While the current savings is less than the down payment amount run the loop
while current_savings <= total_cost * portion_down_payment:
    current_savings*=(1+investment_return_rate)
    current_savings+=(monthly_salary*portion_saved)
    num_months+=1
    #if the num_months modulu 6 = 0 then add the raise
    if(num_months % 6 == 0):
        monthly_salary *= (1 + semi_annual_raise)

print('Number of months: ', num_months)




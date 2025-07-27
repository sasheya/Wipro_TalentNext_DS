# Project 1

distance = float(input("How far would you like to travel in miles? "))
if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")

# Project 2

cost_per_hour = 0.51
hours_per_day = 24
cost_per_day = cost_per_hour * hours_per_day
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

budget = 9187
days_with_budget = budget / cost_per_day

print(f"Cost per day: ${cost_per_day:.2f}")
print(f"Cost per week: ${cost_per_week:.2f}")
print(f"Cost per month: ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate for {int(days_with_budget)} days.")

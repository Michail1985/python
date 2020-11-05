from sys import argv

work_hour, wage_rate, bonus = argv
work_hour = float(work_hour)
wage_rate = float(wage_rate)
bonus = float(bonus)
wages = work_hour * wage_rate + bonus
print(wages)
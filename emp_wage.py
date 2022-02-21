import random

IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

emp_check = random.randint(0, 2)
if emp_check == IS_PRESENT_FULL_DAY:
    print(f"Employee is present for full time and the wage is ₹{WAGE_PER_HOUR * FULL_DAY_HOURS}")
elif emp_check == IS_PRESENT_PART_TIME:
    print(f"Employee is present for part time and wage is ₹{WAGE_PER_HOUR * PART_TIME_HOURS}")
else:
    print("Employee is absent")
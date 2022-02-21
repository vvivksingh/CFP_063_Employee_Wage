import random

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4

emp_attandence = {
    IS_PRESENT_FULL_DAY :
    f"Employee is present for full time and the wage is {WAGE_PER_HOUR * FULL_DAY_HOURS}",
    IS_PRESENT_PART_TIME:
    f"Employee is present for part time and wage is {WAGE_PER_HOUR * PART_TIME_HOURS}",
    IS_ABSENT:
    f"Employee is absent"
    }

emp_check = random.randint(0, 2)

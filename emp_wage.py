import random

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4


def calculate_employee_wage(wage_per_hour, num_of_working_days, working_hour_per_month, company):
    emp_attendence = {
        IS_PRESENT_FULL_DAY: FULL_DAY_HOURS,
        IS_PRESENT_PART_TIME: PART_TIME_HOURS,
        IS_ABSENT: 0
    }

    working_days = 0
    total_working_hours = 0

    while (working_days < num_of_working_days and total_working_hours < working_hour_per_month):
        emp_check = random.randint(0, 2)
        total_working_hours = total_working_hours + emp_attendence.get(emp_check)
        working_days = working_days + 1

    total_wage = total_working_hours * wage_per_hour
    print(f"Employee total wage for Company {company} is {total_wage}")

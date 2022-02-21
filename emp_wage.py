import random

IS_ABSENT = 0
IS_PRESENT_FULL_DAY = 1
IS_PRESENT_PART_TIME = 2
WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4
TOTAL_WORKING_DAYS = 20
TOTAL_WORKING_HOURS = 100


def calculateEmployeeWage():
    emp_attandence = {
        IS_PRESENT_FULL_DAY: FULL_DAY_HOURS,
        IS_PRESENT_PART_TIME: PART_TIME_HOURS,
        IS_ABSENT: 0
    }

    workingDays = 0
    totalWorkingHours = 0

    while (workingDays < TOTAL_WORKING_DAYS and totalWorkingHours < TOTAL_WORKING_HOURS):
        emp_check = random.randint(0, 2)
        totalWorkingHours = totalWorkingHours + emp_attandence.get(emp_check)
        workingDays = workingDays + 1

    return totalWorkingHours * WAGE_PER_HOUR


totalWage = calculateEmployeeWage()


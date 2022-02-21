import emp_wage

if __name__ == '__main__':
    print("Welcome to Employee Wage Builder")
    emp_dmart = emp_wage.EmployeeWageBuilder(20, 20, 100, "Dmart")
    emp_jio = emp_wage.EmployeeWageBuilder(30, 25, 110, "Jio")
    emp_dmart.calculate_employee_wage()
    emp_jio.calculate_employee_wage()



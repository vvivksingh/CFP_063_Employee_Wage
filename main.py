import emp_wage

if __name__ == "__main__":
    print("Welcome to Employee Wage Builder")
    emp_wage = emp_wage.EmployeeWageBuilder()
    emp_wage.add_employee(20, 20, 100, "Dmart")
    emp_wage.add_employee(30, 25, 110, "Jio")
    emp_wage.calculate_employee_wage()
    employees = "\n".join(str(employee) for employee in emp_wage.company_array)
    print(employees)
<<<<<<< HEAD
=======

>>>>>>> uc11_wage_using_lambda


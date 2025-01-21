# Write a function that takes a list of employee salaries
# and calculates the average salary.

salaries_li = input("Enter Salaries Separated by comma:\n").split(",")
salaries_li = [int(salary) for salary in salaries_li]
def calc_avg_employee_salary(salaries:list):
    total_salary, avg_salary = 0, 0
    for salary in salaries:
        total_salary += salary
    avg_salary = total_salary/(len(salaries))
    return avg_salary

print(f"Average Salary is: {calc_avg_employee_salary(salaries_li)}")
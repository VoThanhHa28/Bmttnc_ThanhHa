work_hours = float(input('Enter employee work hours: '))
salary_grade = float(input('Enter salary per standard hour: '))
standard_hour = 44
hour_over_grade = max(0, work_hours - standard_hour)
real_salary = standard_hour * salary_grade + hour_over_grade * salary_grade * 1.5
print(f"Real employee's salary: {real_salary}")

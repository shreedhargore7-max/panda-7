import pandas as pd

data = {
    "Name": ['Ram', 'Shay', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simram'],
    "Age": [28, 34, 30, 29, 40, 25, 32, 27],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary']>50000]
print('Employees with salary > 50000')
print(high_salary)


#filtering row  salary > 50k & age>30

filtered_rows = df[(df['Salary']>50000) & (df['Age']>30)]


print("\nEmployees with salary > 50000 and age > 30")

print(filtered_rows)

#using ORcondition
filtered_rows = df[(df['Salary']>50000) | (df['Age']>30)]
print("\nEmployees with salary > 50000 or age > 30")
print(filtered_rows)
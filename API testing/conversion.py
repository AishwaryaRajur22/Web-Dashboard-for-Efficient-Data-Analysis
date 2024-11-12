import pandas as pd
data = {
    'Emp ID': [101, 102, 103],
    'Emp Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'Engineering', 'Marketing']
}
df = pd.DataFrame(data)
df.to_excel('employee_data.xlsx', index=False)
print("Data successfully written to employee_data.xlsx")
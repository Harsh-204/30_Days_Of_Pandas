1import pandas as pd
2
3def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
4    if N <= 0:
5        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
6
7    employee = employee.drop_duplicates(subset='salary')
8    employee = employee.sort_values(by='salary', ascending=False)
9
10    if len(employee) < N:
11        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
12
13    salary = employee['salary'].iloc[N - 1]
14
15    return pd.DataFrame({f'getNthHighestSalary({N})': [salary]})
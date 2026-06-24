1import pandas as pd
2
3def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
4    unique_salaries = employee["salary"].drop_duplicates()
5    max_salary = unique_salaries.max()
6    second_max = unique_salaries[unique_salaries < max_salary].max()
7    return pd.DataFrame({"SecondHighestSalary": [second_max if pd.notna(second_max) else None]})
8
9data = [[1, 100], [2, 200], [3, 300]]
10employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})
11print(second_highest_salary(employee))
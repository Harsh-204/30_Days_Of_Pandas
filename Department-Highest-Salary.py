1import pandas as pd
2
3def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
4    employee = employee[
5        employee["salary"] == employee.groupby("departmentId")["salary"].transform("max")
6    ]
7
8    result = employee.merge(
9        department,
10        left_on="departmentId",
11        right_on="id"
12    )
13
14    return result.rename(
15        columns={
16            "name_x": "Employee",
17            "name_y": "Department",
18            "salary": "Salary"
19        }
20    )[["Department", "Employee", "Salary"]]
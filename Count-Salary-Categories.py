1import pandas as pd
2
3def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
4    return pd.DataFrame({
5        "category": ["Low Salary", "Average Salary", "High Salary"],
6        "accounts_count": [
7            (accounts["income"] < 20000).sum(),
8            ((accounts["income"] >= 20000) & (accounts["income"] <= 50000)).sum(),
9            (accounts["income"] > 50000).sum()
10        ]
11    })
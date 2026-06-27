1import pandas as pd
2def fix_names(users: pd.DataFrame) -> pd.DataFrame:
3    users['name'] = users['name'].str.capitalize()
4    users = users.sort_values(by = 'user_id', ascending = True)
5    return users
6
7
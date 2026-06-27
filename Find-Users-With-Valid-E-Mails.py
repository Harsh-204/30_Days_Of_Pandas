1import pandas as pd
2
3def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
4    pattern = r'^[a-zA-Z][a-zA-Z0-9_\.-]*@leetcode\.com$'
5    valid_emails_df = users[users['mail'].str.contains(pattern, na=False)]
6    return valid_emails_df
7
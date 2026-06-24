1import pandas as pd
2def delete_duplicate_emails(person: pd.DataFrame) -> None:
3    person.sort_values('id', inplace=True)
4    person.drop_duplicates(subset=['email'], keep='first', inplace=True)
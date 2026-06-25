1import pandas as pd
2
3def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
4    customer = orders["customer_number"].value_counts().idxmax()
5    return pd.DataFrame({"customer_number": [customer]})
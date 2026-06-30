1import pandas as pd
2
3def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
4    df = activity.groupby("player_id")["event_date"].min().reset_index()
5    df = df.drop_duplicates(subset=['player_id'], keep='first', inplace=False)
6    df = df[["player_id", "event_date"]]
7    df.rename(columns={"event_date": "first_login"}, inplace=True)
8    return df
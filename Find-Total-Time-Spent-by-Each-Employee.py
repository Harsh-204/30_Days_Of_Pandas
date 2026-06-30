1import pandas as pd
2
3def total_time(employees: pd.DataFrame) -> pd.DataFrame:
4    Total_time = employees.groupby(['emp_id','event_day'])[['in_time','out_time']].sum().reset_index()
5    Total_time['total_time'] = Total_time['out_time']-Total_time['in_time']
6    Total_time = Total_time[['emp_id', 'event_day', 'total_time']]
7    Total_time.rename(columns = {'event_day': 'day'},inplace = True)
8    return Total_time
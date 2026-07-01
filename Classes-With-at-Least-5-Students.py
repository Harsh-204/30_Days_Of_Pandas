1import pandas as pd
2
3def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
4    grp_courses = courses.groupby('class').filter(lambda x: x['class'].count() >= 5)
5    df = grp_courses.drop_duplicates(subset = 'class')
6    return df.drop(columns = ['student'])
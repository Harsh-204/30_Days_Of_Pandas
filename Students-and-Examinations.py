1import pandas as pd
2
3def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
4    # Create all student-subject combinations
5    result = students.merge(subjects, how="cross")
6
7    # Count exams attended by each student for each subject
8    counts = (
9        examinations
10        .groupby(["student_id", "subject_name"])
11        .size()
12        .reset_index(name="attended_exams")
13    )
14
15    # Merge counts with all combinations
16    result = result.merge(
17        counts,
18        on=["student_id", "subject_name"],
19        how="left"
20    )
21
22    # Replace NaN with 0
23    result["attended_exams"] = result["attended_exams"].fillna(0).astype(int)
24
25    # Sort as required
26    return result.sort_values(
27        by=["student_id", "subject_name"]
28    ).reset_index(drop=True)
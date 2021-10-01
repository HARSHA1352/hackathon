import pandas as pd
from pandas_profiling import ProfileReport
df= pd.read_csv('Rainfall_Jan_to_Mar_2021.csv')
print(df)
profile=ProfileReport(df)
profile.to_file(output_file="Rainfall_Jan_to_Mar_2021.html")
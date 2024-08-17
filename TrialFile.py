import pandas as pd
import datetime as dt

df=pd.read_csv("BookList.csv")
print(df['ID'])

#How to print date
print(dt.date.day)
delta=dt.timedelta(days=7)
print(dt.date.today()+delta)
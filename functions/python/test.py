import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('name_list.xlsx', sheet_name='Sheet1')


room = df['Room']
staff_id = df['ID']
name = df['Name']
state = df['State']

print(room[0])

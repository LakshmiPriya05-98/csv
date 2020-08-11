import pandas as pd
import pyodbc
df = pd.read_csv(r'C:\Users\Lavanya Priya\Desktop\delimit\eg1_data.csv')
connection = pyodbc.connect('Driver={SQL Server};Server=.\\sqlexpress;Database=cd;uid=sa;pwd=sqlexpress')
cursor = connection.cursor()
cursor.execute('CREATE TABLE details (id int, fname nvarchar(50), lname nvarchar(50), salary int)')
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO cd.dbo.details (id, fname, lname,salary)
                VALUES (?,?,?,?)
                ''',
                   row.id,
                   row.fname,
                   row.lname,
                   row.salary
                   )
connection.commit()
print('con success')

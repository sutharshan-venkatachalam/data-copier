#1.populating departmentsdata into table

import pandas as pd
import os

conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
dept = pd.read_sql('SELECT * FROM departments', conn)
print('1.dept:', dept)

BASE_DIR = 'C:\\Users\\sutharshan.v\\Research\\data\\retail_db_json\\'
table_name = 'departments\\'
file_name = os.listdir(f'{BASE_DIR}{table_name}')[0]
print('2.filename :', file_name)

# #get full file path
fp = f'{BASE_DIR}{table_name}{file_name}'
table_path = 'departments'
print('fp:', fp)
df = pd.read_json(fp, lines=True)
print('3.dataframe:',df)
df.to_sql(table_path, conn, if_exists='append', index=False)
view_table = pd.read_sql('SELECT count(1) FROM departments',conn)
print("end----", view_table)


# 2. validate department table
# import pandas as pd
# query = 'SELECT * FROM departments'
# conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
# df = pd.read_sql(query,conn)
# df
# df.count()
# view_table = pd.read_sql('SELECT count(1) FROM departments',conn)
# print(view_table)

#3.Populating orders table
# BASE_DIR = 'C:\\Users\\sutharshan.v\\Research\\data\\retail_db_json\\'
# table_path = 'orders\\'
# table_name = 'orders'
#
# import os
# file_name = os.listdir(f'{BASE_DIR}{table_path}')[0]
# fp = f'{BASE_DIR}{table_path}{file_name}'
#
# import pandas as pd
# json_reader = pd.read_json(fp, lines=True, chunksize=1000)
#
# conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
#
# for df in json_reader:
#     min_key = df['order_id'].min()
#     max_key = df['order_id'].max()
#     df.to_sql(table_name, conn, if_exists='append', index=False)
#     print(f'Processed {table_name} with in the range of {min_key} and {max_key}')

#4.Validate orders table in database

#5.Validate orders table using Pandas

import pandas as pd
query = 'SELECT * FROM orders'
conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
df = pd.read_sql(
    query,
    conn
)
print(df.count())

print(df.dtypes)

cnt = pd.read_sql(
    'SELECT order_status, count(1) AS order_count FROM orders GROUP BY order_status',
    conn
)
print("count:",cnt)


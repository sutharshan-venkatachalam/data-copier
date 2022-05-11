# import pandas as pd

import os
# def main():
#     print("i'm in main app.py")
#     print(os.environ)
#     DB_NAME = os.environ.get('DB_NAME_VALUE')
#     print('DB_NAME:',DB_NAME)
#
#
# if __name__ == '__main__':
#     main()



# to_sql & data_frame
#
# users_list = [
#     {'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
#     {'user_first_name': 'Donald', 'user_last_name': 'Duck'}
# ]
#
# df = pd.DataFrame(users_list)
#
# conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
# df.to_sql('users', conn, if_exists='append', index=False)
#
# result = pd.read_sql('SELECT * FROM users', conn)
# print("result:",result)





#read_sql
# def pandas_practice():
#     print('welcome pandas')
#     query = 'SELECT * FROM users'
#     conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
#     df = pd.read_sql(query, conn)
#
#     print(df)
#
#     df.count()
#
# pandas_practice()

# def main():
#     print('welcome to python')
#     # The file name is hardcoded and assigned to fp.
#     fp = 'C:\\Users\\sutharshan.v\\Research\\data\\retail_db_json\\order_items\\' \
#          'part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'
#     df = pd.read_json(fp, lines=True, chunksize = 1000)
#     print(type(df))
#     # print(df.count())
#     json_reader = df
#     # print(df.describe())
#     # print(df.columns)
#     # print(df.dtypes)
#     # print(df[['order_item_order_id', 'order_item_subtotal']])
#     # print(df[df['order_item_order_id'] == 2])
#     for idx, df in enumerate(json_reader):
#         print(f'Number of records in chunk with index {idx} is {df.shape},{df.shape[0]}')


# if __name__== "__main__":
#     main()


# Integrate read and write logic
import os
from read import get_json_reader
from write import load_db_table


def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])


def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    print(type(BASE_DIR))
    # table_name = os.environ.get('TABLE_NAME')
    table_name = "products"

    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    process_table(BASE_DIR, conn, table_name)


if __name__ == '__main__':
    main()


#adding all the tables
# import sys
# import os
# from read import get_json_reader
# from write import load_db_table
#
#
# def process_table(BASE_DIR, conn, table_name):
#     json_reader = get_json_reader(BASE_DIR, table_name)
#     for df in json_reader:
#         load_db_table(df, conn, table_name, df.columns[0])
#
#
# def main():
#     configs = dict(os.environ.items())
#     conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
#     BASE_DIR = os.environ.get('BASE_DIR')
#     table_names = sys.argv[1].split(',')
#     print("table_names:",table_names)
#     for table in table_names:
#         process_table(BASE_DIR, conn, table)
#     print("all df entered successfully")
#
#
# if __name__ == '__main__':
#     main()
import logging

import psycopg2

logging.basicConfig(level=logging.DEBUG)

connection = psycopg2.connect(
    host='localhost',
    database='Test',
    user='postgres',
    password='root',
    port='5432'
)

table_select_query = '''
        select * from Customer
'''

pointer = connection.cursor()
try:
    pointer.execute(table_select_query)
    # rows = pointer.fetchall()
    # rows = pointer.fetchone()
    rows = pointer.fetchmany(4)
    file = open('data.txt', 'w')
    # print(rows)
    file.write('Usernames'+'\n')
    for row in rows:
        file.writelines(row[1]+'\n')
    #     print(row[1], '-------LOAN--------', row[-1])

finally:
    logging.info("Data retrieved")

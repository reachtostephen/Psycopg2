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

delete_sql_query = '''
        delete from Customer where id = 3
'''

pointer = connection.cursor()
try:
    pointer.execute(delete_sql_query)
    connection.commit()
    logging.info('Deletion is done')
except Exception as e:
    logging.error("Deletion couldn't be made ", e)
finally:
    pointer.close()
    connection.close()

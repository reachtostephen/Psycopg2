import logging

import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='Test',
    user='postgres',
    password='root',
    port='5432'
)

update_sql_query = '''
        update Customer set age = 35 where id = 3
'''

pointer = connection.cursor()
try:
    pointer.execute(update_sql_query)
    connection.commit()
    logging.info("Data updated")
except Exception as e:
    logging.error("Update couldn't be made ", e)
finally:
    connection.close()

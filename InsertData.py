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

insert_sql_query = '''
        insert into Customer(ID, name, age, address, LOAN_AMOUNT) 
        values(3,'GHI',30,'BAN',300000)
'''

pointer = connection.cursor()
try:
    pointer.execute(insert_sql_query)
    connection.commit()
    logging.info('Insertion is done')
except Exception as e:
    logging.error("Insertion couldn't be made ", e)
finally:
    pointer.close()
    connection.close()

import numpy as np
import pandas as pd
import datetime
import requests
import psycopg2

url = 'http://ballings.co/data.py'
#The following line will create an object called data
exec(requests.get(url).content)
#The data will be stored in an object called data. 
data.to_csv(path_or_buf = 'C:/Temp/bzan545newdata.csv', index = False)
pd.concat([pd.read_table('C:/Temp/bzan545masterdata.csv', delimiter = ','), data]).to_csv(path_or_buf = 'C:/Temp/bzan545masterdata.csv', index = False)

database = {'user': 'postgres',
            'pass': 'bzan545saxon',
            'name': 'postgres',
            'host': 'localhost',
            'port': '5432'}

pgConnectString = f"""host={database['host']}
                      port={database['port']}
                      dbname={database['name']}
                      user={database['user']}
                      password={database['pass']}"""

pgConnection = psycopg2.connect(pgConnectString)

query = "TRUNCATE TABLE bzan545masterdata; COPY bzan545masterdata FROM 'C:\\Temp\\bzan545masterdata.csv' WITH (format csv, header true, delimiter ',');"

pgConnection.autocommit = True
cursor = pgConnection.cursor()
cursor.execute(query)
pgConnection.commit()
pgConnection.close()
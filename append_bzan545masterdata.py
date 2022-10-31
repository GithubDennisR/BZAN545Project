import numpy as np
import pandas as pd
import datetime
import requests

url = 'http://ballings.co/data.py'
#The following line will create an object called data
exec(requests.get(url).content)
#The data will be stored in an object called data. 
data.to_csv(path_or_buf = 'C:/Temp/bzan545newdata.csv', index = False)
pd.concat([pd.read_table('C:/Temp/bzan545masterdata.csv', delimiter = ','), data]).to_csv(path_or_buf = 'C:/Temp/bzan545masterdata.csv', index = False)
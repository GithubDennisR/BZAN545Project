import numpy as np
import pandas as pd
import datetime
import requests

url = 'http://ballings.co/data.py'
#The following line will create an object called data
exec(requests.get(url).content)
#The data will be stored in an object called data.

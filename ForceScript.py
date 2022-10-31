import random
import datetime 
import numpy as np
import pandas as pd
import os
today = datetime.date(2022,9,30)
random.seed(int(today.strftime('%j')))
nbrrecords = random.randrange(22, 300)
yesterday = today - datetime.timedelta(days=1)
salesdate = np.array([yesterday.strftime('%m/%d/%Y') for i in range(nbrrecords)])
productid = np.array([random.randrange(22, 300) for i in range(nbrrecords)])
region = np.array([random.choice(['a', 'b', 'c', 'd', 'e']) for i in range(nbrrecords)])
freeship = np.array([random.randrange(0, 2) for i in range(nbrrecords)])
discount = np.array([round(random.uniform(0.01,10),3) for i in range(nbrrecords)])
itemssold = np.array([random.randrange(1,222) for i in range(nbrrecords)]) 
data = pd.DataFrame({'salesdate':salesdate,'productid':productid,'region':region,'freeship':freeship,'discount':discount,'itemssold':itemssold})
path = 'C:\\Users\\denni\\OneDrive\\Desktop\\545 Project\\'
tablerecords = data.to_csv(os.path.join(path,'DATA1.csv'),mode = 'a', header = True)

x = list(np.linspace(1,31,31))
x = [int(i) for i in x]

for x in x:
    today = datetime.date(2022,10,x)
    random.seed(int(today.strftime('%j')))
    nbrrecords = random.randrange(22, 300)
    yesterday = today - datetime.timedelta(days=1)
    salesdate = np.array([yesterday.strftime('%m/%d/%Y') for i in range(nbrrecords)])
    productid = np.array([random.randrange(22, 300) for i in range(nbrrecords)])
    region = np.array([random.choice(['a', 'b', 'c', 'd', 'e']) for i in range(nbrrecords)])
    freeship = np.array([random.randrange(0, 2) for i in range(nbrrecords)])
    discount = np.array([round(random.uniform(0.01,10),3) for i in range(nbrrecords)])
    itemssold = np.array([random.randrange(1,222) for i in range(nbrrecords)]) 
    data = pd.DataFrame({'salesdate':salesdate,'productid':productid,'region':region,'freeship':freeship,'discount':discount,'itemssold':itemssold})
    path = 'C:\\Users\\denni\\OneDrive\\Desktop\\545 Project\\'
    tablerecords = data.to_csv(os.path.join(path,'DATA1.csv'),mode = 'a', header = False)
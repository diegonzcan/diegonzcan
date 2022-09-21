#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv

file = 'Drivers-Report(Sep-20-2022)'

hfile = open(r"C:\\Users\diego\\Documents\\TWEN\Netradyne Source Data\\" + file + '.csv')
rfile = open(r"C:\\Users\diego\\Documents\\TWEN\Netradyne Source Data\\"+ file + '.csv')

hcsvreader = csv.reader(hfile)
rcsvreader = csv.reader(rfile)

header = []
for line in range(11):
    header = next(hcsvreader)

rows = []
for row in rcsvreader:
    rows.append(row)

Date = rows[3]
Date = Date[2]
Date = Date.split()
Date = Date[0]

rows1 = []
for row in hcsvreader:
    rows1.append(row)
    
data = rows[11:]

header = np.array(header)
df = pd.DataFrame(data)
df.columns = header
df['Date'] = Date
df['Minutes Analyzed'] = df['Minutes Analyzed'].astype(int)
df = df.loc[df['Minutes Analyzed'] > 0]
df = df.drop(columns=(['Driver ID','Green Minutes%','Over Speeding%']))
final_cols = ['Driver Name', 'Date', 'Minutes Analyzed', 'Driver Score', 'Driver Star',
       'High G', 'Low Impact', 'Driver Initiated', 'Potential Collision',
       'Sign Violations', 'Traffic Light Violation', 'U Turn',
       'Hard Braking', 'Hard Turn', 'Hard Acceleration',
       'Driver Distraction', 'Following Distance', 'Speeding Violations',
       'Seatbelt Compliance', 'Camera Obstruction', 'Weaving',
       'Requested Video', 'Total Events']
df = df[final_cols]
df.to_csv(r'C:\Users\diego\Documents\TWEN\Netradyne Source Data\c_netradyne.csv')


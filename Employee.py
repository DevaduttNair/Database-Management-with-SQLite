# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:55:07 2022

@author: Devadutt Nair
"""

import sqlite3

X= sqlite3.connect('EMPLOYEES.db')

X.execute(''' CREATE TABLE IF NOT EXISTS EMPLOYEE
          (ID INT NOT NULL, 
           Name TEXT, 
           Age INT,
           Date_Join TEXT,
           Place TEXT,
           Salary INT)''')
          
Y = X.cursor()

Y.execute('''INSERT INTO EMPLOYEE VALUES (1,'John',25,'01.01.2020','Kerala',25000),
          (2,'Adam',33,'01.02.2020','Tamil Nadu',30000),
          (3,'Mary',42,'01.03.2020','Karnataka',120000),
          (4,'Jacob',42,'01.04.2020','Karnataka',140000),
          (5,'Aaron',42,'01.05.2020','Kerala',100000)''' )
          
for row in Y.execute('SELECT * FROM EMPLOYEE ORDER BY Date_Join'):
    print(row)

X.commit()

Y.close() 

import sqlite3

X= sqlite3.connect('EMPLOYEES.db')

Y = X.cursor()


Y.execute("SELECT * FROM EMPLOYEE WHERE NAME = 'John' ")

print(Y.fetchall())

X.commit()

Y.close()

import sqlite3

X= sqlite3.connect('EMPLOYEES.db')

Y = X.cursor()

data = Y.execute("SELECT * from EMPLOYEE");

for k in data:
    print ("ID = ", k[0])
    print ("Name = ", k[1])
    print ("Date_Join = ", k[2])
    print ("Place = ", k[3])
    print ("Salary = ", k[4])
    print ("Age = ", k[5])
    
X.commit()

Y.close()

    
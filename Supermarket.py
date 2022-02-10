# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:41:57 2022

@author: Devadutt Nair
"""
import sqlite3

X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

Y.execute("SELECT * FROM Supermarket_sales")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[16]))
  
print("Maximum of Unit price is = ",max(new_list))  

print("Minimum of Unit price is = ",min(new_list))  

print("Average of Unit price is = ",sum(new_list)/len(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()


 
Y.execute("SELECT * FROM Supermarket_sales")

new_list=[]



for k in Y.fetchall():
  new_list.append(int(k[7]))
  



print("Maximum of Quantity is = ",max(new_list))  

print("Minimum of Quantity is = ",min(new_list))  

print("Average of Quantity is = ",sum(new_list)/len(new_list))  



X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Productline = 'Health and beauty'")

new_list=[]

for k in Y.fetchall():
  new_list.append(int(k[7]))
  

print("Maximum of Quantity in Health and Beauty is = ",max(new_list))  

print("Minimum of Quantity in Health and Beauty = ",min(new_list))  

print("Average of Quantity in Health and Beauty = ",sum(new_list)/len(new_list))  

X.commit()

Y.close()

import sqlite3

X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

Y.execute("SELECT * FROM Supermarket_sales WHERE Productline = 'Electronic accessories'")

new_list=[]

for k in Y.fetchall():
  new_list.append(int(k[7]))
  
print("Maximum Quantity of Electronic accessories is = ",max(new_list))  

print("Minimum Quantity of Electronic accessories = ",min(new_list))  

print("Average Quantity of Electronic accessories = ",sum(new_list)/len(new_list))  



X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()
 
Y.execute("SELECT * FROM Supermarket_sales WHERE Gender = 'Male' AND Productline = 'Health and beauty'")

new_list=[]

for k in Y.fetchall():
  new_list.append(int(k[7]))
  

print("Men with Health and beauty is = ",len(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()


 
Y.execute("SELECT * FROM Supermarket_sales")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[7]))

Y.execute("SELECT * FROM Supermarket_sales")

new_list1=[]

for k in Y.fetchall():
  new_list1.append(int(k[8]))


X.commit()

Y.close()

import matplotlib.pyplot as plt
plt.scatter(new_list,new_list1)

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Productline = 'Health and beauty'")

new_list=[]

for k in Y.fetchall():
  new_list.append(int(k[16]))
  

print("Maximum of Unit price in Health and Beauty is = ",max(new_list))  

print("Minimum of Unit price in Health and Beauty = ",min(new_list))  

print("Average of Unit price in Health and Beauty = ",sum(new_list)/len(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Gender = 'Male' AND Productline = 'Health and beauty'")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[7]))
  

print("Men with Health and beauty is = ",len(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Gender = 'Female' AND Productline = 'Fashion accessories'")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[7]))
  

print("Women with Fashion Accessories is = ",len(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Gender = 'Female' AND Productline = 'Fashion accessories' OR Productline = 'Sports and travel'")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[7]))
  

print("Women with Fashion Accessories & Sports and travel is = ",len(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales")

tax_value=[]

for k in Y.fetchall():
  tax_value.append(int(k[8]))
  
Y.execute("SELECT * FROM Supermarket_sales")
  
quantity=[]

for k in Y.fetchall():
  quantity.append(int(k[7]))
  
import matplotlib.pyplot as plt

plt.scatter(quantity,tax_value)

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Gender = 'Male'")

tax_value=[]

for k in Y.fetchall():
  tax_value.append(int(k[8]))
  
Y.execute("SELECT * FROM Supermarket_sales WHERE Gender = 'Male'")
  
quantity=[]

for k in Y.fetchall():
  quantity.append(int(k[7]))
  
import matplotlib.pyplot as plt

plt.scatter(quantity,tax_value)

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE City = 'Yangon'")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[8]))
  

print("Tax collected from Yangon = ",sum(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE City = 'Yangon' OR City = 'Mandalay'")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[7]))
  

print("Total Sales from Yangon & Mandalay = ",sum(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE City = 'Yangon'")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[7]))
  

print("Sales from Yangon = ",sum(new_list))  

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE City = 'Mandalay'")

new_list=[]


for k in Y.fetchall():
  new_list.append(int(k[7]))
  

print("Sales from Mandalay = ",sum(new_list))  

X.commit()

Y.close()

print("Yangan has more sales than Mandalay - 1859 > 1820")

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales")

tax_value=[]

for k in Y.fetchall():
  tax_value.append(int(k[8]))
  
Y.execute("SELECT * FROM Supermarket_sales")
  
unit_price=[]

for k in Y.fetchall():
    unit_price.append(int(k[16]))
  
import matplotlib.pyplot as plt

plt.scatter(unit_price,tax_value)

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Gender = 'Male'")

new_list=[]


for k in Y.fetchall():
  new_list.append(float(k[14]))
  

print("Highest Gross income of Male = ",max(new_list))

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Gender = 'Female'")

new_list=[]


for k in Y.fetchall():
  new_list.append(float(k[14]))
  

print("Highest Gross income of Female = ",max(new_list))

X.commit()

Y.close()

print("Males have higher gross income than females 49.49 > 49.65")


import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Customertype = 'Normal'")

new_list=[]


for k in Y.fetchall():
  new_list.append(float(k[14]))
  

print("Highest Gross income of Normal customer = ",max(new_list))

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Customertype = 'Member'")

new_list1=[]


for k in Y.fetchall():
  new_list1.append(float(k[14]))
  

print("Highest Gross income of Special customer = ",max(new_list1))

X.commit()

Y.close()

print("Normal customers have higher gross margin")


import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE gross_iincome = '0.5085'")

new_list1=[]


for k in Y.fetchall():
  new_list1.append((k[1]))
  

print("Lowest Gross income Invoice ID = ",(new_list1))

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE gross_iincome = '9.989'")

new_list1=[]


for k in Y.fetchall():
  new_list1.append((k[1]))
  

print("Highest Gross income Invoice ID = ",(new_list1))

X.commit()

Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Payment = 'Cash'")

new_list1=[]


for k in Y.fetchall():
  new_list1.append(float(k[14]))
  

print("Gross Margin against Cash = ",max(new_list1))

X.commit()
Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Payment = 'Credit card'")

new_list1=[]


for k in Y.fetchall():
  new_list1.append(float(k[14]))
  

print("Gross Margin against Credit card = ",max(new_list1))

X.commit()
Y.close()

import sqlite3

  
X = sqlite3.connect('SalesDBNew.db')
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales WHERE Payment = 'Ewallet'")

new_list1=[]


for k in Y.fetchall():
  new_list1.append(float(k[14]))
  

print("Gross Margin against Cash = ",max(new_list1))

X.commit()
Y.close()

print(" Credit card payment has the highest gross margin margin while Cash payment has the lowest gross margin")



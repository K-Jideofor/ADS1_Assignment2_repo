# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:58:53 2022

@author: kjide
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define functions to read and transpose file
def readfile(doc):
    filedata = pd.read_excel(doc, skiprows = 3)
    return filedata, filedata.transpose()

Climate_Change = readfile('climate change.xls')
print(Climate_Change)

# URBAN POPULATION IS THE INDICATOR OF INTEREST
"""
Use iloc to extract columns of interest, reset_index to reset index of DataFrame,
set_axis to assign desired index to given axis
"""
UrbanPop = Climate_Change[1].iloc[4:,[989, 2205, 2661, 3041, 13225, 9197]]
#print(UrbanPop)
UrbanPop = UrbanPop.reset_index()
#print(UrbanPop)
UrbanPop = UrbanPop.set_axis(["Year", "Australia", "Brazil", "Canada", 
                              "China", "Nigeria", "Kenya"], axis=1)
print(UrbanPop)

# Use iloc to extract rows of interest
UrbanPop = UrbanPop.iloc[[0,10,20,30,40,50,60], :]
#print(UrbanPop)

# BAR PLOT
# Drop Columns Australia, Canada, Kenya
bar_data = UrbanPop.drop(["Australia", "Canada", "Kenya"], axis=1)  
print(bar_data)

# Define Bar Plot Functions
def bar_chart(country1, country2, country3):
    plt.subplots(figsize=(10, 6))
    width = wt
    ct1 = np.arange(len(country1))
    ct2 = [x + width for x in ct1]
    ct3 = [x + width for x in ct2]
    plt.bar(ct1, country1, color='blue', width=wt, label=lab1)
    plt.bar(ct2, country2, color='red', width=wt, label=lab2)
    plt.bar(ct3, country3, color='green', width=wt, label=lab3)
    plt.xticks([s + width for s in range(len(country1))], ["1960", "1970", "1980", "1990", 
                                                           "2000", "2010", "2020"])
    plt.legend()
    return

wt = 0.2
country1 = bar_data["Brazil"]
country2 = bar_data["China"]
country3 = bar_data["Nigeria"]
lab1 = "Brazil"
lab2 = "China"
lab3 = "Nigeria"
bar_chart(country1, country2, country3)
plt.xlabel("Year")
plt.ylabel("Urban Population")
plt.title("Bar Plot Showing The Urban Population in 3 Countries (1960-2020)")
plt.show()


# METHANE EMISSIONS (% change from 1990) IS THE INDICATOR OF INTEREST
"""
Use iloc to extract columns of interest, reset_index to reset index of DataFrame,
set_axis to assign desired index to given axis, dropna to remove rows that have NaN values
"""
Methane_Emissions = Climate_Change[1].iloc[4:,[1018, 2234, 2690, 3070, 13254, 9226]]
#print(Methane_Emissions)
Methane_Emissions = Methane_Emissions.reset_index()
#print(Methane_Emissions)
Methane_Emissions = Methane_Emissions.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                                "China", "Nigeria", "Kenya"], axis=1)
Methane_Emissions = Methane_Emissions = Methane_Emissions.dropna(axis=0)
print(Methane_Emissions)

# Use iloc to extract rows of interest
Methane_Emissions = Methane_Emissions.iloc[-13:]

# BAR PLOT
bar_data = Methane_Emissions.drop(["Kenya"], axis=1)  # Drop Column Kenya
print(bar_data)

# Define Bar Plot Functions
def bar_chart(country1, country2, country3, country4, country5):
    plt.subplots(figsize=(10, 6))
    width = wt
    ct1 = np.arange(len(country1))
    ct2 = [x + width for x in ct1]
    ct3 = [x + width for x in ct2]
    ct4 = [x + width for x in ct3]
    ct5 = [x + width for x in ct4]
    plt.bar(ct1, country1, color='blue', width=wt, label=lab1)
    plt.bar(ct2, country2, color='black', width=wt, label=lab2)
    plt.bar(ct3, country3, color='orange', width=wt, label=lab3)
    plt.bar(ct4, country4, color='red', width=wt, label=lab4)
    plt.bar(ct5, country5, color='green', width=wt, label=lab5)
    plt.xticks([s + width for s in range(len(country1))], ["2000", "2001", "2002", "2003", 
                                                           "2004", "2005", "2006", "2007", 
                                                           "2008", "2009", "2010", "2011", "2012"])
    plt.legend()
    return

wt = 0.15
country1 = bar_data["Australia"]
country2 = bar_data["Brazil"]
country3 = bar_data["Canada"]
country4 = bar_data["China"]
country5 = bar_data["Nigeria"]
lab1 = "Australia"
lab2 = "Brazil"
lab3 = "Canada"
lab4 = "China"
lab5 = "Nigeria"
bar_chart(country1, country2, country3, country4, country5)
plt.xlabel("Year")
plt.ylabel("Methane Emissions(% change from 1990)")
plt.title("Bar Plot Showing The Methane Emissions in 5 Countries (2000-2012)")
plt.show()


# CO2 EMISSION (kt) IS THE INDICATOR OF INTEREST
"""
Use iloc to extract columns of interest, reset_index to reset index of DataFrame,
set_axis to assign desired index to given axis, dropna to remove rows that have NaN values
"""
CO2_Emissions = Climate_Change[1].iloc[4:,[1032, 2248, 2704, 3084, 13268, 9240]]
#print(CO2_Emissions)
CO2_Emissions = CO2_Emissions.reset_index()
#print(CO2_Emissions)
CO2_Emissions = CO2_Emissions.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                        "China", "Nigeria", "Kenya"], axis=1)
CO2_Emissions = CO2_Emissions = CO2_Emissions.dropna(axis=0)
print(CO2_Emissions)

# Use iloc to extract rows of interest
CO2_Emissions = CO2_Emissions.iloc[[0,5,10,15,20,25], :]
#print(CO2_Emissions)

# BAR PLOT
bar_data = CO2_Emissions.drop(["China"], axis=1)  # Drop Column China
print(bar_data)

# Define Bar Plot Functions
def bar_chart(country1, country2, country3, country4, country5):
    plt.subplots(figsize=(10, 6))
    width = wt
    ct1 = np.arange(len(country1))
    ct2 = [x + width for x in ct1]
    ct3 = [x + width for x in ct2]
    ct4 = [x + width for x in ct3]
    ct5 = [x + width for x in ct4]
    plt.bar(ct1, country1, color='blue', width=wt, label=lab1)
    plt.bar(ct2, country2, color='black', width=wt, label=lab2)
    plt.bar(ct3, country3, color='orange', width=wt, label=lab3)
    plt.bar(ct4, country4, color='red', width=wt, label=lab4)
    plt.bar(ct5, country5, color='green', width=wt, label=lab5)
    plt.xticks([s + width for s in range(len(country1))], ["1990", "1995", "2000", 
                                                           "2005", "2010", "2015"])
    plt.legend()
    return

wt = 0.15
country1 = bar_data["Australia"]
country2 = bar_data["Brazil"]
country3 = bar_data["Canada"]
country4 = bar_data["Kenya"]
country5 = bar_data["Nigeria"]
lab1 = "Australia"
lab2 = "Brazil"
lab3 = "Canada"
lab4 = "Kenya"
lab5 = "Nigeria"
bar_chart(country1, country2, country3, country4, country5)
plt.xlabel("Year")
plt.ylabel("CO2 Emissions(kt)")
plt.title("Bar Plot Showing The CO2 Emissions in 5 Countries (1990-2015)")
plt.show()


# ELECTRIC POWER CONSUMPTION (kWh per capita) IS THE INDICATOR OF INTEREST
"""
Use iloc to extract columns of interest, reset_index to reset index of DataFrame,
set_axis to assign desired index to given axis, dropna to remove rows that have NaN values
"""
Elect_Power_Cons = Climate_Change[1].iloc[4:,[1038, 2254, 2710, 3090, 13274, 9246]]
#print(Elect_Power_Cons)
Elect_Power_Cons = Elect_Power_Cons.reset_index()
#print(Elect_Power_Cons)
Elect_Power_Cons = Elect_Power_Cons.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                              "China", "Nigeria", "Kenya"], axis=1)
Elect_Power_Cons = Elect_Power_Cons = Elect_Power_Cons.dropna(axis=0)
print(Elect_Power_Cons)

# Use iloc to extract rows of interest
Elect_Power_Cons = Elect_Power_Cons.iloc[[0,5,10,15,20,25,30,35,40], :]
#print(Elect_Power_Cons)

# Line Plot
# Define Line Plot Functions
def line_plot(x_axis, y_data):
    plt.figure(figsize=(10,5))
    for i in range(len(y_data)):
        plt.plot(x_axis,y_data[i],label=label[i],linestyle='dashed')
    plt.legend()
    plt.xticks(x_axis,xticks)
    plt.title(title,fontsize=8)
    return

x_axis = Elect_Power_Cons["Year"].index
y_data = [Elect_Power_Cons["Australia"],Elect_Power_Cons["Brazil"],Elect_Power_Cons["Canada"],
          Elect_Power_Cons["China"],Elect_Power_Cons["Nigeria"]]
xticks = ["1971","1976","1981","1986","1991","1996","2001","2006","2011"]
label = ["Australia","Brazil","Canada","China","Nigeria"]
title = 'Line Plot Showing The Electric Power Consumption in 5 Selected Countries (1971-2011)'

line_plot(x_axis, y_data)

plt.xlabel("Year")
plt.ylabel("Elect_Power_Cons(kWh per capita)")
plt.show()


# AGRICULTURAL LAND (% of land area) IS THE INDICATOR OF INTEREST
"""
Use iloc to extract columns of interest, reset_index to reset index of DataFrame,
set_axis to assign desired index to given axis, dropna to remove rows that have NaN values
"""
Agric_Land = Climate_Change[1].iloc[4:,[1062, 2278, 2734, 3114, 13298, 9270]]
#print(Agric_Land)
Agric_Land = Agric_Land.reset_index()
#print(Agric_Land)
Agric_Land = Agric_Land.set_axis(["Year", "Australia", "Brazil", "Canada", 
                                  "China", "Nigeria", "Kenya"], axis=1)
Agric_Land = Agric_Land = Agric_Land.dropna(axis=0)
print(Agric_Land)

# Use iloc to extract rows of interest
Agric_Land = Agric_Land.iloc[[9,14,19,24,29,34,39,44,49,54,59], :]
#print(Agric_Land)

# Line Plot
# Define Line Plot Functions
def line_plot(x_axis, y_data):
    plt.figure(figsize=(10,5))
    for i in range(len(y_data)):
        plt.plot(x_axis,y_data[i],label=label[i],linestyle='dashed')
    plt.legend()
    plt.xticks(x_axis,xticks)
    plt.title(title,fontsize=8)
    return

x_axis = Agric_Land["Year"].index
y_data = [Agric_Land["Australia"],Agric_Land["Brazil"],Agric_Land["Canada"],
          Agric_Land["China"],Agric_Land["Nigeria"]]
xticks = ["1970","1975","1980","1985","1990","1995","2000","2005","2010","2015","2020"]
label = ["Australia","Brazil","Canada","China","Nigeria"]
title = 'Line Plot Showing The Agricultural land (% of land area) in 5 Selected Countries (1970-2020)'

line_plot(x_axis, y_data)

plt.xlabel("Year")
plt.ylabel("Agric_Land(% of land area)")
plt.show()

# CORRELATION FOR CANADA
Canada = pd.DataFrame({'Elect_Power_Cons': Elect_Power_Cons["Canada"], 
                       'Agric_Land': Agric_Land["Canada"], 
                       'CO2_Emissions': CO2_Emissions["Canada"]})

print(Canada)

# Fillna fills columns that have NaN values
Canada = Canada.fillna(0)
# Compute correlation of columns, removing NaN values
print(Canada.corr())

# HEAT MAP FOR CANADA
plt.imshow(Canada.corr(), cmap='Reds', interpolation='none')
plt.colorbar()
plt.xticks(range(len(Canada.columns)), Canada.columns, rotation=45)
plt.yticks(range(len(Canada.columns)), Canada.columns)

labels = Canada.corr().values
for y in range(labels.shape[0]):
    for x in range(labels.shape[1]):
        plt.text(x, y, '{:.2f}'.format(labels[y,x]), ha='center', va='center')
plt.title('Correlation Heatmap for Canada')
plt.show()


# CORRELATION FOR NIGERIA
Nigeria = pd.DataFrame({'Elect_Power_Cons': Elect_Power_Cons["Nigeria"], 
                        'Agric_Land': Agric_Land["Nigeria"], 
                        'Methane_Emissions': Methane_Emissions["Nigeria"]})

print(Nigeria)

# Fillna fills columns that have NaN values
Nigeria = Nigeria.fillna(0)
# Compute correlation of columns, removing NaN values
print(Nigeria.corr())

# HEAT MAP FOR NIGERIA
plt.imshow(Nigeria.corr(), cmap='Greens', interpolation='none')
plt.colorbar()
plt.xticks(range(len(Nigeria.columns)), Nigeria.columns, rotation=45)
plt.yticks(range(len(Nigeria.columns)), Nigeria.columns)

labels = Nigeria.corr().values
for y in range(labels.shape[0]):
    for x in range(labels.shape[1]):
        plt.text(x, y, '{:.2f}'.format(labels[y,x]), ha='center', va='center')
plt.title('Correlation Heatmap for Nigeria')
plt.show()

# CORRELATION FOR CHINA
China = pd.DataFrame({'UrbanPop': UrbanPop["China"], 
                      'Agric_Land': Agric_Land["China"], 
                      'Methane_Emissions': Methane_Emissions["China"], 
                      'Elect_Power_Cons': Elect_Power_Cons["China"]})

print(China)

# Fillna fills columns that have NaN values
China = China.fillna(0)
# Compute correlation of columns, removing NaN values
print(China.corr())

# HEAT MAP FOR CHINA
plt.imshow(China.corr(), cmap='Blues', interpolation='none')
plt.colorbar()
plt.xticks(range(len(China.columns)), China.columns, rotation=45)
plt.yticks(range(len(China.columns)), China.columns)

labels = China.corr().values
for y in range(labels.shape[0]):
    for x in range(labels.shape[1]):
        plt.text(x, y, '{:.2f}'.format(labels[y,x]), ha='center', va='center')
plt.title('Correlation Heatmap for China')
plt.show()



